import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

	baseUrl = ReadConfig.getApplicationURL()
	username = ReadConfig.getUserName()
	password = ReadConfig.getPassword()

	logger = LogGen.loggen()

	@pytest.mark.regression
	def test_homePageTitle(self, setup):

		self.logger.info("****************** Test_001_Login ******************** ")
		self.logger.info("****************** Verifying title test  ******************** ")

		self.driver = setup
		self.driver.get(self.baseUrl)
		act_title = self.driver.title
		
		if act_title=="Your store. Login":
			self.logger.info("****************** Passed title test ******************** ")
			self.driver.close()
			assert True
			
		else:
			self.logger.error("****************** Failed title test  ******************** ")
			self.driver.save_screenshot("./Screenshots/"+"test_homePageTitle.png")
			self.driver.close()
			assert False
			

	@pytest.mark.sanity
	@pytest.mark.regression
	def test_login(self, setup):

		self.logger.info("****************** Verifying login test  ******************** ")

		self.driver = setup
		self.driver.get(self.baseUrl)

		self.LP = LoginPage(self.driver)
		self.LP.setUserName(self.username)
		self.LP.setPassword(self.password)
		self.LP.clickLogin()

		act_title = self.driver.title
		

		if act_title == "Dashboard / nopCommerce administration":
			self.logger.info("****************** Passed login test  ******************** ")
			self.driver.close()
			assert True
		else:
			self.logger.error("****************** Failed login test  ******************** ")
			
			self.driver.save_screenshot("./Screenshots/"+"test_login.png")
			self.driver.close()
			assert False
			


		


