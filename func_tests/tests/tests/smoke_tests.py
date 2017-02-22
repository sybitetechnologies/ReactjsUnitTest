from wtframework.wtf.config import WTF_TIMEOUT_MANAGER, WTF_CONFIG_READER
from wtframework.wtf.testobjects.basetests import WTFBaseTest
from wtframework.wtf.web.webdriver import WTF_WEBDRIVER_MANAGER


class SmokeTest(WTFBaseTest):
    def setUp(self):
        self.driver = WTF_WEBDRIVER_MANAGER.new_driver()
        self.base_url = WTF_CONFIG_READER.get("selenium.baseurl")

    def test_smoke(self):
        driver = self.driver
        driver.get(self.base_url + "/src/index.html")
        WTF_TIMEOUT_MANAGER.brief_pause()

        res = driver.find_elements_by_xpath("//span[contains(text(), 'Application is Ready')]")
        self.assertTrue(len(res) > 0, "Application is Not Ready")

        driver.find_element_by_css_selector("p").click()

        res = driver.find_elements_by_xpath("//p[contains(text(), 'Text After Click')]")
        self.assertTrue(len(res) > 0, "Control Did Not Change State")
