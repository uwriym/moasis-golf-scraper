import csv
import pickle

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from collections import Counter

from remove_stopwords import word_list
from remove_stopwords import eliminate_stopwords

import time

class DealbadaCrawler:
    def __init__(self, page):
        global KEYWORD
        self.post_count = 0
        self.page = page
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.KEYWORD = KEYWORD
        #KEYWORD = self.KEYWORD
        self.browser = webdriver.Chrome(executable_path="/Users/eoorim/Documents/seleniumpro/chromedriver 2", options=self.chrome_options)
        self.URL = f"https://www.dealbada.com/bbs/board_text_search.php?search={self.KEYWORD}#page=2&gsc.tab=0&gsc.q={self.KEYWORD}&gsc.page={page}"


    def wait_for(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))

    def extract_data(self):

        post_text_list = []
        comment_text_list = []

        self.wait_for((By.ID, "bo_v_con"))
        post = self.browser.find_element(By.ID, "bo_v_con")
        post_text_list.append(post.text)

        comments = self.browser.find_elements(By.CSS_SELECTOR, "section#bo_vc p")
        for comment in comments:
            comment_text_list.append(comment.text)

        return post_text_list + comment_text_list



    def crawling_start(self):
        global total_text_list
        self.browser.get(self.URL)
        self.wait_for((By.CLASS_NAME,"gs-title"))
        search_results = self.browser.find_elements(By.CSS_SELECTOR,"a.gs-title")

        for search_result in search_results:
            if "골프포럼" in search_result.text:
                try:
                    ActionChains(self.browser).key_down(Keys.COMMAND).click(search_result).perform()
                except:
                    pass
        # browser.quit()
        switch_count = 0
        for window in self.browser.window_handles:
            self.browser.switch_to.window(window)
            if switch_count > 0:
                self.wait_for((By.ID, "bo_v_con"))
                try:
                    total_text_list = total_text_list + self.extract_data()
                    time.sleep(.5)
                    print("Yes")
                    self.post_count += 1
                except:
                    print("Connection Refused")
                self.browser.close()
            time.sleep(.5)
            switch_count += 1
        self.browser.quit()


