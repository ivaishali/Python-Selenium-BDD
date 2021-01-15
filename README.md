# Python-Selenium-BDD-Framework

Description
=============
Test Automation Framework using selenium and Python with the below features:

* Framework is based on page object model.
* Reporting using Allure report.
* Reading locators from JSON file.
* Reading test data from JSON file.
* Configured Behave as BDD 


Install dependences
=====================
* Install the depended packages in ``requirements.txt`` using ``pip install -r requirements.txt``


Create new test case
=====================

In order to create a new test case using the **Framework**, you have to follow the below steps:

* In **locators module**, create a new locator for the element you would like to use, as below:


        [{
            "pageName": "HomePage",
            "name": "link_login",
            "locateUsing": "xpath",
            "locator": "//a[contains(text(),'Log In')]"
        }]

* In **test data module**, add the test data needed for your test case, as below:

        {
            "environment": "https://learn.letskodeit.com/",
            "browser": "firefox",
            "email": "test@email.com",
            "password": "abcabc"
        }


* If the element exist in more than one page (**Navigation element**), use **navigation module** to create a script for that navigation bar and add your navigation action to that element, as below:

        def goToLoginPage(self):
            self.elementClick(*self.locator(self.homePage_locators, 'link_login'))

* If the element exists in only one page, go to **page module** and create a new script for that page e.g: ``login_page.py`` and add all the actions in that page, as below:

        def login(self, email, password):
            self.sendKeys(email, *self.locator(self.loginPage_locators, 'input_email'))
            self.sendKeys(password, *self.locator(self.loginPage_locators, 'input_password'))
            self.elementClick(*self.locator(self.loginPage_locators, 'btn_login'))


Run the test case
==================

In order to run the test case after creation, use on of the below commands:
``behave --tags=@regression``
``behave -f allure_behave.formatter:AllureFormatter -o allure-report --tags=@regression``

``allure serve allure_report``


