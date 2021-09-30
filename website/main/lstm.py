# -*- coding: utf-8 -*-
"""광화문_LSTM for django.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Lj34NE655tyQ_MQ1_16cF0jSvGSd8wow

### 종로구- 광화문사거리 LSTM model django 업로드
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
from datetime import datetime
import seaborn as sns
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.layers import LSTM

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

# # google colab용
# from google.colab import drive
# drive.mount('/content/drive')

# 저장한 예측값 불러오기


def model_load2():

    #test_gwang_feature = np.load('/content/drive/MyDrive/DS_project/test_gwang_feature.npy')
    test_gwang_feature = np.load(
        'C:/Users/cityo/Desktop/Git_Space/finalPJT/website/main/test_gwang_feature.npy')

    # 저장한 모델 로드하고 예측
    reconstructed_model = tf.keras.models.load_model(
        'C:/Users/cityo/Desktop/Git_Space/finalPJT/website/main/gwang_checkpoint.h5')
    pred = reconstructed_model.predict(test_gwang_feature)

    # minmaxscaling 복원
    max = 3056.0
    min = 98.0
    pred_values = np.round((pred*(max-min)+min)).astype(int).tolist()
    recent = pred_values[-1]

    print('광화문사거리 현재 예측교통량은 ', recent, '입니다')
