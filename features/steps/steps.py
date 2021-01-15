from time import sleep

from behave import given, when, then, step

from navigation.homeNavigation import HomeNavigation
from pages.loggedin_page import LoggedInPage
from pages.login_page import LoginPage
from utils.teststatus import TestStatus

PAGE_NAVIGATION_TIMER = 3
IDLE_TIMER = 2


@given('the app is launched')
def step_impl(context):
    try:
        homeNavigation = HomeNavigation(context.driver)
        ts = TestStatus(context.driver)
        ts.markFinal(homeNavigation.isAt, "Homepage is not loaded properly !!!")
        return
    except Exception as e:
        raise e
    finally:
        sleep(PAGE_NAVIGATION_TIMER)


@when(u'User navigate to login page')
def step_impl(context):
    homeNavigation = HomeNavigation(context.driver)
    homeNavigation.goToLoginPage()


@then(u'Verify user on login page')
def step_impl(context):
    loginPage = LoginPage(context.driver)
    ts = TestStatus(context.driver)
    ts.markFinal(loginPage.isAt, "navigation to login page failed")


@step(u'User login with username "{email}" and password "{password}"')
def step_impl(context, email, password):
    loginPage = LoginPage(context.driver)
    loginPage.login(email=email, password=password)


@step(u'Verify loggedin user')
def step_impl(context):
    ts = TestStatus(context.driver)
    loggedInPage = LoggedInPage(context.driver)
    ts.markFinal(loggedInPage.isAt, "login failed")
