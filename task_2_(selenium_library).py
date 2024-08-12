# Importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 


# Function to open websites
def open_website(site):
    global driver
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    driver = webdriver.Chrome(options = chrome_options)
    driver.get(site)
    
# Function to click buttons
def click_button(full_xpath):
    button = driver.find_element(By.XPATH, full_xpath) 
    driver.execute_script("arguments[0].click();", button)
    
# Function to fill empty fields
def fill_field(field_id, field_text):
    global field
    field = driver.find_element(By.ID, field_id)
    field.send_keys(field_text)
    
# Function to clean field and input date
def fill_date(field_id, field_text):
    box = driver.find_element(By.ID, field_id)
    box.send_keys(Keys.CONTROL + "a")
    box.send_keys(field_text)
    box.send_keys(Keys.ENTER)


# 1) Opening website
open_website("https://demoqa.com/")

# 2) Clicking "Widgets"
click_button("/html/body/div[2]/div/div/div[2]/div/div[4]/div/div[3]/h5")

# 3) Clicking "Auto Complete"
click_button("/html/body/div[2]/div/div/div/div[1]/div/div/div[4]/div/ul/li[2]/span")

# 4) Writting "bl" and then selecting "black"
fill_field("autoCompleteMultipleInput", "bl")
field.send_keys(Keys.DOWN)
field.send_keys(Keys.ENTER)

# 5) Clicking "Date Picker"
click_button("/html/body/div[2]/div/div/div/div[1]/div/div/div[4]/div/ul/li[3]/span")

# 6.a) Writting date ("01/01/2000")
fill_date("datePickerMonthYearInput", "01/01/2000")

# 6.b) Writting date and time ("January 1, 2000 8:00 AM")
fill_date("dateAndTimePickerInput", "January 1, 2000 8:00 AM")

# 7.a) Clicking "Elements"
click_button("/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/span/div/div[1]/span")

# 7.b) Clicking "Web Tables"
click_button("/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/div/ul/li[4]/span")

# 8) Clicking "Add"
click_button("/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/div[1]/button")

# 9.a) Writting first name ("Teddy")
fill_field("firstName", "Teddy") 

# 9.b) Writting last name ("Smith")
fill_field("lastName", "Smith")

# 9.c) Writting email ("test@test.com")
fill_field("userEmail", "test@test.com")

# 9.d) Writting age ("20")
fill_field("age", "20")

# 9.e) Writting salary ("1000")
fill_field("salary", "1000")

# 9.f) Writting department ("A")
fill_field("department", "A")

# 10) Clicking "Submit"
click_button("/html/body/div[4]/div/div/div[2]/form/div[7]/div/button")

# 11) Deleting the row with first name = "Kierra"
rows = driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div")

for i in range(1, len(rows)+1):
    element = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[" + str(i) + "]/div/div[1]")
    first_name = element.text
    
    if first_name == "Kierra":
        click_button("/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[" + str(i) + "]/div/div[7]/div/span[2]")   

# 12) Closing the browser
driver.close()