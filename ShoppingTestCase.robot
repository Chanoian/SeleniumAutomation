*** Settings ***
Library  BuiltIn
Library  MySeleniumLibrary.py
Suite Teardown  end of test

*** Variables ***
${browser}      chrome
${store_url}    http://automationpractice.com
${store_url_validator}      0123-456-789
${women_section_validator}  You will find here all woman fashion collections
${women_section_xpath}  //a[contains(text(),'Women')]
${women_page_validator}  You will find here all woman fashion collections.
${women_section_dresses_xpath}  (//a[contains(text(),'Dresses')])[5]
${women_section_summer_dresses_xpath}  (//a[contains(text(),'Summer Dresses')])[3]
${women_section_summer_validator}    Short dress, long dress
${women_section_dresses_printed_chiffon_dress_xpath}    //img[@alt='Printed Chiffon Dress']
${quick_view_string}   Quick view
${quick_view_xpath}   //div[@id='center_column']/ul/li[3]/div/div/div/a[2]
${proceed_to_check_out1_xpath}     //div[4]/a/span
${proceed_to_check_out2_xpath}     //div[3]/div/p[2]/a/span
${email_address}        myemailfortest2020@gmail.com
${first_name}           myFirstName
${last_name}            myLastName
${password}             myPasswd
${address}              1234 My Address
${city}                 myCity
${postCode}             12345
${state}                Florida
${country}              United States
${mobilePhone}          1234567890
${submit_locator1}      //button[@id='submitAccount']/span
${submit_locator2}      //div[@id='center_column']/form/p/button/span
${submit_locator3}      //form[@id='form']/p/button/span
${order_confirmation}   Printed Chiffon Dress


*** Test Cases ***
Go to http://automationpractice.com and Check for Phone Number
    go to web page      http://automationpractice.com
    look for text on the current page   ${store_url_validator}

Click On The Women Section and Check for You will find here all woman fashion collections
    click element   ${women_section_xpath}  xpath
    look for text on the current page   ${women_section_validator}

Click on Summer Dresses and Check for Short dress, long dress
    click element   ${women_section_dresses_xpath}  xpath
    click element   ${women_section_summer_dresses_xpath}   xpath
    look for text on the current page   ${women_section_summer_validator}

Mouse over Printed Chiffon Dress and Check for Quick View
    mouse over locator     ${women_section_dresses_printed_chiffon_dress_xpath}   xpath
    look for text on the current page   ${quick_view_string}
    click element   ${quick_view_xpath}     xpath

Add To Cart and Choose Medium Size
    add to cart   M

Click Proceed To Checkout
    click element    ${proceed_to_check_out1_xpath}      xpath
    click element    ${proceed_to_check_out2_xpath}      xpath

Type Emaill Address
    create email     ${email_address}

Type First Name
    input first name    ${first_name}

Type Last Name
    input last name     ${last_name}

Type Password
   input password       ${password}

Type Address
    input address       ${address}

Type City
    input city          ${city}

Type Post Code
    input post code     ${postCode}

Type State
    input state     ${state}

Type Country
    input country   ${country}

Type Mobile Phone
    input phone number      ${mobilePhone}

Proceed to Checkout
    click element       ${submit_locator1}      xpath
	click element       ${submit_locator2}      xpath


Accept Terms and Condition
    accept terms and conditions
    click element       ${submit_locator3}      xpath

Look for the order on the current page
    look for text on the current page       ${order_confirmation}