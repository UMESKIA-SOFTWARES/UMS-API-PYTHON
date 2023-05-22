import requests
import json

url = "https://api.umeskiasoftwares.com/api/v1/smsbalance"
api_key = "XXXXXXXXXXXXXXX="  # Replace with your API key
email = "example@gmail.com"  # Replace with your email

payload = {
    "api_key": api_key,
    "email": email
}

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers)
    data = response.json()
    success = data["success"]

    if success == "200":
        credit_balance = data["creditBalance"]
        print("Sms Balance retrieved successfully, with creditBalance:", credit_balance)
    else:
        result_code = data["ResultCode"]
        error_message = data["errorMessage"]
        print("Sms not sent, with ResultCode:", result_code, "and errorMessage:", error_message)

except requests.exceptions.RequestException as e:
    print("An error occurred:", str(e))
