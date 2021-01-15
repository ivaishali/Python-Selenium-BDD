def verify_that(actualTxt, expectedTxt):
    assert actualTxt in expectedTxt, "Assertion Failure !! Actualt Text is %s and expcted Test is %s" % (
        actualTxt, expectedTxt)
