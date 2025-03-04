import streamlit as st
import numpy as np


# 吃饭备选餐厅映射
restaurant_mapping = {
    1: '妈子面',
    2: '碗碗',
    3: '麻辣诱惑',
    4: 'B记',
    5: '杂饭之家',
    6: '邱太食堂',
    7: '机车面',
    8: 'KFC',
    9: '唐记',
    10: '卤肉饭',
    11: '随机小吃',
    12: 'fruit楼上那家'
}


if st.button('开始'):
    num_restaurants = len(restaurant_mapping)
    random_number = np.random.randint(1, num_restaurants + 1)
    selected_restaurant = restaurant_mapping[random_number]
    st.markdown(f"**<span style='font-size:24px;'>{selected_restaurant}</span>**", unsafe_allow_html=True)
