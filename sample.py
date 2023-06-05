import requests

url = "<login url>"
base_url = "<base url>"
session_id = "<session id>"

headers = {
    "Host": base_url,
    "Connection": "keep-alive",
    "Content-Length": "1611",
    "sec-ch-ua": "\"Chronium\";v=\"112\",\"Google Chrome\";v=\"112\",\"Not:A-Brand\";v=\"9g\"",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua-mobile": "",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "sec-ch-ua-platform": "\"Windows\"",
    "Origin": base_url,
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": f"{base_url}/DentalstudiosF/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US, en: g=0.9",
    "Cookie": f"JSESSIONID={session_id}"
}

data = {
    "userName": "user name",
    "password": "password",
    "customerId": "cust id",
    "practice": {
        "id": 1,
        "name": "practice name",
        "name2": "practice name?",
        "address": "address",
        "zipCode": {
            "id": "<zipcor",
            "state": "«state›",
            "city": "«city›",
            "zipClass": "STANDARD",
            "zipCode": "<zipcode 2›",
            "updaterime": "<update time›",
            "createTime": "<create time›"
        },
        "phone": "phone number",
        "fax": "‹fax>"
    }
}

response = requests.post(url, json=data, headers=headers)

if response.ok:
    print(response.text)
else:
    print(f"Error: {response.status_code}")