class GolfzoneMarketCrawler:
    def __init__(self):
        global KEYWORD
        self.post_count = 0
        # self.page = page
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.KEYWORD = KEYWORD[:-2]
        # KEYWORD = self.KEYWORD
        self.browser = webdriver.Chrome(executable_path="/Users/eoorim/Documents/seleniumpro/chromedriver 2",
                                        options=self.chrome_options)
        self.URL = f"https://www.golfzonmarket.com/search/list?reSearchWord={self.KEYWORD}&productLineCnt=20"

    def wait_for(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))

    def extract_data(self):
        review_text_list = []
        time.sleep(1)
        # 페이징
        review = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[4]/div[1]/div/a[3]")
        review.click()

        self.wait_for((By.CLASS_NAME, "r-txt"))
        rev_page = self.browser.find_element(By.CLASS_NAME, "r-txt")
        if ("개" in rev_page.text[3:6]):
            photo_rev_page = int(rev_page.text[3:5])
        else:
            photo_rev_page = int(rev_page.text[3:6])
        if ("개" in rev_page.text[12:15]):
            normal_rev_page = int(rev_page.text[12:14])
        else:
            normal_rev_page = int(rev_page.text[12:15])

        if photo_rev_page // 5 == 0:
            photo_rev_page //= 5
        else:
            photo_rev_page = (photo_rev_page // 5) + 1

        if normal_rev_page // 5 == 0:
            normal_rev_page //= 5
        else:
            normal_rev_page = (normal_rev_page // 5) + 1

        print(photo_rev_page, normal_rev_page)

        # Photo Review
        for i in range(1, photo_rev_page + 1):
            try:
                if i < 11:
                    self.wait_for((By.ID,"paging_photo"))
                    btn = self.browser.find_element(By.XPATH,f"/html/body/div[1]/div[5]/div[1]/div[4]/div[2]/div[3]/div/div[1]/div/a[{i}]")
                    btn.click()
                    self.wait_for((By.CLASS_NAME,"h1"))
                    time.sleep(1.5)

                elif i == 11:
                    next_btn = self.browser.find_element(By.XPATH,"/html/body/div[1]/div[5]/div[1]/div[4]/div[2]/div[3]/div/div[1]/div/a[12]")
                    next_btn.click()

                    self.wait_for((By.ID,"paging_photo"))
                    time.sleep(1.5)

                elif i > 11:
                    self.wait_for((By.ID, "paging_photo"))
                    btn = self.browser.find_element(By.XPATH, f"/html/body/div[1]/div[5]/div[1]/div[4]/div[2]/div[3]/div/div[1]/div/a[{i - 8}]")
                    btn.click()
                    self.wait_for((By.CLASS_NAME, "h1"))
                    time.sleep(1.5)

                elif i == 21:
                    next_btn = self.browser.find_element(By.XPATH, "/html/body/div[1]/div[5]/div[1]/div[4]/div[2]/div[3]/div/div[1]/div/a[13]")
                    next_btn.click()

                    self.wait_for((By.ID, "paging_photo"))
                    time.sleep(1.5)

                elif i > 21:

                    self.wait_for((By.ID, "paging_photo"))
                    btn = self.browser.find_element(By.XPATH, f"/html/body/div[1]/div[5]/div[1]/div[4]/div[2]/div[3]/div/div[1]/div/a[{i - 18}]")
                    btn.click()
                    self.wait_for((By.CLASS_NAME, "h1"))
                    time.sleep(1.5)


            except:
                pass

            try:
                photo_revs = self.browser.find_elements(By.CSS_SELECTOR, "div#photoRvArea > ul > li")

                print(f"------ Photo {i} page ------")

                for photo_rev in photo_revs:
                    if i < 22:
                        txt3 = photo_rev.find_elements(By.CLASS_NAME,"txt3")

                        for t in txt3:
                            print(t.text)
                            review_text_list.append(t.text)
                    else:
                        pass
            except:
                pass

        # Normal Review
        for i in range(1, normal_rev_page + 1):
            try:
                if i < 11:
                    self.wait_for((By.ID, "normal_paging"))
                    btn = self.browser.find_element(By.XPATH,
                                                    f"/html/body/div[1]/div[5]/div[1]/div[4]/div[2]/div[3]/div/div[2]/div/a[{i}]")
                    btn.click()
                    self.wait_for((By.CLASS_NAME, "h1"))
                    time.sleep(1.5)

                elif i == 11:
                    next_btn = self.browser.find_element(By.XPATH,
                                                         "/html/body/div[1]/div[5]/div[1]/div[4]/div[2]/div[3]/div/div[2]/div/a[12]")
                    next_btn.click()

                    self.wait_for((By.ID, "normal_paging"))
                    time.sleep(1.5)

                elif i > 11:
                    self.wait_for((By.ID, "normal_paging"))
                    btn = self.browser.find_element(By.XPATH,
                                                    f"/html/body/div[1]/div[5]/div[1]/div[4]/div[2]/div[3]/div/div[2]/div/a[{i - 8}]")
                    btn.click()
                    self.wait_for((By.CLASS_NAME, "h1"))
                    time.sleep(1.5)

                elif i == 21:
                    next_btn = self.browser.find_element(By.XPATH,
                                                         "/html/body/div[1]/div[5]/div[1]/div[4]/div[2]/div[3]/div/div[2]/div/a[13]")
                    next_btn.click()

                    self.wait_for((By.ID, "normal_paging"))
                    time.sleep(1.5)

                elif i > 21:
                    self.wait_for((By.ID, "normal_paging"))
                    btn = self.browser.find_element(By.XPATH,
                                                    f"/html/body/div[1]/div[5]/div[1]/div[4]/div[2]/div[3]/div/div[2]/div/a[{i - 18}]")
                    btn.click()
                    self.wait_for((By.CLASS_NAME, "h1"))
                    time.sleep(1.5)
            except:
                pass

            try:
                photo_revs = self.browser.find_elements(By.CSS_SELECTOR, "div#normalRvArea > ul > li")

                print(f"------ Normal {i} page ------")

                for photo_rev in photo_revs:
                    if i < 22:
                        txt3 = photo_rev.find_elements(By.CLASS_NAME, "txt3")

                        for t in txt3:
                            print(t.text)
                            review_text_list.append(t.text)
                    else:
                        pass
            except:
                pass

        return review_text_list

    def crawling_start(self):
        global total_text_list
        self.browser.get(self.URL)
        if self.KEYWORD == "캘러웨이":
            self.browser.find_element(By.ID, "chk-con20").click()
        else:
            self.browser.find_element(By.ID, "chk-con1").click()


        self.browser.maximize_window()

        # self.wait_for((By.CLASS_NAME,"bHwPlI"))
        # x_btn = self.browser.find_element(By.CLASS_NAME,"bHwPlI")
        # x_btn.click()

        goods = self.browser.find_elements(By.CLASS_NAME, "hover")
        #c = 0
        for good in goods:
            #if c == 3:
                #break
            ActionChains(self.browser).key_down(Keys.COMMAND).click(good).perform()
            #c += 1

        switch_count = 0
        for window in self.browser.window_handles:
            self.browser.switch_to.window(window)
            if switch_count > 0:
                self.wait_for((By.ID, "prdtImgPath"))
                time.sleep(1)
                try:
                    total_text_list = total_text_list + self.extract_data()
                except:
                    print("Connection Refused")
                self.browser.close()
            time.sleep(.5)
            switch_count += 1
        self.browser.quit()


class CameronCrawler:
    def __init__(self):
        global KEYWORD
        self.post_count = 0
        # self.page = page
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.KEYWORD = KEYWORD
        self.browser = webdriver.Chrome(executable_path="/Users/eoorim/Documents/seleniumpro/chromedriver 2",
                                        options=self.chrome_options)
        self.URL = f"https://cafe.naver.com/scottycameron"

    def wait_for(self, locator):
        return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located(locator))


    def extract_data(self):
        post_text_list = []
        self.browser.switch_to.frame("cafe_main")
        title = self.browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/div[1]/div[1]/div/h3")
        article = self.browser.find_element(By.CLASS_NAME, "article_viewer")
        comments = self.browser.find_elements(By.CSS_SELECTOR, "span.text_comment")
        post_text_list.append(title.text)
        post_text_list.append(article.text)
        # print(title.text)
        # print(article.text)
        for comment in comments:
            # print(comment.text)
            post_text_list.append(comment.text)

        return post_text_list

    def crawling_start(self):
        global total_text_list
        self.browser.get(self.URL)

        cookies = pickle.load(open("naver_cookies.pkl", "rb"))
        for cookie in cookies:
            self.browser.add_cookie(cookie)

        self.browser.refresh()

        volvik_ball = "%BA%BC%BA%F2+%B0%F8"
        srixon_ball = "%BD%BA%B8%AF%BD%BC+%B0%F8"
        title_ball = "%C5%B8%C0%CC%C6%B2%B8%AE%BD%BA%C6%AE+%B0%F8"
        callaway_ball = "%C4%B6%B7%AF%BF%FE%C0%CC+%B0%F8"

        if self.KEYWORD == "볼빅 공":
            self.browser.get(
                f"https://cafe.naver.com/scottycameron?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=13018047%26search.searchBy=1%26userDisplay=50%26search.query={volvik_ball}")
        elif self.KEYWORD == "스릭슨 공":
            self.browser.get(
                f"https://cafe.naver.com/scottycameron?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=13018047%26search.searchBy=1%26userDisplay=50%26search.query={srixon_ball}")
        elif self.KEYWORD == "타이틀리스트 공":
            self.browser.get(
                f"https://cafe.naver.com/scottycameron?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=13018047%26search.searchBy=1%26userDisplay=50%26search.query={title_ball}")
        elif self.KEYWORD == "캘러웨이 공":
            self.browser.get(
                f"https://cafe.naver.com/scottycameron?iframe_url=/ArticleSearchList.nhn%3Fsearch.clubid=13018047%26search.searchBy=1%26userDisplay=50%26search.query={callaway_ball}")
        else:
            pass


        self.browser.switch_to.frame("cafe_main")
        # self.wait_for((By.CLASS_NAME,"td_article"))
        posts = self.browser.find_elements(By.CLASS_NAME, "article")
        for post in posts:
            # print(post.text)

            if "월례회" in post.text or "경매" in post.text or "완료" in post.text or "이벤트" in post.text:
                pass
            else:
                try:
                    ActionChains(self.browser).key_down(Keys.COMMAND).click(post).perform()
                except:
                    pass

        switch_count = 0
        for window in self.browser.window_handles:
            self.browser.switch_to.window(window)
            if switch_count > 0:
                self.wait_for((By.CLASS_NAME, "title_text"))
                time.sleep(1)
                try:
                    total_text_list = total_text_list + self.extract_data()
                except:
                    print("Connection Refused")
                self.browser.close()
            time.sleep(.5)
            switch_count += 1

        self.browser.quit()

KEYWORD = input("검색어: ")
total_text_list = []


for i in range(1,11):
    DealbadaCrawler(i).crawling_start()


GolfzoneMarketCrawler().crawling_start()
CameronCrawler().crawling_start()
print(total_text_list)

eliminate_stopwords(total_text_list)

word_count = Counter(word_list).most_common()


# 파일 생성
words_file = open(f'/Users/eoorim/Desktop/Coding/Python/M.Oasis/golf-crawling-moasis/result/{KEYWORD}_Words.txt', 'w')
for word in word_list:
    words_file.write(word)
    words_file.write(', ')


csv_file = open(f'/Users/eoorim/Desktop/Coding/Python/M.Oasis/golf-crawling-moasis/result/{KEYWORD}_Count.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(["Word", "Count", "Label"])
for w in word_count:
    if int(w[1]) > 19:
        wd = str(w[0])
        # 비싼 넣을까 말까
        if ("문제" in wd) or ("비싸" in wd) or ("전범기업" in wd) or ("비싼" in wd) or ("불량률" in wd) or ("이상하게" in wd) \
                or ("오차" in wd) or ("일제" in wd) or ("일본" in wd) or ("중국" in wd) or ("최악" in wd)\
                or ("싸구려" in wd):
            writer.writerow([w[0],w[1],"부정"])
        elif ("가성비" in wd) or ("저렴" in wd) or ("싸게" in wd) or ("잘샀" in wd) or ("덕분" in wd) or ("이쁘" in wd) \
                or ("좋" in wd) or ("추천" in wd) or ("써볼까" in wd) or ("추천" in wd) or ("최고" in wd) or ("1위" in wd) \
                or ("손맛" in wd) or ("선호" in wd) or ("부럽습니다" in wd) or ("정타" in wd) or ("메리트" in wd) \
                or ("선물" in wd) or ("프리미엄" in wd) or ("만족" in wd) or ("맘에들어요" in wd) or ("재구매" in wd) \
                or ("애용" in wd) or ("예쁘" in wd) or ("강력" in wd) or ("부담없이" in wd) or ("감사" in wd) \
                or ("인기" in wd) or ("고맙습니다" in wd) or ("감사" in wd) or ("득템" in wd) or ("깨끗" in wd) \
                or ("믿고" in wd) or ("A급" in wd) or ("깔끔" in wd) or ("멀리" in wd) or ("효과" in wd) or ("도움" in wd) \
                or ("괜찮습니다" in wd):
            writer.writerow([w[0],w[1],"긍정"])
        elif ("볼빅" in wd) or ("마그마" in wd):
            writer.writerow([w[0],w[1],"볼빅"])
        elif ("타이틀" in wd) or ("Pro" in wd) or ("v1" in wd) or ("V1" in wd) or ("소프트필" in wd) or ("프로브이원" in wd):
            #if "볼빅" in KEYWORD:
                #writer.writerow([w[0], w[1], "경쟁브랜드"])
            #else:
                writer.writerow([w[0], w[1], "타이틀리스트"])
        elif ("브릿지스톤" in wd) or ("브리지스톤" in wd) or ("파이즈" in wd) or ("e6" in wd) or ("E6" in wd) \
                or ("XS" in wd) or ("투어B" in wd):
            #if "볼빅" in KEYWORD:
                #writer.writerow([w[0], w[1], "경쟁브랜드"])
            #else:
                writer.writerow([w[0],w[1],"브릿지스톤"])

        elif ("캘러웨이" in wd) or ("크롬소프트" in wd) or ("트루비스" in wd) or ("에픽" in wd) or ("트리플" in wd):
            #if "볼빅" in KEYWORD:
                #writer.writerow([w[0], w[1], "경쟁브랜드"])
            #else:
                writer.writerow([w[0],w[1],"캘러웨이"])

        elif ("스릭슨" in wd) or ("XV" in wd) or ("xv" in wd) or ("TRISPEED" in wd) or ("지스타" in wd) or ("Srixon" in wd) \
            or ("던롭" in wd) or ("DDH" in wd) or ("ddh" in wd):
            #if "볼빅" in KEYWORD:
                #writer.writerow([w[0], w[1], "경쟁브랜드"])
            #else:
                writer.writerow([w[0], w[1], "스릭슨"])
        elif ("커클랜드" in wd) or ("미즈노" in wd) or ("DDH" in wd) or ("스넬" in wd) \
                or ("빅야드" in wd) or ("TP5" in wd) or ("테일러메이드" in wd) or ("윌슨" in wd) or ("나이키" in wd) \
                or ("낫소" in wd) or ("Snell" in wd) or ("MTB" in wd) or ("세인트나인" in wd) or ("마루망" in wd) \
                or ("락바텀" in wd) or ("PXG" in wd) or ("star" in wd) or ("젝시오" in wd) or ("아쿠쉬네트" in wd) \
                or ("다이아윙스" in wd) or ("텔메" in wd) or ("RZN" in wd) or ("스텔스" in wd) or ("ERC" in wd) \
                or ("GBB" in wd) or ("아이오노머" in wd) or ("코브라" in wd) or ("라이언" in wd) or ("커크랜드" in wd) \
                or ("넥센" in wd) or ("혼마" in wd):
            #if "볼빅" in KEYWORD:
                #writer.writerow([w[0], w[1], "경쟁브랜드"])
            #else:
                writer.writerow([w[0],w[1],"기타 경쟁 브랜드"])
        elif ("비비드" in wd) or ("형광" in wd) or ("칼라" in wd) or ("컬러" in wd) or ("주황" in wd) or ("색깔" in wd)\
                or ("연두" in wd) or ("핑크" in wd) or ("빨강" in wd) or ("노란" in wd) or ("보라" in wd):
            if "볼빅" in KEYWORD:
                writer.writerow([w[0],w[1],"강점"])

        else:
            writer.writerow([w[0],w[1],"중립"])
    else:
        pass


print(f"검색된 단어: {len(word_list)}개")
