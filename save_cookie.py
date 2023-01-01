import pickle

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 요소 기다리는 패키지 import
from selenium.webdriver.common.keys import Keys # 7.4 Special Key import
from selenium.webdriver.support import expected_conditions as EC # 기다리는 조건
from selenium.webdriver import ActionChains # Action을 묶어주는 패키지

import time


url = "https://cafe.naver.com/scottycameron"

def exec_chrom():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    #userAgent = UserAgent(verify_ssl=False)
    #userAgent = UserAgent().random
    #chrome_options.add_argument(f'user-agent={userAgent}')
    chrome_options.add_argument('--incognito')
    browser = webdriver.Chrome(executable_path="/Users/eoorim/Desktop/Coding/Python/M.Oasis/golf-crawling-moasis/chromedriver 2",
                               options=chrome_options)
    browser.get(url)
    return browser


def login(browser):
    time.sleep(60)
    pickle.dump(browser.get_cookies(), open("naver_cookies.pkl", "wb")) #최초 로그인 후 쿠키 저장시에만
    cookies = pickle.load(open("naver_cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.get(url)


login(exec_chrom())

