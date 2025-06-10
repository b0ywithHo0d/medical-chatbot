import requests

def search_drug_info_by_name(drug_name: str, api_key: str) -> dict:
    url = "https://apis.data.go.kr/1471000/DrbEasyDrugInfoService/getDrbEasyDrugList"
    params = {
        "serviceKey": api_key,
        "itemName": drug_name,
        "type": "json",
        "numOfRows": 1,
        "pageNo": 1
    }
    res = requests.get(url, params=params)
    data = res.json()

    if data.get("body") and data["body"].get("items"):
        return data["body"]["items"][0]
    else:
        return {"error": "정보 없음"}
