# Importing library
from playwright.sync_api import sync_playwright


# 1) Opening website
p = sync_playwright().start()
browser = p.chromium.launch(headless=False)
context = browser.new_context()
page = context.new_page()
page.goto("https://demoqa.com/")

# 2) Clicking "Widgets"
page.locator("'Widgets'").dispatch_event("click")

# 3) Clicking "Auto Complete"
page.locator("'Auto Complete'").dispatch_event("click")

# 4) Writting "bl" and then selecting "black"
page.locator("id=autoCompleteMultipleInput").fill("bl")
page.keyboard.press("ArrowDown")
page.keyboard.press("Enter")

# 5) Clicking "Date Picker"
page.locator("'Date Picker'").dispatch_event("click")

# 6.a) Writting date ("01/01/2000")
page.locator("id=datePickerMonthYearInput").fill("01/01/2000")
page.keyboard.press("Enter")

# 6.b) Writting date and time ("January 1, 2000 8:00 AM")
page.locator("id=dateAndTimePickerInput").fill("January 1, 2000 8:00 AM")
page.keyboard.press("Enter")

# 7.a) Clicking "Elements"
page.locator("'Elements'").dispatch_event("click")

# 7.b) Clicking "Web Tables"
page.locator("'Web Tables'").dispatch_event("click")

# 8) Clicking "Add"
page.locator("'Add'").dispatch_event("click")

# 9.a) Writting first name ("Teddy")
page.locator("id=firstName").fill("Teddy") 

# 9.b) Writting last name ("Smith")
page.locator("id=lastName").fill("Smith")

# 9.c) Writting email ("test@test.com")
page.locator("id=userEmail").fill("test@test.com")

# 9.d) Writting age ("20")
page.locator("id=age").fill("20")

# 9.e) Writting salary ("1000")
page.locator("id=salary").fill("1000")

# 9.f) Writting department ("A")
page.locator("id=department").fill("A")

# 10) Clicking "Submit"
page.locator("'Submit'").dispatch_event("click")

# 11) Deleting the row with first name = "Kierra"
rows = page.locator("xpath=/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div")

for i in range(1, rows.count()+1):
    element =  page.locator("xpath=/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[" + str(i) + "]/div/div[1]")
    first_name = element.inner_text()
    
    if first_name == "Kierra":
        page.locator("xpath=/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[" + str(i) + "]/div/div[7]/div/span[2]").dispatch_event("click") 

# 12) Closing the browser
context.close()
browser.close()