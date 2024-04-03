import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


# plt.rcParams['font.sans-serif'] = ['SimHei']  
# # Matplotlib中设置字体-黑体，解决Matplotlib中文乱码问题
# plt.rcParams['axes.unicode_minus'] = False   
def convert_wan_to_number(wan_str):
    if pd.notna(wan_str):  
        num_str = wan_str.replace("万", "")
        return float(num_str) * 10000
    else:
        return np.nan  
df=pd.read_excel('./data2.xlsx')
df['人气'] = df['人气'].apply(convert_wan_to_number)
type_popularity = df.groupby('类型')['人气'].mean()
type_counts = df['类型'].value_counts()
print(type_counts)
print(type_popularity)

font = FontProperties(fname='/Users/lilcookie/Library/Fonts/SimHei.ttf ', size=14)
plt.figure(figsize=(12,6))
type_counts.plot(kind='bar')
plt.title('the distribution of novel type')
plt.xlabel('the novel type')
plt.ylabel('numble')
plt.show()

plt.figure(figsize=(12, 6))
type_popularity.plot(kind='bar', color='orange')
plt.title('average popularity of fiction genre')
plt.xlabel('the novel type',)
plt.ylabel('average popularity')
plt.show()