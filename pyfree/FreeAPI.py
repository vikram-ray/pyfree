import requests
import json


def get_bank_details(ifsc: str):
    url = 'https://ifsc.razorpay.com/{}'
    result = requests.get(url.format(ifsc))
    if result.status_code == 200:
        return json.loads(result.content)
    if result.status_code == 404:
        return {"status": "invalid IFSC code"}
    return result
    
