import streamlit as st
from PIL import Image
from utils.ocr_utils import extract_text_from_image
from utils.drug_api import search_drug_info_by_name
from utils.gpt_utils import generate_gpt_guidance

st.set_page_config(page_title="약사봇", page_icon="💊")
st.title("💊 약사봇 - 사진으로 약 성분 분석하기")

uploaded_file = st.file_uploader("약 성분이 적힌 사진을 올려주세요", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 이미지", use_column_width=True)

    with st.spinner("🔍 텍스트 인식 중..."):
        text = extract_text_from_image(image)
        st.write("🔤 인식된 텍스트:", text)

    with st.spinner("💊 약 성분 분석 중..."):
        api_key = st.secrets["DRUG_API_KEY"]
        drug_info = search_drug_info_by_name(text.strip(), api_key)

        if "error" in drug_info:
            st.error("약 정보를 찾을 수 없습니다.")
        else:
            st.subheader("📋 의약품 기본 정보")
            st.write("**효능**:", drug_info["efcyQesitm"])
            st.write("**복용법**:", drug_info["useMethodQesitm"])

            with st.spinner("🤖 AI 설명 생성 중..."):
                ai_text = generate_gpt_guidance(drug_info)
                st.subheader("👩‍⚕️ 복용 안내 (AI 요약)")
                st.write(ai_text)
