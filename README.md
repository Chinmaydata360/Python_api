# 🚀 Crypto Data Automation & Reporting System  

This project fetches **live cryptocurrency data** from the CoinGecko API, identifies **top performers (to SELL)** and **bottom performers (to BUY)**, saves reports as CSV files, and automatically emails the report every morning at **8 AM**.  

---

## 📌 Features  
- Fetches live data of **250+ cryptocurrencies** using CoinGecko API  
- Identifies:  
  🔼 **Top 10 coins with highest % increase (SELL candidates)**  
  🔽 **Bottom 10 coins with highest % decrease (BUY candidates)**  
- Saves reports in CSV format (`crypto_data.csv`, `top_10.csv`, `bottom_10.csv`)  
- Sends an **automated email** with summary and full dataset attached  
- Runs automatically every day at **8 AM** using `schedule`  

---

## 🛠️ Tech Stack  
- **Python**  
- **Pandas** → Data wrangling  
- **Requests** → API calls  
- **smtplib & email.mime** → Email automation  
- **Schedule** → Task scheduling  

---

## 📂 Project Structure  
