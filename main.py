import streamlit as st
from utlis import generate_script

st.title("🎬 视频脚本生成器")

with st.sidebar:
    openai_api_key = st.text_input("请输入OpenAI密钥：",type="password")
    st.markdown("[获取OpenAI密钥](https://platform.openai.com/account/api-keys)")

subject = st.text_input("💡 请输入视频的主题")
video_length = st.number_input("⏱️  请输入视频的大致时长(单位：分钟)",step=0.1)
creativity = st.slider("✨ 请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）", min_value=0.0,
                       max_value=1.0, value=0.2, step=0.1)

clicked = st.button("生成脚本")
if clicked and not openai_api_key:
    st.info("请输入你的OpenAI密钥")
    st.stop()
if clicked and not subject:
    st.info("请输入你的视频主题")
    st.stop()
if clicked and not video_length > 0.1:
    st.info("视频时长必须大于0.1")
    st.stop()
if clicked:
    with st.spinner("AI正在思考中，请稍等..."):
        title, script = generate_script(subject, video_length, creativity, openai_api_key)
    st.success("视频脚本已生成！")
    st.subheader("🔥 标题：")
    st.write(title)
    st.subheader("📝 视频脚本：")
    st.write(script)