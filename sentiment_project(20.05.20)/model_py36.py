#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import warnings
warnings.simplefilter('ignore')
sns.set(rc={'figure.figsize' : (12, 6)})
sns.set_style("darkgrid", {'axes.grid' : True})

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_csv('IMDB Dataset.csv')
data.head()


# In[3]:


from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
#one hot encoding
data['sentiment'] = label_encoder.fit_transform(data['sentiment'])
data.head()


# In[4]:


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

def ngram_vectorize(texts, labels):
    kwargs = {'ngram_range' : (1, 2),'dtype' : 'int32','strip_accents' : 'unicode',
              'decode_error' : 'replace','analyzer' : 'word','min_df' : 2}

    #tf-idf로 vectorize
    tfidf_vectorizer = TfidfVectorizer(**kwargs)
    transformed_texts = tfidf_vectorizer.fit_transform(texts)
    
    # selector를 이용하여, vector화된 값들을 최적화  
    selector = SelectKBest(f_classif, k=min(20000, transformed_texts.shape[1]))
    selector.fit(transformed_texts, labels)
    transformed_texts = selector.transform(transformed_texts).astype('float32')

    return transformed_texts

#벡터화
vect_data = ngram_vectorize(data['review'], data['sentiment'])
tfidf = TfidfVectorizer()
tr_texts = tfidf.fit_transform(data['review'])


# In[5]:


from sklearn.model_selection import train_test_split

# 데이터 분할 (학습, 테스트)
X = vect_data.toarray()
y = (np.array(data['sentiment']))

#학습 80%, 테스트 20%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=13)


# In[6]:


from tensorflow.python.keras import models
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.layers import Dropout

LEARNING_RATE = 1e-3
DROPOUT_RATE = 0.2
UNITS = 64

#sequence구축
model = keras.Sequential()
model.add(Dropout(rate= DROPOUT_RATE, input_shape = X_train.shape[1:]))
model.add(Dense(units=UNITS, activation='relu'))
model.add(Dropout(rate=DROPOUT_RATE))
model.add(Dense(units=1, activation='sigmoid'))
model.summary()

optimizer = tf.keras.optimizers.Adam(lr=LEARNING_RATE)
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['acc'])

#조기종료를 위한 콜백
callbacks = [tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=2)]


# In[7]:


#학습횟수, 학습배치사이즈
EPOCHS = 100
BATCH_SIZE = 128

#학습시작
history = model.fit(X_train, y_train, epochs=EPOCHS,
                    validation_data=(X_test, y_test), verbose=1,
                    batch_size=BATCH_SIZE, callbacks=callbacks)


# In[8]:


# 모델을 이용하여, test정확도 측정
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=1)
print('Test loss:', test_loss)
print('Test accuracy:', test_acc)


# In[9]:


#결과 그래프
def plot_history(history):
    accuracy = history.history['acc']
    val_accuracy = history.history['val_acc']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    
    epochs = range(1,len(accuracy) + 1)
    
    # Plot accuracy  
    plt.figure(1)
    plt.plot(epochs, accuracy, 'b', label='Training accuracy')
    plt.plot(epochs, val_accuracy, 'g', label='Validation accuracy')
    plt.title('Training and validation accuracy')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    
    # Plot loss
    plt.figure(2)
    plt.plot(epochs, loss, 'b', label='Training loss')
    plt.plot(epochs, val_loss, 'g', label='Validation loss')
    plt.title('Training and validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

plot_history(history)


# In[10]:


#모델저장
model.save('IMDB_model.h5')

