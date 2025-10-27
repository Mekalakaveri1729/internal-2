import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from webdriver_manager.chrome import ChromeDriverManager
import time
@pytest.fixture
def setup_teardown():
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()
def get_alert_text(driver):
    alert = get_alert_text(driver) 
    text = alert.text
    alert.accept()
    return text
def test_empty_username(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "username").clear()
    driver.find_element(By.NAME, "password").send_keys("Kaveri@1252")
    driver.find_element(By.NAME, "sb").click()
    time.sleep(1)
    alert_text = get_alert_text(driver)
    assert alert_text == "Username cannot be empty"
def test_empty_password(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "username").send_keys("Kaveri")
    driver.find_element(By.NAME, "password").clear()
    driver.find_element(By.NAME, "sb").click()  
    time.sleep(1)
    alert_text = get_alert_text(driver)
    assert alert_text == "Password cannot be empty"
def test_short_password(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "username").send_keys("Kaveri")
    driver.find_element(By.NAME, "password").send_keys("Kav@1")
    driver.find_element(By.NAME, "sb").click() 
    time.sleep(1)
    alert_text = get_alert_text(driver) 
    assert alert_text == "Password must be at least 6 characters "
def test_valid_input(setup_teardown):
    driver = setup_teardown
    driver.get("http://127.0.0.1:5000/")
    driver.find_element(By.NAME, "username").send_keys("Kaveri")    
    driver.find_element(By.NAME, "password").send_keys("Kaveri@1252")
    driver.find_element(By.NAME, "sb").click()
    time.sleep(1)
    current_url=driver.current_url
    assert "/submit" in current_url,f"Expected URL geerting.html but got {current_url}"
    body_text=driver.find_element(By.TAG_NAME,"body").text
    assert "Hello, Kaveri! Welcome to our website !" in body_text, f"Expected greeting message not found in page body"
