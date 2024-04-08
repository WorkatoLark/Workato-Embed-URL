import base64
import time
import uuid

import jwt
import requests

API_TOKEN = 'wrkaus-eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJmY2VhMzY0Ni0zZjFjLTQ3YjgtYTYwZS04NGVjMWVjNGU2OGYiLCJqdGkiOiIwYTMwMmM0MC03NDI2LTQ1ODAtOGMzOC0zNWFlMTM1NDNmZDUifQ.f4kd_M_Z_u6Ul7j_soIjV2MaMKIP8O-Q14PAgSoveDvLeWfag6kKqJgLU5ui7agS66Kp8EhCGepBj2GcyKi0myzcodc9FWPkkobfyiuZQpm4jK9SGSyj28Usnozg-7vNO86hifyxmri2vG6PpAJwFl2f99NuUZl-ZHd5gdCQSCOdmLke7MsdwKpcWe3s6FF7y2IuNPGeP8YkvN8R1w8yvJIH64tUVv7KNTFlb5N9fJd_BHv5vb-70ylHGW8tq7n1XAI9kuri_mRNvpyuMgmkCaXT3JsJ4w0E_-NEVR7Sb0ubbh4Xn7DNdlBq59tkdoUu2de-PEk3OapEirsi9OpjP94fiyg_ggCGeiXzv6cvwxvoRif4qjgVcraVvGiAGWFqj62jt-9aChucfGUFRjd6py9v8DY5D3NVyUkoAwPLJp-OFePrL5HB0uP8t3Mred8q5DBWtBckn8bjCExevq_Tz1ko6rK90KaZN0Vkkga7nhrwTTTZu227ZeKKVEdNa33KAVnfKPxry77Hw8sMCJNO41WUGbrQBfdrX6IbrGaLaxznfKkXd4BtRohsKrO_aSdcZJUKJCQWoLvGMrx57pbNnvN7hvRHouVMYWR1BLL9Ze7uK_kBwRnRahf6OP3zfgwsXHqrCsoRVJA_LF2Mubr4990Hlj7lzhYkud-gu8wPYq8'


def generate_vendor_id():
    url = 'https://www.workato.com/api/account/signature_verification_key'
    headers = {
        'Authorization': API_TOKEN,
        'Content-Type': 'application/json'
    }

    data = {
        'key': """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2Gd0lsobf1XGoc060pTY
/68HZPsMITIGsl9VHEUNorMCciY4O2cISSXgCAZNvlzB1rPjfWxk2he4lk3WJh0j
kTHU5lgACH4Jqeb+yuANpTNByrIvDRxQYbR7ad1iaO0wBsTB/hdS93xcm3B4+SVe
Ehz1CqCVMS5B4ZVwcVpoukF3IGBy6tdMBQmoXTN3mBm0VOpMHpdNvNpS3LeyEyJh
Mmm4UzGQodPrl6cu2fdKITETJLS+lr7ODRIUZ/8hNAyxsjgb1WDkhzqi4nc3Rz8W
HNTrYyB1ujUqn3QUqHhcdYVFr8LqSeZITMVgMCfIMbnnTBxHIzbIjFLfBxJ6Z8vq
mwIDAQAB
-----END PUBLIC KEY-----"""
    }

    response = requests.put(url, headers=headers, json=data)

    print(response.status_code)
    print("generate_vendor_id response: {}".format(response.text))
    if response.status_code != 200:
        print("generate_vendor_id failed")
        return None

    return response.json()['vendor_id']


def base64url_encode(input):
    return base64.urlsafe_b64encode(input).rstrip(b'=')


def generate_jwt(user_id, connection_id):
    vendor_id = generate_vendor_id()
    print("vendor_id: {}".format(vendor_id))

    private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA2Gd0lsobf1XGoc060pTY/68HZPsMITIGsl9VHEUNorMCciY4
