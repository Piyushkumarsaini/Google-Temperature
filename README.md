# Google Temperature Scraper using Django & BeautifulSoup

This project allows users to get the current temperature of any city using Google search results. It uses web scraping with `BeautifulSoup` to extract live data and displays it via a Django-powered API. The temperature data is also stored in a MySQL database for further analysis.

## 📌 Features

- Get current temperature of any city via Google search
- Store data (city, temperature, time, date) in MySQL
- Automatically create the table if not exists
- Track highest and lowest temperatures for a city (on the same day)
- Fetch temperature using a simple API endpoint

## ⚙️ Technologies Used

- **Python**
- **Django**
- **Web Scraping** – BeautifulSoup, Requests
- **MySQL** – Manual table creation and data handling using `mysql.connector`
- **JSON & API** – Django `JsonResponse` to return temperature data
- **Postman** – For API Testing
- **Git & GitHub** – Version control and collaboration

## 📁 Project Structure

- `views.py`:
  - `TemperatureScrap`: Scrapes temperature from Google, saves to database, and shows current, lowest, and highest temperatures.
  - `user_input`: Accepts JSON input from user and extracts city name.
- `MySQL Database`:
  - Table: `google_detail`
  - Columns: `City_Name`, `Temperature`, `Time`, `Date`

## 📦 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Piyushkumarsaini/Google-Temperature.git
