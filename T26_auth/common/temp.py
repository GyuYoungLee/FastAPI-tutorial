import base64
from datetime import datetime, timedelta

import bcrypt
from jose import jwt

# 패스워드 암호화
pw = bcrypt.hashpw("1234".encode("UTF-8"), bcrypt.gensalt())
print(pw)

ok = bcrypt.checkpw("1234".encode("UTF-8"), pw)
print(ok)

# Basic 토큰 생성
data = "gy:1234"

basic = base64.b64encode(data.encode("UTF-8"))
print(basic)  # Z3k6MTIzNA==

data = base64.b64decode(basic)
print(data)

# Bearer 토큰 생성
payload = {
    "user_id": "gy",
    "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
}

token = jwt.encode(payload, "secret", "HS256")
print(token)

data = jwt.decode(token, "secret", "HS256")
print(data)
