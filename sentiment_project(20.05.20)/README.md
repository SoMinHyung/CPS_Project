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

<img src="https://user-images.githubusercontent.com/11614046/85217434-f813c680-b3cb-11ea-9b03-d729de0bf14a.PNG" width="50%"></img>


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
	크롤링한 데이터인 quora와 twit의 csv파일,
	설문조사 데이터인 survey result.csv파일,
	딥러닝모델(h5),
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

### IMDB 크롤링 결과

<img src="https://user-images.githubusercontent.com/11614046/85217468-7f613a00-b3cc-11ea-9a5c-31a4ac75ca62.PNG" width="70%"></img>

- 리뷰가 많은 영화들의 별점 10개와 1개인 리뷰를 각각 12500개씩 크롤링합니다.
- 별점 10점인 리뷰는 positive, 별점 1점인 리뷰는 negative로 저장하도록 합니다.
  
  
  
### EDA 결과(IMDB의 데이터 분석)

<img src="https://user-images.githubusercontent.com/11614046/85217609-a2401e00-b3cd-11ea-89c1-c217158a5098.PNG" width="25%"></img>

- 위는 불용어 삭제 전의 분석 결과.
- stopword의 사용이 굉장히 많기 때문에, 해당 단어들을 삭제해야할 필요가 있다.
- 따라서, nltk의 stopword를 가져와서 일치하면 삭제하도록 했다.
  
  

<img src="https://user-images.githubusercontent.com/11614046/85217538-10381580-b3cd-11ea-8d01-489ed6c9ef4e.png" width="70%"></img>

- 위는 불용어 삭제 후 분석 결과. (전체, 긍정, 부정 순)
  
- 알 수 있는 점
	1. 긍정과 부정에서 good, like 등의 단어가 동시에 상위권에 들어있는 것을 알 수 있다.
	- good과 not good이라는 단어가 있지만, 단어로 나누다보니 not과 good이 쪼개져서 나온 결과라고 할 수 있다.
	- 따라서, ngram을 이용해 단어를 2개씩 묶어서 분석하도록 하자.
	- 예를 들면, i don't like actor이면 i don't / don't like / like actor와 같은 식으로 나눈다.
	- 문맥상의 의미를 반영할 수 있다.  
  '
  
	2. film, movie, really와 같이 일반적으로 많이 사용되는 단어들은 삭제되지 않았다.
	- 많은 데이터에서 많이 쓰인 데이터의 가중치는 줄이고, 적은 데이터에서 많이 쓰인 데이터의 가중치는 높여준다.
	- tf-idf행렬을 이용한다.
	- <img src="https://user-images.githubusercontent.com/11614046/85217855-cf8dcb80-b3cf-11ea-9b2d-01614a7df148.PNG" width="100%"></img>

	
### 감성사전 구축 결과
- 딥러닝 모델 개요
<img src="https://user-images.githubusercontent.com/11614046/85217937-6eb2c300-b3d0-11ea-8fdb-b1db9224db2b.PNG" width="100%"></img>

- 위와 같이 특징을 추출하는데 효율적인 dense레이어를 2개넣었다.
- 과적합을 막기 위해 각 dense레이어에 dropout 20%를 설정하였다.
- 첫 dense레이어의 결과는 1 초과의 값이기 때문에, 활성화함수로는 정답률이 높은 relu함수를 사용한다.
- 두번째 dense레이어는 결과가 0 or 1의 값이 나오기 때문에, 활성화함수로 sigmoid를 사용한다.
- (값이 0이면 negative, 1이면 positive한 글을 작성한 것이다)
- 손실함수는 binary-crossentropy를 사용한다. (결과가 0 or 1이기 때문에)
- Callback을 사용하여, 정확도가 개선되지 않는다면 조기에 종료하도록 설정한다.
- 데이터가 너무 많기 때문에, batch학습을 활용한다.

<img src="https://user-images.githubusercontent.com/11614046/85218073-b6861a00-b3d1-11ea-9e63-b9775680f7d0.png" width="80%"></img>
- 테스트 결과 정확도가 93%의 모델이 생성되었음을 알 수 있다.


### 일반인의 IoT security관련 크롤링 결과

<img src="https://user-images.githubusercontent.com/11614046/85218190-b33f5e00-b3d2-11ea-9184-5d0116b193d0.PNG" width="80%"></img>
- 위와 같이 Quora에서 400개 (검색어 : iot security)

<img src="https://user-images.githubusercontent.com/11614046/85218203-e2ee6600-b3d2-11ea-9042-4a070bb9fdae.PNG" width="80%"></img>

- 위와 같이 트위터에서 13000개 (검색어 : iot security) (트윗날짜, 계정명, 내용을 수집)

<img src="https://user-images.githubusercontent.com/11614046/85218215-0d402380-b3d3-11ea-86bd-22dfd78091a5.PNG" width="80%"></img>
- 위와 같이 구글 survey를 이용하여, iot security에 대해 어떻기 생각하는지 질문하여 39개의 응답데이터를 수집.


### 구축한 모델로 iot security를 분석한 결과

<img src="https://user-images.githubusercontent.com/11614046/85218260-a2431c80-b3d3-11ea-877f-a9a4f8427d10.PNG" width="80%"></img>
- 위는 5월 1일 ~ 6월 10일까지의 데이터 분석 결과이다.
- 전체 평균 점수는 40.5점으로 약간 부정적으로 보고 있는 편이다.
- 설문조사는 33점, Quora는 45점, Twitter는 40점이다.

<img src="https://user-images.githubusercontent.com/11614046/85218347-68264a80-b3d4-11ea-9ccb-9d20cfc38281.PNG" width="80%"></img>
- 0.9점 이상의 긍정적인 데이터를 보면 중요하다, office upgrade를 위한 것이라고 생각해야 한다 등이 있다. 
- 0.1점 미만의 부정적인 데이터를 보시면 관련 표준이나 정책이 부족함을 비판하는 글, iot의 보안 취약성이 계속 문제가 되어 왔고 현재 여러 분야에서 iot 기술이 사용되고 있지만 여전히 최소한의 security protection만 하고 있다는 글, iot security 공격이 사업에 큰 악영향을 준다는 글이 있었다



### 해석
- 이러한 차이는 자료 출처의 특성에 따라서 발생한 것으로 보인다. 
- 설문조사는 IoT를 모르는 사람의 데이터도 포함되지만, Quora와 Twitter는 관련 분야에 관심이 있거나, 전문가인 사람이 글을 쓰는 경우가 많습니다.
- 그래서 설문조사의 경우 모른다, 어렵다 등의 답변이 많아서 부정적으로 나온 것으로 해석됩니다. 
- 그리고 Quora의 경우 해당 분야에 관심있다고 태그한 사람에게 직접적으로 답변을 요청하는 기능이 있어 이들이 설명문인 글이 많아 다른 자료에 비해 상대적으로 글이 길고, (iot security에 대한 부정적이고, 긍정적인 내용을 모두 포함한 경우가 많아 중간인 0.5점에 가까운 점수를 받은 것으로 보입니다). 
- 수집한 데이터를 확인한 결과 트위터는 IoT 보안 관련 제품 광고, 관련 뉴스, 포스팅 등의 자료 제목 등의 데이터가 많아 Quora의 데이터보다는 부정적으로 나온 것으로 보입니다. ex) 당신의 security가 위험합니다. 저희의 제품을 사용하세요!


