# IoT Security 감성분석 project코드입니다

## 0. data 폴더에는 
		크롤링한 데이터인 quora와 twit의 csv파일
		딥러닝모델(h5)
		데이터 분석 결과인 sentiment_result.csv파일이 있습니다. 


## 1. EDA 
- 수집한 데이터의 EDA를 진행하는 코드입니다. (Exploratory data analysis)    


## 2. keras_py366
- 수집된 데이터의 클렌징, 토큰화, lemmantization을 진행한뒤, ngram을 통해 데이터를 재가공합니다.
BoW(Bag of Word)를 체크하기 위해, tfidf를 이용하여 희소행렬을 생성합니다.
전처리된 데이터를 tensorflow를 활용하여 감성분석 기초 모델을 만듭니다.    


## 3. movie_crawler
- imdb에서 영화에서 좋은 리뷰, 나쁜 리뷰를 크롤링해옵니다.
현재 세팅된 것으로는 각각 12500개씩을 가져오도록 해놨으나, 수정가능합니다.
py37에 최적화되어있습니다    



## 4. quora_crawler
- iot security를 키워드로 한 질문과 대답(Q&A)들을 크롤링해옵니다. 약 400개 정도의 글을 가져옵니다    


## 5. sentiment_result
- model_py에서 생성한 h5모델을 불러오고, quora와 twitter에서 크롤링한 데이터를 가져와서 감성을 분석합니다.    


## 6. tweet_crawler
- iot security를 키워드로 한 트윗들을 크롤링해옵니다. 5월과 6월간의 모든 트윗으로 대략 12000개정도입니다    