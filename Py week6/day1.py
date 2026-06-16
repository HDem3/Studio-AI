import hashlib

pwd = "ciao123"
hashed = hashlib.sha256(pwd.encode()).hexdigest()

print(hashed)