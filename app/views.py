from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import mysql.connector as conn
import json
from django.views.decorators.csrf import csrf_exempt





con = conn.connect(
    host="localhost",
    port="3306",
    user="piyushkuamrsaini",
    passwd="piyush@gmail",
    database="google_temperature_detail"
)

# Connect to MySQL database
cursor = con.cursor()


# Create a cursor object to execute queries
create_table_for_database = cursor.execute("""
    create table if not exists google_detail(
    City_Name varchar(100),
    Temperature varchar(100),
    Time time,
    Date date)
    """)

con.commit()



def savedata_database(city_name, temperature, time, date):
    # execute so output (none)
    insert_data_for_database = cursor.execute("insert into google_detail(City_Name,Temperature,Time,Date)values(%s, %s, %s, %s)",(city_name, temperature, time, date))
    con.commit()



# Function to fetch lowest data from the database
def lowest_temperature(city,date):
    # for variable none value
    lowest_data = None
    #minimum data fetch for database 
    cursor.execute("select City_Name,min(Temperature),Time,Date from google_detail where City_Name = %s and Date = %s",(city,date))
    min_data = cursor.fetchone()
    if min_data is not None:
        city_name = min_data[0]
        temperature = min_data[1]
        time = min_data[2]
        date = min_data[3]
        lowest_data = {
            "city_name": city_name,
            "temperature": temperature,
            "time": str(time),
            "date": str(date)
            }

        return lowest_data



# Function to fetch highest data from the database
def highest_temperature(city,date): 
   # maximum data fetch for database
    highest_data = None
    cursor.execute("select City_Name,max(Temperature),Time,Date from google_detail where City_Name = %s and Date = %s",(city,date))
    max_data = cursor.fetchone()
    if max_data is not None:
        city_name = max_data[0]
        temperature = max_data[1]
        time = max_data[2]
        date = max_data[3]
        highest_data = {
            "city_name": city_name,
            "temperature": temperature,
            "time": str(time),
            "date": str(date)
            }

    return highest_data


@csrf_exempt
def user_input(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        city_name = payload.get('city_name')
        return HttpResponse(city_name)

@csrf_exempt
def TemperatureScrap(request,city):
    HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}
    url = "https://www.google.com/search?q=temperature+in+"+city
    response = requests.get(url,headers=HEADERS)


    if response.status_code == 200:
        content_response = response.content
        soup = BeautifulSoup(content_response, "html.parser")
        city_and_state_name = soup.find("span", class_="BBwThe").text
        temperature = soup.find("span", class_="wob_t q8U8x").text
        current_date = datetime.now().date()
        current_time = datetime.now().strftime("%H:%M:%S")


        # Fetch minimum and maximum data from the database
        lowest = lowest_temperature(city, current_date)
        highest = highest_temperature(city, current_date)
        savedata_database(city, temperature, current_time, current_date)    

        # show on new data for scrap
        new_data = {
            "todays_present": {
                "city_name": city_and_state_name,
                "temperature": temperature,
                "time": str(current_time),
                "date": str(current_date)
            },
            "todays_lowest": lowest,
            "todays_highest": highest
        }
        
        # Return the JSON response        
        return JsonResponse(new_data)       
    else:
        message = {"Erorr": "The request to the URL was unsuccessful. Please try again."}
        return JsonResponse(message)


def show_temperature():
    pass