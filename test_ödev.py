from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

import pytest
from pathlib import Path
from datetime import date

class Test_sauceDemo:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.waitForElementVisible((By.ID,"user-name"))
        self.waitForElementVisible((By.ID,"password"))   
        self.folderPath = str(date.today())
        Path(self.folderPath).mkdir(exist_ok=True)  

    def teardown_method(self):
        self.driver.quit()

    @pytest.mark.parametrize("username,password",[("","")]) 
    def test_bos_username_password(self,username,password):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        loginBtn = self.driver.find_element(By.ID,"login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        self.driver.save_screenshot(f"{self.folderPath}/test-bos-username&password.png")
        assert errorMessage.text == "Epic sadface: Username is required"
    
    @pytest.mark.parametrize("username, password", [("standard_user", "")])
    def test_bos_password(self, username, password):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys(username)
        passwordInput = self.driver.find_element(By.ID, "password")
        passwordInput.send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        error_message = self.driver.find_element(By.XPATH, "//h3").text
        self.driver.save_screenshot(f"{self.folderPath}/test-bos-password.png")
        assert error_message == "Epic sadface: Password is required"

    def test_locked_out_user(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        error_message = self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3").text
        self.driver.save_screenshot(f"{self.folderPath}/test-locked_out_user-secret_sauce.png")
        assert error_message == "Epic sadface: Sorry, this user has been locked out."
            
    @pytest.mark.parametrize("username,password",[("","")])
    def test_bos_inputs_x_icon(self,username,password):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        error1 = self.driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        self.driver.find_element(By.ID,"login-button").click()
        close_button = self.driver.find_element(By.XPATH,"//button[@class='error-button']")
        close_button.click()   
        error2 = self.driver.find_elements(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]")
        self.driver.save_screenshot(f"{self.folderPath}/test-buton.png")
        assert  error1 == error2
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce"),("problem_user","secret_sauce"),("performance_glitch_user","secret_sauce")])    
    def test_basarili_giris(self,username,password):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        usernameInput.send_keys(username)
        passwordInput = self.driver.find_element(By.ID,"password")
        passwordInput.send_keys(password)
        self.driver.find_element(By.ID,"login-button").click() 
        self.driver.save_screenshot(f"{self.folderPath}/test-basarili-giris.png")
        assert self.driver.current_url == "https://www.saucedemo.com/inventory.html"
    
    def test_ürün_sayisi(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        ürün_sayisi = len(self.driver.find_elements(By.XPATH,"//div[@class='inventory_item']"))
        self.driver.save_screenshot(f"{self.folderPath}/test-ürün-sayısı.png")
        assert ürün_sayisi == 6
    
    def test_backpackAdd(self):
        usernameInput = self.driver.find_element(By.ID,"user-name")
        passwordInput = self.driver.find_element(By.ID,"password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        button1 = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        button1.click
        button2 = self.driver.find_elements(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        self.driver.save_screenshot(f"{self.folderPath}/test-backpackAdd.png")
        assert button1 != button2
     
    def test_backpack_add_remove(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        buttonBefore = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        buttonBefore.click
        buttonAfter = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        buttonAfter.click
        self.driver.save_screenshot(f"{self.folderPath}/test_backpack_add_remove.png")
        assert buttonBefore == buttonAfter

    def test_bikeLight_add(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        button1 = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button")
        button1.click
        button2 = self.driver.find_elements(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button")
        self.driver.save_screenshot(f"{self.folderPath}/test-bikeLightAdd.png")
        assert button1 != button2
    
    @pytest.mark.parametrize("username,password",[("standard_user","secret_sauce")])      
    def test_shopping_cart(self,username,password):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        buttonLight = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button")
        buttonLight.click
        buttonPack = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button")
        buttonPack.click
        shopping_cart = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div[1]/div[3]/a")
        shopping_cart.click()
        currentUrl = self.driver.current_url
        self.driver.save_screenshot(f"{self.folderPath}/test-shoppingcart.png")
        assert  currentUrl == "https://www.saucedemo.com/cart.html"   
        
    def waitForElementVisible(self,locator,timeout=5):
        WebDriverWait(self.driver,timeout).until(ec.visibility_of_element_located(locator))        







