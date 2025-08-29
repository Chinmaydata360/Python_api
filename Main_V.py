# this application will fetch crypto currency data from coingeko site
# find top 10 to sell
# find bottom to buy 
# send mail to me every day at 8 am

# sechedule
#smtplib
#requests
#datetime
#pandas 
#time


# task 
# download the dataset from the coingeko
# send mail
# svhedule task 8 am

import smtplib # send email
from  email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import email.encoders

import requests
import schedule
from datetime import datetime
import time
import pandas as pd



def send_mail(subject,body,filename):
    #smtp_server
    smtp_server="smtp.gmail.com" #gmail smpt server
    smtp_port=587          #Port foR encryption
    sender_mail="chinmayjoshids@gmail.com"  # gmail of sender
    email_pasword="**********" #Gmail App Password
    recevier_mail="chinmayjoshi311@gmail.com" ## Receiver email address

    # compose the mail
    message=MIMEMultipart()  # Create a multi-part email (can include text + attachments)
    message["From"]=sender_mail   # Sender email
    message["To"]=recevier_mail  # Receiver email
    message["Subject"]= subject  # Email subject

    # attaching body
    message.attach(MIMEText(body,"plain")) # Attach the plain text body to the email

    #attach csv file
    #attach the file

    with open (filename,"rb") as file:    # Open the file in binary mode
        part=MIMEBase("application","octet-stream")  # Define MIME type as binary stream (generic for attachments)
        part.set_payload(file.read())  # Read file content and set as payload
        email.encoders.encode_base64(part) # Encode file in Base64 so it can be sent via email
        part.add_header('Content-Disposition',f'attachment; filename="{filename}"') # Mark as attachment
        message.attach(part) # Attach file part to the message

    
    # start server

    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:   # Connect to Gmail SMTP server
        
            server.starttls()  # Start TLS encryption
        
            server.login(sender_mail,email_pasword) # Login with sender email + app password
        
            server.sendmail(sender_mail,recevier_mail,message.as_string()) # Send the email
    
            print("Email send successfull")

    
    except Exception as e:
        print(f"unable to send mail") # if not send print this







def get_cyrpto_data():

    url='https://api.coingecko.com/api/v3/coins/markets'
    param={
        "vs_currency":"usd",
        "order":"market_cap_desc",
        "per_page":250,
        "page":1
    }

    # sending request
    response=requests.get(url,params=param)

    if (response.status_code==200):
        print("Getting data")

        # storing the responce into data
        data=response.json()
        # creating the datafarme
        df=pd.DataFrame(data)

        #print(df.columns)
        #print(df.head(2))
        df=df[[
            "id","current_price","market_cap","price_change_percentage_24h",
            "high_24h","low_24h","ath","atl"
        ]]

        # creating new columns
        today=datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        df["time_stamp"]=today

        #top_negative 10 
        top_negative_10=df.nsmallest(10,"price_change_percentage_24h")

        top_negative_10.to_csv(f"top_negative_10.csv",index=False)

        top_positive_10=df.nlargest(10,"price_change_percentage_24h")

        top_negative_10.to_csv(f"top_positive_10.csv",index=False)

        



        # to save the data
        file_name="crypto_data.csv"
        df.to_csv(f"crypto_data.csv",index=False)
        print("Data Saved successfull")

        #top 

        # call the email function to send mail report

        subject=f"Top crypto currency to invest"
        body="""
        Good Morning \n\n

        Your crypto report in here

        Top crypto with higest price increass in last 24 hr\n
        top {top_negative_10}\n\n\n

        Top crypto with higest decrease in last 24 hr\n
        Bottom{top_negative_10}\n\n\n     

        Attached 250 plus crypto currency lattest report  
          
        Thanks,
        Chinmay  """
        #sending mail
        send_mail(subject,body,file_name)


    else:
        print("Not good")

#

if __name__=="__main__":

    #call the function

    schedule.every().day.at("13:16").do(get_cyrpto_data)

    while True:
        schedule.run_pending()



