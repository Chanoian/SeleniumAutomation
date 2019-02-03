from selenium import webdriver
from selenium.webdriver.support.ui import *
from selenium.common.exceptions import *
from selenium.webdriver.common.by import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

__author__ = "Chanoian"
__email__ = "shanoian90@gmail.com"


class MySeleniumLibrary(object):

	ROBOT_LIBRARY_SCOPE = 'GLOBAL'

	def __init__(self):
		self.short_sleep = 3
		self.sleep = 10
		self.selenium = webdriver.Chrome()
		self.selenium.implicitly_wait(self.sleep)
		self.selenium.set_page_load_timeout(self.sleep)
		self.email_address_locator = "email_create"
		self.firstName_locator = "customer_firstname"
		self.lastName_locator = "customer_lastname"
		self.password_locator = "passwd"
		self.address_locator = "address1"
		self.city_locator = "city"
		self.postCode_locator = "postcode"
		self.country_locator = "id_country"
		self.state_locator = "id_state"
		self.phoneNumber_locator = "phone_mobile"
		self.terms_conditions_locator = "cgv"

	def __del__(self):
		self._take_screen_shot(filename="endOfTestScreenShot.png")
		self.selenium.close()

	def _take_screen_shot(self, filename="failureScreenShot.png"):
		try:
			self.selenium.save_screenshot(filename=filename)
		except IOError:
			raise IOError("Unable to take screen shot")

	def _find_element(self, locator, locator_type):
		try:
			if locator_type == 'id':
				element = self.selenium.find_element_by_id(locator)
			elif locator_type == "name":
				element = self.selenium.find_element_by_name(locator)
			elif locator_type == "xpath":
				element = self.selenium.find_element_by_xpath(locator)
			elif locator_type == "css":
				element = self.selenium.find_element_by_css_selector(locator)
			else:
				raise AssertionError("Not Valid locator_type")
			return element
		except NoSuchElementException:
			self._take_screen_shot()
			raise NoSuchElementException("Element with locator=%s was not found." % locator)

	def end_of_test(self):
		self.__del__()

	def look_for_text_on_the_current_page(self, value):
		delay = self.sleep
		i = 0
		while i < delay:
			if str(value) in self.selenium.page_source:
				break
			else:
				i += 1
		if i >= delay:
			raise AssertionError("Text=%s not found in this page" % value)

	def select_by_value_from_list(self, locator, locator_type, value):
		element = self._find_element(locator=locator, locator_type=locator_type)
		select = Select(element)
		select.select_by_visible_text(text=value)

	def type_text(self, locator, locator_type, value):
		element = self._find_element(locator=locator, locator_type=locator_type)
		element.send_keys(str(value))

	def go_to_web_page(self, url):
		try:
			self.selenium.get(url=url)
			self.selenium.maximize_window()
		except TimeoutException:
			self._take_screen_shot()
			raise TimeoutException("Timeout Error to reach url=%s" % url)

	def click_element(self, locator, locator_type):
		wait = WebDriverWait(self.selenium, self.sleep)
		if locator_type == "id":
			element = wait.until(EC.element_to_be_clickable((By.ID, locator)))
		elif locator_type == "name":
			element = wait.until(EC.element_to_be_clickable((By.NAME, locator)))
		elif locator_type == "xpath":
			element = wait.until(EC.element_to_be_clickable((By.XPATH, locator)))
		elif locator_type == "css":
			element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
		else:
			raise AssertionError("Not Valid locator_type")
		element.click()

	def mouse_over_locator(self, locator, locator_type):
		element = self._find_element(locator=locator, locator_type=locator_type)
		mouse = ActionChains(self.selenium).move_to_element(element)
		mouse.perform()

	def switch_frame_to_default(self):
		self.selenium.switch_to.default_content()
		sleep(self.short_sleep)

	def switch_frame_with_index(self, index):
		try:
			frame = self.selenium.find_elements_by_tag_name('iframe')[index]
			self.selenium.switch_to.frame(frame)
		except NoSuchFrameException:
			self._take_screen_shot()
			raise NoSuchFrameException("The Specified Frame was not found ", index)

	def click_and_type(self, locator, locator_type, value):
		element = self._find_element(locator=locator, locator_type=locator_type)
		element.click()
		element.send_keys(str(value))

	def click_and_select_by_value(self, locator, locator_type, value):
		element = self._find_element(locator=locator, locator_type=locator_type)
		element.click()
		select = Select(element)
		select.select_by_visible_text(text=value)
		element.click()

	def add_to_cart(self, size):
		self.switch_frame_with_index(index=0)
		self.click_and_select_by_value(locator="group_1", locator_type="name", value=size)
		self.click_element(locator="//p[@id='add_to_cart']/button/span", locator_type="xpath")
		self.switch_frame_to_default()

	def create_email(self, email_address):
		self.type_text(locator=self.email_address_locator, locator_type="id", value=email_address)
		self.click_element(locator="//button[@id='SubmitCreate']/span", locator_type="xpath")

	def input_first_name(self, first_name):
		self.click_and_type(locator=self.firstName_locator, locator_type="id", value=first_name)

	def input_last_name(self, last_name):
		self.click_and_type(locator=self.lastName_locator, locator_type="id", value=last_name)

	def input_password(self, password):
		self.click_and_type(locator=self.password_locator, locator_type="id", value=password)

	def input_state(self, state):
		self.click_and_select_by_value(locator=self.state_locator, locator_type="id", value=state)

	def input_city(self, city):
		self.click_and_type(locator=self.city_locator, locator_type="id", value=city)

	def input_country(self, country):
		self.click_and_select_by_value(locator=self.country_locator, locator_type="id", value=country)

	def input_address(self, address):
		self.click_and_type(locator=self.address_locator, locator_type="id", value=address)

	def input_post_code(self, post_code):
		self.click_and_type(locator=self.postCode_locator, locator_type="id", value=post_code)

	def input_phone_number(self, phone_number):
		self.click_and_type(locator=self.phoneNumber_locator, locator_type="id", value=phone_number)

	def accept_terms_and_conditions(self):
		self.click_element(locator=self.terms_conditions_locator, locator_type="name")


