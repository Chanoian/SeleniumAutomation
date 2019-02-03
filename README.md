"MySeleniumLibrary.py" is Python 3 based Library , which uses Selenium API in the backend.
"ShoppingTestCase.robot" this is the test case which will call the libray's function to test specific scenario.
The output of this test case will be located in html FORMAT file named "log.html" in the same directory.

When you run this test case it will reproduce two .png capture.
endOfTestScreenShot.png : this will get captured in the end of the test case.
failureScreenShot.png : this will get captured if there is any failure detected during the test case.

All the available variables in the robot file can be changed easily from the CLI by using the --variable:

How to run:

pybot --variable first_name: yourName ShoppingTestCase.robot
