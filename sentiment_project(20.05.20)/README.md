#IoT Security 감성분석 project코드입니다

#진행 중

1. data_crawler는 imdb에서 영화에서 좋은 리뷰, 나쁜 리뷰를 크롤링해옵니다.
현재 세팅된 것으로는 각각 12500개씩을 가져오도록 해놨으나, 수정가능합니다.
py37에 최적화되어있습니다


2. model_py는 수집된 데이터의 클렌징, 토큰화, lemmantization을 진행한뒤, ngram을 통해 데이터를 재가공합니다.
BoW(Bag of Word)를 체크하기 위해, tfidf를 이용하여 희소행렬을 생성합니다.
전처리된 데이터를 tensorflow를 활용하여 감성분석 기초 모델을 만듭니다.


3. tweet_crawler는 iot security를 키워드로 한 트윗들을 크롤링해옵니다. 5월과 6월간의 모든 트윗으로 대략 12000개정도입니다


4. quora_crawler는 iot security를 키워드로 한 질문과 대답(Q&A)들을 크롤링해옵니다. 약 400개 정도의 글을 가져옵니다.


5. result는 model_py에서 생성한 h5파일을 사용하여, 글의 감성을 분석하여 사용자의 인식을 조사합니다.
