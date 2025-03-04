import streamlit as st
import numpy as np
import time

# 初始化按钮点击计数
if 'button_count' not in st.session_state:
    st.session_state.button_count = 0

# 屏幕顶端居中显示大标题
st.markdown("<h1 style='text-align: center;'>他妈的我们吃什么！</h1>", unsafe_allow_html=True)

# 向页面注入 CSS 调整按钮样式（大尺寸、加粗）
st.markdown("""
    <style>
    div.stButton > button {
        width: 300px;
        height: 80px;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

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

# 判断点击次数是否超过3次
if st.session_state.button_count >= 3:
    st.markdown("<h2 style='text-align: center;'>吃个锤子吃，你狗东西就是不饿</h2>", unsafe_allow_html=True)
else:
    # 利用 st.columns 居中放置按钮
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        button_clicked = st.button("开始")
    if button_clicked:
        st.session_state.button_count += 1
        with st.spinner("爸爸帮你想~~爸爸帮你挑~~"):
            time.sleep(3)
        num_restaurants = len(restaurant_mapping)
        random_number = np.random.randint(1, num_restaurants + 1)
        selected_restaurant = restaurant_mapping[random_number]
        # 输出结果置中，加粗加大
        st.markdown(f"<h2 style='text-align: center; font-weight: bold; font-size: 32px;'>{selected_restaurant}</h2>", unsafe_allow_html=True)
        st.balloons()
