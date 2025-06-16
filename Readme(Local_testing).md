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
