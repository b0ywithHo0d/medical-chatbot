import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_gpt_guidance(drug_info: dict) -> str:
    summary = f"""
    효능: {drug_info.get('efcyQesitm', '')}
    복용법: {drug_info.get('useMethodQesitm', '')}
    주의사항: {drug_info.get('atpnQesitm', '')}
    부작용: {drug_info.get('seQesitm', '')}
    병용금기: {drug_info.get('intrcQesitm', '')}
    """
    messages = [
        {"role": "system", "content": "너는 약사야. 약 정보를 쉽게 설명해줘."},
        {"role": "user", "content": f"다음 약 정보를 바탕으로 복용 주의사항을 사용자에게 친절하게 설명해줘:\n\n{summary}"}
    ]
    response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
    return response.choices[0].message.content
