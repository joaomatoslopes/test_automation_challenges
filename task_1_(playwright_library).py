# Importing library
from playwright.sync_api import sync_playwright


# Dictionary with person's information
info = {"Student Name": "Teddy Smith",
        "Gender": "Other",
        "Mobile": "1234567891",
        "Date of Birth": "01 January,2000",
        "Hobbies": {"Sports", "Music"},
        "State and City": "NCR Delhi"}


# 1) Opening website
p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
page.goto("https://demoqa.com/")

# 2) Clicking "Forms"
page.locator("'Forms'").dispatch_event("click")

# 3) Clicking "Practice Form"
page.locator("'Practice Form'").dispatch_event("click")

# 4.a) Writting first name ("Teddy")
page.locator("id=firstName").fill(info["Student Name"].split(" ")[0])

# 4.b) Writting last name ("Smith")
page.locator("id=lastName").fill(info["Student Name"].split(" ")[1])

# 4.c) Selecting gender ("Other")
page.locator("'Other'").dispatch_event("click")

# 4.d) Writting mobile number ("1234567891")
page.locator("id=userNumber").fill(info["Mobile"])

# 4.e) dWritting date of birth ("01 Jan 2000")
page.locator("id=dateOfBirthInput").fill(info["Date of Birth"][:6] + " " + info["Date of Birth"][-4:])
page.keyboard.press("Enter")

# 4.f) Selecting hobbies ("Sports" + "Music")
page.locator("'Sports'").dispatch_event("click")
page.locator("'Music'").dispatch_event("click")

# 4.g) Writting state ("NCR")
page.locator("id=react-select-3-input").fill(info["State and City"].split(" ")[0])
page.keyboard.press("Enter")

# 4.h) Writting city ("Delhi")
page.locator("id=react-select-4-input").fill(info["State and City"].split(" ")[1])
page.keyboard.press("Enter")

# 5) Clicking "Submit"
page.locator("'Submit'").dispatch_event("click")

# 6) Checking the information in the pop-up window
rows = page.locator("xpath=/html/body/div[4]/div/div/div[2]/div/table/tbody/tr")

errors = 0
for i in range(1, rows.count()+1):
    label_element = page.locator("xpath=/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[1]")
    label = label_element.inner_text()
    value_element = page.locator("xpath=/html/body/div[4]/div/div/div[2]/div/table/tbody/tr[" + str(i) + "]/td[2]")
    value = value_element.inner_text()
    
    if label in info.keys():
        if (label == "Hobbies" and info[label] != set(value.split(", "))) or (label != "Hobbies" and info[label] != value):
            errors += 1
            print("'" + label + "' information is incorrect.")

if errors == 0:
    print("All informations are correct.")

# 7) Clicking "Close"
page.locator("'Close'").dispatch_event("click")

# 8) Closing the browser
context.close()
browser.close()