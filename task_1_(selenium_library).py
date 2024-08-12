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


# Dictionary with person's information
info = {"Student Name": "Teddy Smith",
        "Gender": "Other",
        "Mobile": "1234567891",
        "Date of Birth": "01 January,2000",
        "Hobbies": {"Sports", "Music"},
        "State and City": "NCR Delhi"}


# 1) Opening website
open_website("https://demoqa.com/")

# 2) Clicking "Forms"
click_button("/html/body/div[2]/div/div/div[2]/div/div[2]/div/div[3]/h5")

# 3) Clicking "Practice Form"
click_button("/html/body/div[2]/div/div/div/div[1]/div/div/div[2]/div/ul/li/span")

# 4.a) Writting first name ("Teddy")
fill_field("firstName", info["Student Name"].split(" ")[0]) 

# 4.b) Writting last name ("Smith")
fill_field("lastName", info["Student Name"].split(" ")[1])

# 4.c) Selecting gender ("Other")
click_button("/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/div[3]/input")

# 4.d) Writting mobile number ("1234567891")
fill_field("userNumber", info["Mobile"])

# 4.e) dWritting date of birth ("01 Jan 2000")
fill_date("dateOfBirthInput", info["Date of Birth"][:6] + " " + info["Date of Birth"][-4:])

# 4.f) Selecting hobbies ("Sports" + "Music")
click_button("/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[7]/div[2]/div[1]/input") # Sports
click_button("/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[7]/div[2]/div[3]/input") # Music

# 4.g) Writting state ("NCR")
fill_field("react-select-3-input", info["State and City"].split(" ")[0])
field.send_keys(Keys.ENTER)

# 4.h) Writting city ("Delhi")
fill_field("react-select-4-input", info["State and City"].split(" ")[1])
field.send_keys(Keys.ENTER)

# 5) Clicking "Submit"
click_button("/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[11]/div/button")

# 6) Checking the information in the pop-up window
rows = driver.find_elements(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr")

errors = 0
for i in range(1, len(rows)+1):
    label_element = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[1]")
    label = label_element.text
    value_element = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[2]")
    value = value_element.text
    
    if label in info.keys():
        if (label == "Hobbies" and info[label] != set(value.split(", "))) or (label != "Hobbies" and info[label] != value):
            errors += 1
            print("'" + label + "' information is incorrect.")

if errors == 0:
    print("All informations are correct.")
    
# 7) Clicking "Close"
click_button("/html/body/div[4]/div/div/div[3]/button")

# 8) Closing the browser
driver.close()