# To check the verification code from authetication app

import pyotp

shared_key = "Enter your secret key" # Generate the secret key from the Autheticator App
totp = pyotp.TOTP(shared_key)

otp = totp.now()
print(f"Generated OTP: {otp}")