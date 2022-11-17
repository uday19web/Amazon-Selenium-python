import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
#########################################################################
email = input("Please enter the email: ")
password = input("Please enter the password: ")
search = input("Enter the Book name to search: ")

'''I used Mozila firefox browser we need to download the driver
check text file named "Driver" for details'''
service_obj =Service(r"D:\Python\Firefox_Driver\64\geckodriver")
driver = webdriver.Firefox(service=service_obj)
driver.implicitly_wait(5)

driver.get("https://www.amazon.in/")
driver.find_element(By.XPATH, "//div[@class='nav-line-1-container']").click()
# Sign in button
driver.find_element(By.CSS_SELECTOR, "input[type = 'email']").send_keys(email)
driver.find_element(By.CSS_SELECTOR, ".a-button-input").click()
driver.find_element(By.ID, "ap_password").send_keys(password)
driver.find_element(By.ID, "signInSubmit").click()

# Click the cart button
driver.find_element(By.CSS_SELECTOR, ".nav-cart-icon").click()

try:
    # find the how many items in the cart
    cart_items = driver.find_element(By.CSS_SELECTOR, "#sc-subtotal-label-buybox").text
    item_count = cart_items.replace('(', "").split()
    # print(item_count)
    existing_cart_item = None
    if int(item_count[1]) > 0:
        existing_cart_item = driver.find_elements(By.XPATH, "//form/div[@data-name='Active Items']")

    for i in range(0, int(item_count[1])):

        for item in existing_cart_item:
            item.find_element(By.XPATH, "//span/input[@data-action='delete']").click()
            # driver.refresh()
        time.sleep(2)
    time.sleep(3)
    driver.find_element(By.ID, "twotabsearchtextbox").click()
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys(search)
    driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]').click()
except Exception as e:
    print(e)
    time.sleep(3)
    driver.find_element(By.ID, "twotabsearchtextbox").click()
    driver.find_element(By.ID, "twotabsearchtextbox").send_keys(search)
    driver.find_element(By.XPATH, '//input[@id="nav-search-submit-button"]').click()


# scroll down
driver.execute_script("window.scrollBy(0, 400);")
# selecting the first item
totalitems = driver.find_elements(By.XPATH, "(//h2/a/span)")
# print(len(totalitems))
item_list = []
for item in totalitems:
    item_list.append(item.text)
    if len(item_list) == 1:
        driver.find_element(By.LINK_TEXT, item_list[0]).click()
    break

# to handle the new tab
tabsopen =driver.window_handles

# to switch to new window or tab
driver.switch_to.window(tabsopen[1])

# click the add cart button
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button").click()

# click the proceed button
driver.find_element(By.XPATH, "//input[@name='proceedToRetailCheckout']").click()

# click the use this address button
driver.find_element(By.XPATH, "//span/input[@aria-labelledby='orderSummaryPrimaryActionBtn-announce']").click()

# it close the new tab and return to first window
driver.close()
# it refresh the main window
driver.switch_to.window(tabsopen[0])
driver.refresh()

