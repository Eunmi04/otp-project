import time
import hmac
import hashlib
import struct
import base64

def generate_totp(secret, interval=30):
    key = base64.b32decode(secret)
    counter = int(time.time()) // interval
    msg = struct.pack(">Q", counter)

    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[-1] & 0x0F
    code = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000

    return str(code).zfill(6)

secret = "JBSWY3DPEHPK3PXP"

# 👉 한 번만 실행
otp = generate_totp(secret)
print("OTP:", otp)