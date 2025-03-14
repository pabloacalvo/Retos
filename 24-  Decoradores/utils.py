import os
import csv
import re

def get_users(file_name: str) -> list:
    with open(f"{os.path.dirname(__file__)}/{file_name}", 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)
    return data


def is_authenticated(username:str, password:str) -> bool:
    user = {
        "username":username,
        "password":password
    }
    all_users = get_users("users.csv")
    if user in all_users:
        return True
    else:
        return False

def is_valid_password(pwd: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z0-9@#$%^&+=]{8,}", pwd))


