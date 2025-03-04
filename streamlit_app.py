import streamlit as st
import numpy as np
import time

# 自定义 CSS 样式，实现按钮和结果文本居中、加粗和加大
st.markdown(
    """
    <style>
    .center-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .center-button button {
        font-size: 24px;
        font-weight: bold;
        padding: 10px 20px;
    }
    .result-text {
        font-size: 24px;
        font-weight: bold;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

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

# 初始化点击次数，存储在 session_state 中
if "click_count" not in st.session_state:
    st.session_state.click_count = 0

# 居中显示“开始”按钮
with st.container():
    st.markdown("<div class='center-container'>", unsafe_allow_html=True)
    button_clicked = st.button("开始")
    st.markdown("</div>", unsafe_allow_html=True)

# 判断点击次数
if button_clicked:
    st.session_state.click_count += 1

if st.session_state.click_count > 3:
    # 超过3次点击则显示提示文本，不允许再执行
    st.markdown("<div class='center-container'><span class='result-text'>吃个锤子吃，你特么就是不饿</span></div>", unsafe_allow_html=True)
elif button_clicked:
    # 点击后显示 spinner，延时3秒后出现结果，并触发气球特效
    with st.spinner("爸爸帮你想~爸爸帮你挑~"):
        time.sleep(3)
    num_restaurants = len(restaurant_mapping)
    random_number = np.random.randint(1, num_restaurants + 1)
    selected_restaurant = restaurant_mapping[random_number]
    st.markdown(f"<div class='center-container'><span class='result-text'>{selected_restaurant}</span></div>", unsafe_allow_html=True)
    st.balloons()
