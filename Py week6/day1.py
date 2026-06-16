import bcrypt

def hash_password(password: str) -> bytes:
    salt= bcrypt.gensalt(11)
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)

pwd= "my_secure_password"

hashed_pwd= hash_password(pwd)
hashed_pwd_str= hashed_pwd.decode()
print(f"Hashed password: {hashed_pwd_str}")
is_valid= verify_password(pwd, hashed_pwd)
print(f"Password valid: {is_valid}")