if __name__ == "__main__":
	new = MySeleniumLibrary()
	new.go_to_web_page(url="http://automationpractice.com")
	new.click_element(locator="//a[contains(text(),'Women')]", locator_type="xpath")
	new.click_element(locator="(//a[contains(text(),'Dresses')])[5]", locator_type="xpath")
	new.click_element(locator="(//a[contains(text(),'Summer Dresses')])[3]", locator_type="xpath")
	new.mouse_over_locator(locator="//img[@alt='Printed Chiffon Dress']", locator_type="xpath")
	new.click_element(locator="//div[@id='center_column']/ul/li[3]/div/div/div/a[2]", locator_type="xpath")
	new.switch_frame_with_index(index=0)
	sleep(3)
	new.click_and_select_by_value(locator="group_1", locator_type="name", value="M")
	sleep(3)
	new.click_element(locator="//p[@id='add_to_cart']/button/span", locator_type="xpath")
	new.switch_frame_to_default()
	sleep(5)
	new.click_element(locator="//div[4]/a/span", locator_type="xpath")
	new.click_element(locator="//div[3]/div/p[2]/a/span", locator_type="xpath")
	new.type_text(locator="email_create", locator_type="id", value="zookko12342213@gmail.com")
	new.click_element(locator="//button[@id='SubmitCreate']/span", locator_type="xpath")
	new.click_and_type(locator="customer_firstname", locator_type="id", value="testName")
	new.click_and_type(locator="customer_lastname", locator_type="id", value="lastName")
	new.click_and_type(locator="passwd", locator_type="id", value="myPassword")
	new.click_and_type(locator="address1", locator_type="id", value="myAddress")
	new.click_and_type(locator="city", locator_type="id", value="myCity")
	new.click_and_type(locator="postcode", locator_type="id", value="12345")
	new.click_and_select_by_value(locator="id_state", locator_type="id", value="Florida")
	new.click_and_select_by_value(locator="id_country", locator_type="id", value="United States")
	new.click_and_type(locator="phone_mobile", locator_type="id", value="1234567890")
	new.click_element(locator="//button[@id='submitAccount']/span", locator_type="xpath")
	new.click_element(locator="//div[@id='center_column']/form/p/button/span", locator_type="xpath")
	new.click_element(locator="cgv", locator_type="id")
	new.click_element(locator="//form[@id='form']/p/button/span", locator_type="xpath")
	new.look_for_text_on_the_current_page(value="Printed Chiffon Dress")
	sleep(5)