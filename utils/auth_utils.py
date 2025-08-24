import pandas as pd
import os
import hashlib

USER_FILE = "data/users.csv"


# Hash password
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


# Ensure CSV exists
def init_user_file():
    if not os.path.exists(USER_FILE):
        os.makedirs(os.path.dirname(USER_FILE), exist_ok=True)
        df = pd.DataFrame(columns=["username", "password"])
        df.to_csv(USER_FILE, index=False)


# Register
def register_user(username, password):
    init_user_file()
    df = pd.read_csv(USER_FILE)

    if username in df['username'].values:
        return False, "❌ Username already exists!"

    new_user = pd.DataFrame([[username, hash_password(password)]], columns=["username", "password"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_csv(USER_FILE, index=False)
    return True, "✅ Registration successful!"


# Login
def login_user(username, password):
    init_user_file()
    df = pd.read_csv(USER_FILE)

    hashed = hash_password(password)
    user = df[(df['username'] == username) & (df['password'] == hashed)]

    if not user.empty:
        return True, "✅ Login successful!"
    return False, "❌ Invalid username or password."
