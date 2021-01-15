import os

import utils.read_json as RJ


def testData(attribute):
    testDataPath = os.path.abspath("./data/test_data.json")
    testDataJsonFile = RJ.readJson(testDataPath)
    return testDataJsonFile[attribute]
