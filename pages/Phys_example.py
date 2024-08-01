import textwrap
import google.generativeai as genai
import streamlit as st

def to_markdown(text):
    text = text.replace('•', '*')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

api_key = "AIzaSyAggXWyYB0W5QHO-sheWLHrrl5Zh3ZoyFg"

# 콘텐츠 생성 함수
def try_generate_content(api_key, prompt):
    genai.configure(api_key=api_key)
   
    model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                                  generation_config={
                                      "temperature": 0.9,
                                      "top_p": 1,
                                      "top_k": 1,
                                      "max_output_tokens": 2048,
                                  },
                                  safety_settings=[
                                      {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                                      {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                                      {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                                      {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
                                  ])
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"API 호출 실패: {e}")
        return None

# Streamlit 애플리케이션 인터페이스
st.title("🔬 물리학 원리와 일상 사례")
st.write("물리학 원리를 입력하면 해당 원리의 개념과 일상 생활에서의 적용 사례를 알려드립니다.")

principle = st.text_input("물리학 원리를 입력하세요")

if principle:
    prompt = f"'{principle}' 원리의 개념과 일상 생활에서의 적용 사례를 설명해줘."
    result = try_generate_content(api_key, prompt)
    if result:
        st.markdown(to_markdown(result))
    else:
        st.error("정보를 가져오지 못했습니다. 나중에 다시 시도해주세요.")
