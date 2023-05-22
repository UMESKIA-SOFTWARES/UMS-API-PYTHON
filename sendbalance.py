import requests
import json

url = "https://api.umeskiasoftwares.com/api/v1/sms"
api_key = "XXXXXXXXXXXXXXXXXX="  # Replace with your API key
email = "example@gmail.com"  # Replace with your email
sender_id = "23107"  # If you have a custom sender id, use it here OR Use the default sender id: 23107
message = "UMS SMS Api Test Message"
phone_number = "0768XXXXX60"  # Phone number should be in the format: 0768XXXXX60 OR 254768XXXXX60 OR 254168XXXXX60

payload = {
    "api_key": api_key,
    "email": email,
    "Sender_Id": sender_id,
    "message": message,
    "phone": phone_number
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
        request_id = data["request_id"]
        message = data["message"]
        print("Sms sent successfully, with request_id:", request_id, "and message:", message)
    else:
        result_code = data["ResultCode"]
        error_message = data["errorMessage"]
        print("Sms not sent, with ResultCode:", result_code, "and errorMessage:", error_message)

except requests.exceptions.RequestException as e:
    print("An error occurred:", str(e))
