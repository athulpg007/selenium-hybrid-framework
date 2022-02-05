from selenium import webdriver
import pytest

@pytest.fixture()

def setup(browser):
	if browser=="firefox":
		driver=webdriver.Firefox()
	
	elif browser=="chrome":
		driver=webdriver.Chrome()

	else:
		driver=webdriver.Firefox()

	return driver


def pytest_addoption(parser):
	parser.addoption("--browser")

@pytest.fixture()
def browser(request):
	return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Athul'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

