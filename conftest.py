import pytest, os, logging
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from src.login import Login
from src.subscribe import Subscribe


@pytest.fixture(scope="session")
def chr_options(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.accept_untrusted_certs = True
    chrome_options.assume_untrusted_cert_issuer = True
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-impl-side-painting")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--disable-seccomp-filter-sandbox")
    chrome_options.add_argument("--disable-breakpad")
    chrome_options.add_argument("--disable-client-side-phishing-detection")
    chrome_options.add_argument("--disable-cast")
    chrome_options.add_argument("--disable-cast-streaming-hw-encoding")
    chrome_options.add_argument("--disable-cloud-import")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-session-crashed-bubble")
    chrome_options.add_argument("--disable-ipv6")
    chrome_options.add_argument("--allow-http-screen-capture")
    chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument("--headless")
    chrome_options.add_experimental_option(name="detach", value=True)
    #chrome_options.add_experimental_option("mobileEmulation", {"deviceName": "Nexus 5"})
    return chrome_options


# local connect
@pytest.fixture(scope="module")
def chr_driver(chr_options):
    path = os.path.abspath(os.path.dirname(__file__)) + "\src\exe\chromedriver.exe"
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'browser': 'ALL', 'performance': 'ALL'}
    driver = webdriver.Chrome(executable_path=path, options=chr_options, desired_capabilities=caps)
    yield driver
    #driver.quit()


@pytest.fixture(scope="module")
def login_obj(chr_driver):
    return Login(driver=chr_driver)


@pytest.fixture(scope="module")
def subscribe_obj(chr_driver):
    return Subscribe(driver=chr_driver)