import requests
from bs4 import BeautifulSoup


try: 
    # Taking city name from user
    cite_name = input("enter the cite name : ")

    # USER IN'T SENDING MY INFORMATION TO HIS URL I'M SCRAPING YOUR DATA
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'})

    # The name taken from uses will be combined with the URL and searched.
    url = "https://www.google.com/search?q=temperature+in+"+cite_name

    # Response variable is collecting data from URL in get request.
    response = requests.get(url,headers=HEADERS)

    # Collecting the contacts of the get request data that has come inside the response variable.
    content_response = response.content

    # It will keep the data of content response inside the soup variable and will help in scraping. I have this data inside this variable and you can scrape it.
    soup = BeautifulSoup(content_response, "html.parser")

    cite_and_state_name = soup.find("span", class_="BBwThe").text
    
    # Is working on extracting the temperature data from inside the URL and converting it into text.
    temperature = soup.find("span", class_="wob_t q8U8x").text
    
    degrees_temperature = soup.find("span",role="button").text
    
    # I am extracting its sunny and converting it into text.
    sunny = soup.find("div", class_="VQF4g").text

    print("Weather in " + cite_and_state_name + ": " + temperature + degrees_temperature + ", " + sunny)
except:
    print("The name you entered is not correct. Please enter the correct name.")
