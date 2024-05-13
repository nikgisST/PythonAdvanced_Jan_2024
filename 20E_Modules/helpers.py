from hashlib import sha256
from canvas import frame


def clean_screen():
    frame.delete("all")


def get_password_hash(password):
    hash_object = sha256(password.encode())          # UTF-8 encoding от string в bytes
    return hash_object.hexdigest()             # type("hello".encode())  - class 'bytes'