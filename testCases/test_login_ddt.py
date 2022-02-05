import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_002_DDT_Login:

	baseUrl = ReadConfig.getApplicationURL()
	path = "./TestData/LoginData.xlsx"
	
	logger = LogGen.loggen()		


	def test_login_ddt(self, setup):

		self.logger.info("****************** Test_002_DDT_Login    ******************** ")
		self.logger.info("****************** Verifying login test  ******************** ")

		self.driver = setup
		
		self.rows = XLUtils.getRowCount(self.path, 'Sheet1')

		list_status = []

		for r in range(2, self.rows+1):


			self.username = XLUtils.readData(self.path, 'Sheet1', r, 1 )
			self.password = XLUtils.readData(self.path, 'Sheet1', r, 2 )
			self.exp      = XLUtils.readData(self.path, 'Sheet1', r, 3 )

			self.driver.get(self.baseUrl)

			self.LP = LoginPage(self.driver)


			self.LP.setUserName(self.username)
			self.LP.setPassword(self.password)
			self.LP.clickLogin()
			
			time.sleep(3)


			act_title = self.driver.title
			exp_title="Dashboard / nopCommerce administration"

			if act_title == exp_title:
				if self.exp=="pass":
					self.logger.info("****************** Passed login test  ******************** ")
					self.LP.clickLogout()
					list_status.append("pass")
					
				elif self.exp=="fail":
					self.logger.info("****************** Failed login test  ******************** ")
					self.LP.clickLogout()
					list_status.append("fail")

					

			elif act_title!=exp_title:
				if self.exp == 'pass':
					self.logger.info("**** failed ****")
					list_status.append("fail")
				elif self.exp == 'fail':
					self.logger.info("**** passed ****")
					list_status.append("pass")	

		if "fail" not in list_status:
			self.logger.info("******* DDT Login test passed **********")
			self.driver.close()
			assert True
		else:
			self.logger.error("******* DDT Login test failed **********")
			self.driver.close()
			assert False

		self.logger.info("******* End of Login DDT Test **********")
		self.logger.info("**************** Completed  TC_LoginDDT_002 ************* ");


		