O2cISSXgCAZNvlzB1rPjfWxk2he4lk3WJh0jkTHU5lgACH4Jqeb+yuANpTNByrIv
DRxQYbR7ad1iaO0wBsTB/hdS93xcm3B4+SVeEhz1CqCVMS5B4ZVwcVpoukF3IGBy
6tdMBQmoXTN3mBm0VOpMHpdNvNpS3LeyEyJhMmm4UzGQodPrl6cu2fdKITETJLS+
lr7ODRIUZ/8hNAyxsjgb1WDkhzqi4nc3Rz8WHNTrYyB1ujUqn3QUqHhcdYVFr8Lq
SeZITMVgMCfIMbnnTBxHIzbIjFLfBxJ6Z8vqmwIDAQABAoIBAGKDJhYGx2G+IIBD
twVp8Sbj/M/BYRIzfczxjQMjhEOOjgx8zZhtHN5/uW6tv/Jqs2sT1PmhwH9v0P3L
TTNojGpqbuq1IL688ZVArLiaKlwL62Vkm/qx6v2vdYcJ2uS9JOHP7CfJYmF7YYT5
PHjew+Ym/H3sAD61OhSBPQC9EXPHxnqEa3mggVpMef+jC/xNQuq0JzPNKWLTTi7i
VjwV5AORbzN+zReSS96s/EZrXhv90JodEsYxV3KOa+QY4XMewJ3swjj4ElcfCvMc
XjbI0rBYRoil3YvxG1TQTO1nw4xx7fOfMkG182oQpc5zSFinvwVZmk70SG6DPcZ3
0kZczVECgYEA/2KSXzYTcUfIcLU11r7dAN84UJcqSq+8bqSrWaHCdQwU96xB2UDp
s6Y0lOTtFFVsmVnaOg4CgGHIWRBUbN/AGE2LLDm3fd2cS/qWGXjmLolbDydnViFf
EWZeJ+E1dA6+I8X5ctTroFZT+CXyoQmC4mzgYzhy7YaMEXS7w5cU7a0CgYEA2Oza
vgjtBEw/NPpf7vCIKtp+U6voh/fY+piYVybxkoTp3QMlUv88djtFB3QXKaJFdRue
diiyto/UnfURD2xXRqa4BWfZJo28dSBHQEYcAKOiTX37EuqN7EcBwyEuruiB0DGD
Qmtz4E3dIYwylstESanfgx7looltHScQmj1WsmcCgYEAvq22Y+hYM+hIu/5QqHnx
QMlpnqJ/LSxxIJtKZK3mJsZSkWnH8JIK69tYvyL98ISnhQgVa+sx6vEXSYhrwK5/
GqYrF2YwnoVsQT5j+7jNBEoB9xqQiTp5ZOBtxJDd/D1VshgK27YmB5ztLQYIVjxn
wO9RykNHbBldU1s5JhwTwDECgYBV8KBIoWilRz/TUU4ob4rCz4U0yOp606pWvZW9
EWSrU5UDRnfHBe+CN8EFTuzORceWubZxwXXr9deaLLjxj06UYwCMw7O4HncHQB56
TExTxIBMixipSduoPAlqsP65tMuZG8SQz9k8iByPaeew7h7DwFUYsWjwl9lur0dY
k+yBCQKBgGVGNFtE41+2D7Koj7P2OlqzM83VYGLeVbEb7feCEb+DDtqVYpur3+b6
nMKke2/92pW07AiO9kAUqx9ZNTSQmiTDzCu9tw83h8MMuXwR11A6kMEWO/aPuLdV
8X+6+NNrNe6tVFKqwAWkDt6uTGpc3LegmsakMDxg6dm+1D76avTO
-----END RSA PRIVATE KEY-----
    """
    payload = {
        "sub": "{}:{}".format(vendor_id, user_id),
        "jti": "{}".format(uuid.uuid4()),
        "iat": int(time.time())
    }

    token = jwt.encode(payload, private_key, algorithm="RS256")

    print(f"https://www.workato.com/direct_link/embedded/connections/{connection_id}?workato_dl_token=" + token)
    return f"https://www.workato.com/direct_link/embedded/connections/{connection_id}?workato_dl_token=" + token


def generate_token(user_id):
    vendor_id = generate_vendor_id()
    print("vendor_id: {}".format(vendor_id))

    private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA2Gd0lsobf1XGoc060pTY/68HZPsMITIGsl9VHEUNorMCciY4
O2cISSXgCAZNvlzB1rPjfWxk2he4lk3WJh0jkTHU5lgACH4Jqeb+yuANpTNByrIv
DRxQYbR7ad1iaO0wBsTB/hdS93xcm3B4+SVeEhz1CqCVMS5B4ZVwcVpoukF3IGBy
6tdMBQmoXTN3mBm0VOpMHpdNvNpS3LeyEyJhMmm4UzGQodPrl6cu2fdKITETJLS+
lr7ODRIUZ/8hNAyxsjgb1WDkhzqi4nc3Rz8WHNTrYyB1ujUqn3QUqHhcdYVFr8Lq
SeZITMVgMCfIMbnnTBxHIzbIjFLfBxJ6Z8vqmwIDAQABAoIBAGKDJhYGx2G+IIBD
twVp8Sbj/M/BYRIzfczxjQMjhEOOjgx8zZhtHN5/uW6tv/Jqs2sT1PmhwH9v0P3L
TTNojGpqbuq1IL688ZVArLiaKlwL62Vkm/qx6v2vdYcJ2uS9JOHP7CfJYmF7YYT5
PHjew+Ym/H3sAD61OhSBPQC9EXPHxnqEa3mggVpMef+jC/xNQuq0JzPNKWLTTi7i
VjwV5AORbzN+zReSS96s/EZrXhv90JodEsYxV3KOa+QY4XMewJ3swjj4ElcfCvMc
XjbI0rBYRoil3YvxG1TQTO1nw4xx7fOfMkG182oQpc5zSFinvwVZmk70SG6DPcZ3
0kZczVECgYEA/2KSXzYTcUfIcLU11r7dAN84UJcqSq+8bqSrWaHCdQwU96xB2UDp
s6Y0lOTtFFVsmVnaOg4CgGHIWRBUbN/AGE2LLDm3fd2cS/qWGXjmLolbDydnViFf
EWZeJ+E1dA6+I8X5ctTroFZT+CXyoQmC4mzgYzhy7YaMEXS7w5cU7a0CgYEA2Oza
vgjtBEw/NPpf7vCIKtp+U6voh/fY+piYVybxkoTp3QMlUv88djtFB3QXKaJFdRue
diiyto/UnfURD2xXRqa4BWfZJo28dSBHQEYcAKOiTX37EuqN7EcBwyEuruiB0DGD
Qmtz4E3dIYwylstESanfgx7looltHScQmj1WsmcCgYEAvq22Y+hYM+hIu/5QqHnx
QMlpnqJ/LSxxIJtKZK3mJsZSkWnH8JIK69tYvyL98ISnhQgVa+sx6vEXSYhrwK5/
GqYrF2YwnoVsQT5j+7jNBEoB9xqQiTp5ZOBtxJDd/D1VshgK27YmB5ztLQYIVjxn
wO9RykNHbBldU1s5JhwTwDECgYBV8KBIoWilRz/TUU4ob4rCz4U0yOp606pWvZW9
EWSrU5UDRnfHBe+CN8EFTuzORceWubZxwXXr9deaLLjxj06UYwCMw7O4HncHQB56
TExTxIBMixipSduoPAlqsP65tMuZG8SQz9k8iByPaeew7h7DwFUYsWjwl9lur0dY
k+yBCQKBgGVGNFtE41+2D7Koj7P2OlqzM83VYGLeVbEb7feCEb+DDtqVYpur3+b6
nMKke2/92pW07AiO9kAUqx9ZNTSQmiTDzCu9tw83h8MMuXwR11A6kMEWO/aPuLdV
8X+6+NNrNe6tVFKqwAWkDt6uTGpc3LegmsakMDxg6dm+1D76avTO
-----END RSA PRIVATE KEY-----
    """
    payload = {
        "sub": "{}:{}".format(vendor_id, user_id),
        "jti": "{}".format(uuid.uuid4()),
        "iat": int(time.time())
    }

    token = jwt.encode(payload, private_key, algorithm="RS256")
    return token


def generate_fully_embedded_url(user_id, path):
    token = generate_token(user_id)
    return f"https://app.workato.com/direct_link?workato_dl_path={path}&workato_dl_token={token}"

if __name__ == '__main__':
    # print(generate_jwt("3461928", "13509024"))
    print(generate_fully_embedded_url("3667343", "recipes/46234834"))


    