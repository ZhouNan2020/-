import streamlit as st
import numpy as np
import time

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

# 页面顶端居中显示大标题
st.markdown("<h1 style='text-align:center;'>他妈的我们吃什么！</h1>", unsafe_allow_html=True)

# 初始化按钮点击计数器
if 'click_count' not in st.session_state:
    st.session_state.click_count = 0

# 使用三列布局将按钮放置在屏幕中间，按钮加粗加大
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    button_clicked = st.button("<strong><span style='font-size:20px;'>开始</span></strong>", key="start_button", unsafe_allow_html=True)

#当按钮被点击时执行逻辑
if button_clicked:
    st.session_state.click_count += 1
    if st.session_state.click_count > 3:
        st.markdown("<p style='text-align:center;font-size:18px;'><strong>吃个锤子吃，你特么就是不饿</strong></p>", unsafe_allow_html=True)
    else:
        # 延时3秒并显示自定义spinner
        with st.spinner("爸爸帮你想~爸爸帮你挑~"):
            time.sleep(3)
        # 随机选择一个餐厅
        num_restaurants = len(restaurant_mapping)
        random_number = np.random.randint(1, num_restaurants + 1)
        selected_restaurant = restaurant_mapping[random_number]
        # 将结果输出在“开始”按钮下，结果加粗加大并置中显示
        st.markdown(f"<p style='text-align:center;font-size:24px;'><strong>{selected_restaurant}</strong></p>", unsafe_allow_html=True)
        st.balloons()
