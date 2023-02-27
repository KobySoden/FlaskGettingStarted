import requests

url = "http://127.0.0.1:5000/login"

payload='username=koby&password=pass'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)