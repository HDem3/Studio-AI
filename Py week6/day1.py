import hashlib
import bcrypt
import os, time


pwd="my_secure_password"

def hash_password_sha256(password):
    return hashlib.sha256(password.encode()).hexdigest()

def hash_password_bcrypt(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=11)).decode()

def hash_password_pbkdf2(password, iterations=300_000):
    return hashlib.pbkdf2_hmac("sha256", password.encode(), os.urandom(16), iterations).hex()


print("SHA-256 Hash:", hash_password_sha256(pwd))
print("bcrypt Hash:", hash_password_bcrypt(pwd))
print("PBKDF2 Hash:", hash_password_pbkdf2(pwd))


#
#
#pwd = b"password123"
#salt = os.urandom(16)
#
#for iterations in [300_000]:
#    start = time.time()
#    hashlib.pbkdf2_hmac("sha256", pwd, salt, iterations)
#    elapsed = (time.time() - start) * 1000
#    print(f"{iterations} iterazioni: {elapsed:.2f} ms")
#
#
#
#
#for cost in range(11, 12):
#    start = time.time()
#    bcrypt.hashpw(pwd, bcrypt.gensalt(rounds=cost))
#    elapsed = (time.time() - start) * 1000
#    print(f"Cost {cost}: {elapsed:.2f} ms")
#
#