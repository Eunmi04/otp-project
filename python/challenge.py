import hmac
import hashlib
import os

def challenge_response(secret, challenge):
    return hmac.new(secret.encode(), challenge, hashlib.sha256).hexdigest()

secret = "mysecret"

# 랜덤 challenge 생성
challenge = os.urandom(16)

response = challenge_response(secret, challenge)

print("Challenge:", challenge.hex())
print("Response :", response)