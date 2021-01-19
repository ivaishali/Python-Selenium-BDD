import os
from base.webdriverfactory import WebDriverFactory

IDLE_TIMER = 3

global gCWD, gSCREEN_SHOTS_PATH
CWD = os.getcwd()
gSCREEN_SHOTS_PATH = CWD + "/reports/screenshots/"


# Hooks
def before_all(context):
    print("Running class setUp")
    wdf = WebDriverFactory()
    driver = wdf.getWebDriverInstance()

    if context is not None:
        context.driver = driver


def after_all(context):
    context.driver.quit()
    print("Running class tearDown")


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    pass


def after_scenario(context, scenario):
    pass


def after_feature(context, feature):
    pass


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def before_tag(context, tag):
    pass


def after_tag(context, tag):
    pass
