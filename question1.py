import time
import re
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utility import highlighter

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
# install webdriver manager
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))

driver.get("https://automationpractice.com")
driver.find_element(By.CLASS_NAME, "login").click()
driver.find_element(By.ID, "email").send_keys("testautomationmfs@gmail.com")
driver.find_element(By.ID, "passwd").send_keys("TestAutomation@123")
driver.find_element(By.ID, "SubmitLogin").click()
driver.find_element(By.XPATH, "//*[@id='center_column']/ul/li/a").click()
time.sleep(2)
product1 = driver.find_element(By.LINK_TEXT, "Faded Short Sleeve T-shirts").text
time.sleep(2)
element = driver.find_element(By.CSS_SELECTOR, "#homefeatured > .ajax_block_product:nth-child(1) .replace-2x")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
price1 = driver.find_element(By.CSS_SELECTOR,
                             "#homefeatured > .ajax_block_product:nth-child(1) .left-block .price").text

element = driver.find_element(By.CSS_SELECTOR, "#homefeatured > .ajax_block_product:nth-child(2)")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.find_element(By.CSS_SELECTOR, ".hovered .left-block .price").click()
product2 = driver.find_element(By.LINK_TEXT, "Blouse").text
price2 = driver.find_element(By.CSS_SELECTOR, ".hovered .left-block .price").text

element = driver.find_element(By.CSS_SELECTOR, "#homefeatured > .ajax_block_product:nth-child(3) .replace-2x")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
product3 = driver.find_element(By.LINK_TEXT, "Printed Dress").text
price3 = driver.find_element(By.CSS_SELECTOR,
                             "#homefeatured > .ajax_block_product:nth-child(3) .left-block .price").text

element = driver.find_element(By.CSS_SELECTOR, "#homefeatured > .ajax_block_product:nth-child(4) .replace-2x")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
product4 = driver.find_element(By.LINK_TEXT, "Printed Dress").text
price4 = driver.find_element(By.CSS_SELECTOR,
                             "#homefeatured > .ajax_block_product:nth-child(4) .left-block .price").text

element = driver.find_element(By.CSS_SELECTOR, "#homefeatured > .ajax_block_product:nth-child(5) .replace-2x")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
product5 = driver.find_element(By.LINK_TEXT, "Printed Summer Dress").text
price5 = driver.find_element(By.CSS_SELECTOR,
                             "#homefeatured > .ajax_block_product:nth-child(5) .left-block .price").text

element = driver.find_element(By.CSS_SELECTOR, "#homefeatured > .ajax_block_product:nth-child(6) .replace-2x")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
product6 = driver.find_element(By.LINK_TEXT, "Printed Summer Dress").text
price6 = driver.find_element(By.CSS_SELECTOR,
                             "#homefeatured > .ajax_block_product:nth-child(6) .left-block .price").text

element = driver.find_element(By.CSS_SELECTOR, "#homefeatured > .ajax_block_product:nth-child(7) .replace-2x")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
product7 = driver.find_element(By.LINK_TEXT, "Printed Summer Dress").text
price7 = driver.find_element(By.CSS_SELECTOR,
                             "#homefeatured > .ajax_block_product:nth-child(7) .left-block .price").text

items = [
    (product1, price1),
    (product2, price2),
    (product3, price3),
    (product4, price4),
    (product5, price5),
    (product6, price6),
    (product7, price7)
]

items.sort(key=lambda item: item[1])
print(items)

driver.execute_script("scrollBy(0,250);")

driver.find_element(By.XPATH, "//a[contains(text(),\'Women\')]").click()
driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .subcategory-image .replace-2x").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "li:nth-child(2) > .subcategory-image .replace-2x").click()
driver.find_element(By.ID, "layered_id_attribute_group_2").click()
time.sleep(3)
driver.find_element(By.ID, "layered_id_attribute_group_24").click()
time.sleep(3)
driver.execute_script("window.scrollTo(0,600)")
time.sleep(4)

elem1 = driver.find_element(By.XPATH, "//div[@id='left_column']//a[2]")
time.sleep(7)

ActionChains(driver).click_and_hold(elem1).pause(1).move_by_offset(-57, 0).release().perform()
time.sleep(4)
driver.find_element(By.XPATH, "//div[@class='right-block']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='More']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//i[@class='icon-plus']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//i[@class='icon-plus']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[@id='color_24']").click()
time.sleep(2)
dropdown = driver.find_element(By.ID, "group_1")
dropdown.find_element(By.XPATH, "//option[. = 'M']").click()
time.sleep(3)
driver.find_element(By.XPATH, "//span[normalize-space()='Add to cart']").click()
driver.find_element(By.CSS_SELECTOR, ".exclusive > span").click()
time.sleep(7)
assert driver.find_element(By.ID, "layer_cart_product_attributes").text == "Pink, M"
#  verify product_quantity is 3
assert driver.find_element(By.ID, "layer_cart_product_quantity").text == "3"
#  verify products_total is $152.97
assert driver.find_element(By.CSS_SELECTOR, ".ajax_block_products_total").text == "$152.97"
# verify cart_shipping_cost is $2.00
assert driver.find_element(By.CSS_SELECTOR, ".ajax_cart_shipping_cost:nth-child(2)").text == "$2.00"
#  verify block_cart_total $154.97
assert driver.find_element(By.CSS_SELECTOR, ".ajax_block_cart_total:nth-child(2)").text == "$154.97"

total_product_cost = driver.find_element(By.CSS_SELECTOR, ".ajax_block_products_total").text
shipping_cost = driver.find_element(By.CSS_SELECTOR, ".ajax_cart_shipping_cost:nth-child(2)").text
total_cost = driver.find_element(By.CSS_SELECTOR, ".ajax_block_cart_total:nth-child(2)").text
quantity = driver.find_element(By.ID, "layer_cart_product_quantity").text
size = driver.find_element(By.ID, "layer_cart_product_attributes").text


def price_to_float(price: str) -> float:
    # clean the price string
    trimmer = re.compile(r'[^\d.,]+')
    trimmed = trimmer.sub('', price)

    # figure out the separator which will always be "," or "." and at position -3 if it exists
    decimal_separator = trimmed[-3:][0]
    if decimal_separator not in [".", ","]:
        decimal_separator = None

    # re-clean now that we know which separator is the correct one
    trimer = re.compile(rf'[^\d{decimal_separator}]+')
    trimmed = trimer.sub('', price)

    if decimal_separator == ",":
        trimmed = trimmed.replace(",", ".")

    result = float(trimmed)
    return result


x = ((price_to_float(total_product_cost)) + (price_to_float(shipping_cost)))
y = price_to_float(total_cost)
assert x == y

print(quantity),
print(size),
print(total_product_cost),
print(shipping_cost),
print(total_cost)

driver.close()
