import requests
from bs4 import BeautifulSoup


try:
    # Taking city name from user
    cite_name = input("enter the cite name : ")


    # Define user agent headers to mimic a web browser
    HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'})


    # Construct the URL for the Google search
    url = "https://www.google.com/search?q=temperature+in+"+cite_name


    # Send a GET request to the URL
    response = requests.get(url,headers=HEADERS)



     
    # Check if the response status code is 200 (OK)
    if response.status_code == 200:

        # Collect the content of the response
        content_response = response.content

        # Parse the content with BeautifulSoup
        soup = BeautifulSoup(content_response, "html.parser")



        # Extract relevant information
        cite_and_state_name = soup.find("span", class_="BBwThe").text
        temperature = soup.find("span", class_="wob_t q8U8x").text
        degrees_temperature = soup.find("span",role="button").text
        sunny = soup.find("div", class_="VQF4g").text




        # Display the weather information
        print("Weather in " + cite_and_state_name + ": " + temperature + degrees_temperature + ", " + sunny)
    else:
        print("The request to the URL was unsuccessful. Please try again.")

except:
    print("The name you entered is not correct. Please enter the correct name.")

