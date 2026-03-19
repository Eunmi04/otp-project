import hmac
import hashlib
import struct
import base64

def generate_hotp(secret, counter):
    key = base64.b32decode(secret)
    msg = struct.pack(">Q", counter)

    h = hmac.new(key, msg, hashlib.sha1).digest()
    o = h[-1] & 0x0F
    code = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 1000000

    return str(code).zfill(6)

# 👉 이거 추가
secret = "JBSWY3DPEHPK3PXP"

for i in range(1, 4):
    print(f"counter={i} → OTP={generate_hotp(secret, i)}")