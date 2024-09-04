# MFA Bypass with Selenium and Python

This repository provides an example of how to bypass Multi-Factor Authentication (MFA) using Selenium with Python. It includes two key files:

1. `totp.py` - Checks the generation and verification of Time-based One-Time Passwords (TOTP) from an authenticator app.
2. `base.py` - Uses Selenium to automate the login process and bypass MFA.

## Requirements

Before running the scripts, ensure you have the following installed:

- Python 3.x
- Selenium
- `pyotp` (Python library for generating TOTP)
- WebDriver for your chosen browser

You can install the required Python packages using pip:

```bash
pip install selenium pyotp
```

## Files Overview

### `totp.py`

This file contains the logic for generating and verifying TOTP codes from an authenticator app, such as Microsoft Authenticator App. It uses the `pyotp` library to generate these codes based on a shared secret key.

### `base.py`

This file automates the login process using Selenium. It navigates to the login page, enters the user's credentials, and then bypasses the MFA by generating the correct TOTP code (Real-time code) using the logic from `totp.py`.

## Usage

1. **Update TOTP Secret Key**:
   
   In the `base.py` file, replace the placeholder with your TOTP secret key:

   ```python
   import pyotp

   # Replace 'YOUR_SECRET_KEY' with your actual secret key from the authenticator app
   shared_secret_key = "Enter your secret key here"
   totp = pyotp.TOTP(shared_secret_key)
   ```

2. **Run the Selenium Script**:
   
   Run the `base.py` script to automate the login process and bypass MFA:

   ```bash
   python base.py
   ```

   The script will open a browser window, navigate to the login page, enter the credentials, and automatically input the correct TOTP code to bypass MFA.

## Important Notes

- **Security Warning**: Bypassing MFA can be a security risk. This code is intended for educational purposes only. Do not use it for unauthorized access or in a production environment.
- **Legal Disclaimer**: Make sure you have explicit permission to test MFA bypass on any system. Unauthorized access to systems is illegal and unethical.

## Conclusion

This repository demonstrates how to bypass MFA using Selenium and Python. It leverages the `pyotp` library to generate the necessary TOTP codes automatically. Use this knowledge responsibly and ensure that you follow all legal and ethical guidelines.
