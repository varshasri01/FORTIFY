import hashlib
import requests
def hash_password(password):
    password_bytes = password.encode("utf-8")
    hash_object = hashlib.sha1(password_bytes)
    hash_string = hash_object.hexdigest()
    return hash_string.upper()
def get_api_data(prefix):
    response= requests.get("https://api.pwnedpasswords.com/range/"+prefix)
    return response.text
def get_password_leaks_count(response, suffix):
    for line in response.splitlines():
        hash_suffix, count = line.split(":")
        if hash_suffix==suffix:
            return int(count)
    return 0
def check_password(password):
    hashed_password= hash_password(password)
    prefix=hashed_password[:5]
    suffix=hashed_password[5:]
    response= get_api_data(prefix)
    return get_password_leaks_count(response, suffix)