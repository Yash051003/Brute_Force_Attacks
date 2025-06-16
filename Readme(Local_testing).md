# 🔐 BruteForce Login Tester (Educational Purpose Only)

This Python script attempts to brute-force login credentials against a Django-based login page hosted locally or on a LAN. It's intended **only for ethical and educational use** on applications you own or have permission to test.

---

## ⚠️ DISCLAIMER

> **This tool is strictly for testing your own web application's login security. Unauthorized use against systems without consent is illegal and unethical.**

---

## 🚀 Features

- Iterates through a list of passwords against a specified username.
- Detects successful login by checking for redirection or response content.
- Supports CSRF token handling via BeautifulSoup (if enabled).
- Works with both `localhost` and LAN-hosted Django apps.

---

## 🛠️ Requirements

- Python 3.8+
- `requests`
- `beautifulsoup4` (if CSRF parsing is required)

Install dependencies using:

```bash
pip install requests beautifulsoup4
```

---

##🧪 How to Use
1. Start your Django app
Ensure your target Django app is running:

```bash
python manage.py runserver 0.0.0.0:8000
```

2. Edit the script
Modify the following variables in brute_force.py:

```bash
url = "http://<YOUR-IP>:8000/accounts/login/"
username = "admin"
passwords = ["Yash", "admin", "password", "admin123", "letmein", "qwerty"]
```

3. Run the script in Kali Linux or terminal:

```bash
python brute_force.py
```

## 📷 Screenshot

![BruteForce Demo](assets/Code.png)
