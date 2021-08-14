from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
#import chromedriver_binary

user_input = input("Enter the location you would like to get weather information for.")

#Setup webdriver
option = webdriver.ChromeOptions()
option.add_argument("headless")

#driver = webdriver.Chrome(executable_path = "/Users/eduardo/Documents/projects/Weather/chromedriver")
driver = webdriver.Chrome(ChromeDriverManager().install(), options = option)
driver.get("https://www.weather.gov/")



#Click text box to activate

driver.find_element_by_xpath("//*[@id='inputstring']").click()
#submit information to input box
search_box = driver.find_element_by_xpath("//*[@id='inputstring']")
search_box.send_keys(user_input)

#click the go button
time.sleep(1)
submit_button = driver.find_element_by_xpath("//*[@id='btnSearch']")
submit_button.click()

#get url for desired website
time.sleep(2)
page_url = driver.current_url
print(page_url)

#set up html of page

#page_url = "https://forecast.weather.gov/MapClick.php?lat=37.777120000000025&lon=-122.41963999999996#.YRbhui1h1B0"
page = requests.get(page_url)

#Test for html output
#print(page.text)
	
#create soup for page
soup = BeautifulSoup(page.content, "html.parser")




#isolate weather information box in web page
weather_information = soup.find(id = "current-conditions")

#get weather information
location = weather_information.find("h2", class_ = "panel-title").text.split(',')
location = location[0]
sky = weather_information.find("p", class_ = "myforecast-current").text
temp = weather_information.find("p", class_ = "myforecast-current-lrg").text

#isolate table where the humidity element is
information_table = weather_information.find(id = "current_conditions_detail")
#get humidity string and split into list
humidity = information_table.find("tr").text.split("\n")
humidity = humidity[2] #store humidity into variable

final_information = """

Location: {}
Forcast: {}
Temperature: {}
Humidity: {}

""".format(location, sky, temp, humidity)

print(final_information)












