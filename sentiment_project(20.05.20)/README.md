# 비정형 데이터를 활용한 일반인의 IoT Security Sentiment 분석

### 팀원
- 소민형
- 유나은
- 박경덕

### 프로젝트 목적
- 감성분석을 통해 IoT Security에 대한 일반 사용자의 보안 sentiment를 분석 및 보안의식을 파악한다.

- 차후에 보안 사고가 발생했을 때 보안의식이 어떻게 변화하는지 분석할 기준점을 생성한다

### 프로젝트 개요
- IMDB에서 영화리뷰를 크롤링해와서, 감성사전 구축을 위한 데이터를 수집한다.
- EDA를 통해 수집한 비정형 데이터의 형태를 파악하고, 최적화된 분석의 방향성을 찾는다.
- tensorflow와 scikit-learn을 사용한 감성사전을 구축한다.
- twitter와 quora에서 일반인들의 iot security에 관한 데이터를 크롤링해온다.
- Google docs로 설문지를 만들고, 해외 각종 커뮤니티에 올려 IoT Security에 관한 데이터를 추가 수집한다.
- 구축한 감성사전으로 iot security관련 데이터를 분석하여, 일반인의 보안 sentiment를 알아본다.


### 사용한 오픈 소스
- Python 3.7
- string / os / csv / datetime / time
- re / collections
- selenium 3.141.0
- beautifulsoup4 4.8.2
- GetOldTweets3
- plotly 2.2.3
- seaborn 0.9.0
- matplotlib 3.1.1
- pandas 0.25.1 
- numpy 1.18.1
- sklearn 0.21.3
- nltk 3.4.5
- tensorflow 2.1.0 
- keras 2.2.4

## 코드 및 파일설명
### 0. data 폴더에는 
	크롤링한 데이터인 quora와 twit의 csv파일
	딥러닝모델(h5)
	데이터 분석 결과인 sentiment_result.csv파일이 있습니다. 


### 1. EDA 
- 수집한 데이터의 EDA를 진행하는 코드입니다. (Exploratory data analysis)
- 영화리뷰를 먼저 분석해서, 딥러닝 모델링의 방향성을 정합니다.
- 트위터와 Quora의 데이터를 분석해서 결과값을 예측해봅니다.


### 2. keras_py366
- 수집된 데이터의 클렌징, 토큰화, lemmantization을 진행한뒤, ngram을 통해 데이터를 재가공합니다.
- BoW(Bag of Word)를 체크하기 위해, tfidf를 이용하여 희소행렬을 생성합니다.
- 전처리된 데이터를 tensorflow를 활용하여 감성분석 기초 모델을 만듭니다.    


### 3. movie_crawler
- imdb에서 영화에서 좋은 리뷰, 나쁜 리뷰를 크롤링해옵니다.
- 현재 세팅된 것으로는 각각 12500개씩을 가져오도록 해놨으나, 수정가능합니다.
- 목적 : 감성사전 구축을 위한 긍부정 표현 수집
- 선정이유 : 평점 데이터가 있기 때문에, 각각의 평점을 이용해 리뷰에 포함된 단어들의 긍부정 정도를 파악하기 용이.
- py37에 최적화되어있습니다    


### 4. quora_crawler
- iot security를 키워드로 한 질문과 대답(Q&A)들을 크롤링해옵니다. 약 400개 정도의 글을 가져옵니다    


### 5. sentiment_result
- model_py에서 생성한 h5모델을 불러오고, quora와 twitter에서 크롤링한 데이터를 가져와서 감성을 분석합니다. 
- 분석 결과를 간단하게 분석합니다.
- 결과 값을 csv파일로 저장합니다.


### 6. tweet_crawler
- iot security를 키워드로 한 트윗들을 크롤링해옵니다. 5월과 6월간의 모든 트윗으로 대략 12000개정도입니다    


## 결과
