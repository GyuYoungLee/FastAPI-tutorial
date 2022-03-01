import base64
from datetime import datetime, timedelta

import bcrypt
import jwt

# 암호화
pw = bcrypt.hashpw("1234".encode("UTF-8"), bcrypt.gensalt())
print(pw)

ok = bcrypt.checkpw("1234".encode("UTF-8"), pw)
print(ok)

# 인증 토큰
payload = {
    "user_id": "gy",
    "exp": datetime.utcnow() + timedelta(seconds=60 * 60 * 24)
}

token = jwt.encode(payload, "secret", "HS256")
print(token)

data = jwt.decode(token, "secret", "HS256")
print(data)

# base64 인코딩
data = "gy:1234"

basic = base64.b64encode(data.encode("UTF-8")).decode("UTF-8")
print(basic)  # Z3k6MTIzNA==

plain = base64.b64decode(basic).decode("UTF-8")
print(plain)
