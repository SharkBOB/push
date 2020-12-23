import pandas as pd
import numpy as np
import math


# Fund Investment

def investment(y1, y2, y3):
    year1 = y1 - 2020
    year2 = y2 - 2020
    year3 = y3 - 2020
    # Calculate compound interest on annual investment
    year2020 = round(30000 * pow(1.04, year1 * 12), -2)
    year2021 = round(30000 * pow(1.04, year2 * 12), -2)
    year2022 = round(30000 * pow(1.04, year3 * 12), -2)
    profitability = year2020 + year2021 + year2022 - (32000 * 3)
    return profitability


Profit = investment(2023, 2022, 2021)
print(Profit)

import jieba
from wordcloud import WordCloud
import matplotlib.pyplot as plt
df=pd.read_excel('wordcloud.xlsx')
s=str(df)
print(s)
mytext=" ".join(jieba.cut(s))
print(mytext)

wordclound=WordCloud(font_path='simsun.ttf',background_color='white').generate(mytext)
# word_list=jieba.cut(s,cut_all=True)
# word_space_list=" ".join(word_list)
# my_wordcolud=WordCloud().generate(word_space_list)

plt.imshow(wordclound,interpolation='bilinear')
plt.axis('off')
plt.show()

if __name__ == '__main__':
    investment(2023, 2022, 2021)