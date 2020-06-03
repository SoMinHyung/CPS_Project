#!/usr/bin/env python
# coding: utf-8

# In[34]:


from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
import csv

"""
이 크롤러 클래스의 목적


해외 영화 리뷰 사이트인 IMDB에서 

1. 영화를 리뷰많은 순으로 정렬 (num개) #내가 설정한 num은 250
2. 각 영화마다 평점10점 리뷰 50개, 평점 1점 리뷰 50개씩을 크롤링
3. 긍정표현 12500개, 부정표현 12500개를 수집

"""

class Scraper():    
    
    def __init__(self):
        print("크롤링 시작")
        
        
        
    def make_csv(self):
        #처음에 실행할 때는 w로 실행하여, 기존의 데이터가 있으면 초기화
        file = open("review.csv", "w", newline = "", encoding  = 'UTF-8')
        wr = csv.writer(file)
        wr.writerow(["review","sentiment"])
        file.close()
   


    #CSV파일로 저장합니다. UTF-8을 사용하면, 한글이 깨지기때문에, euc-kr형식으로 저장합니다.
    def write_csv(self, review, sentiment):
        #파일은 데이터 추가, newline 시 공백 추가
        file = open("review.csv", "a", newline="", encoding  = 'UTF-8')

        wr = csv.writer(file)

        for i in range(len(review)):
            wr.writerow([review[i], sentiment[i]])

        file.close()
        
    

    def find_review_page(self,driver, num, title):
        """
        num번째 영화의 리뷰페이지로 이동하는 함수입니다.
        """
        #해당 영화 페이지로 이동
        print(title)
        driver.find_element_by_link_text(title).click()
        time.sleep(3)

        #영화 페이지에서 리뷰페이지로 이동
        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser") 
        move = bs.find("div", class_="user-comments").find_all('a')
        driver.find_element_by_link_text(move[-1].string).click()
        time.sleep(3)

        

    def review_scrap(self, driver, score):
        """
        페이지 이동을 모두 마친 후, 영화 리뷰 페이지에서 크롤링하는 함수입니다
        score = 1 이면 별점1점인 부정적인 리뷰
        score = 10 이면 별점10점임 긍정적인 리뷰
        """
        time.sleep(1)
        
        #별점 1점을 선택
        if score == 1:
            driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[1]/form/div/div[3]/select/option[2]').click()
            time.sleep(3)     
        elif score == 10:
            driver.find_element_by_xpath('//*[@id="main"]/section/div[2]/div[1]/form/div/div[3]/select/option[11]').click()
            time.sleep(3)

        #기본리뷰가 25개밖에 안되기 때문에 25개를 더 보기 누름
        driver.find_element_by_id("load-more-trigger").click()
        time.sleep(3)

        html = driver.page_source
        bs = BeautifulSoup(html, "html.parser") 
        reviews = bs.find("div", class_="lister-list").find_all("div", class_="text show-more__control clickable")
        reviews2 = bs.find("div", class_="lister-list").find_all("div", class_="text show-more__control")

        reviewList = []
        sentimentList = []

        for rev in reviews:
            reviewList.append(rev.text)
            if score == 1:
                sentimentList.append("negative")
            else:
                sentimentList.append("positive")

        for rev in reviews2:
            reviewList.append(rev.text)
            if score == 1:
                sentimentList.append("negative")
            else:
                sentimentList.append("positive")

        self.write_csv(reviewList, sentimentList)

        
        
    def scrap(self, num):
        path = os.getcwd()+"\chromedriver.exe"
        driver = webdriver.Chrome(path)
        
        try:
            self.make_csv()

            #평가가 많은 순으로 100개 정렬
            driver.get("https://www.imdb.com/chart/top/?sort=nv,desc&mode=simple&page=1")
            time.sleep(2)

            #검색할 검색어는 1~100위의 영화
            html = driver.page_source
            bs = BeautifulSoup(html, "html.parser")
            contents = bs.find("tbody", class_="lister-list").find_all("td", class_="titleColumn")

            title = []


            #전체 페이지에 250개의 영화가 있기때문에 num개만 추출하도록 설정
            count = 0
            for c in contents:
                if count > num-1 :
                    break
                count += 1

                title.append(c.find("a").text)


            count = 0
            for t in title:
                #n번째 영화의 리뷰페이지로 이동
                self.find_review_page(driver, count, t)

                #리뷰페이지에서 리뷰를 크롤링, csv파일에 저장
                self.review_scrap(driver, 1)
                self.review_scrap(driver, 10)

                #크롤링을 마친 후, 초기 페이지로 이동
                driver.get("https://www.imdb.com/chart/top/?sort=nv,desc&mode=simple&page=1")
                time.sleep(2)

                count += 1
                print(str(count) + "번 째 데이터 크롤링 완료")

            time.sleep(5)
            print("크롤링 종료")


        finally:
            time.sleep(3)
            driver.quit()


# In[37]:


s = Scraper()
s.scrap(11)


# In[ ]:




