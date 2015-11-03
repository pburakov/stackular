import random
from passlib.apps import custom_app_context as pwd


def encrypt(password):
    return pwd.encrypt(password, rounds=535000, salt_size=16)


def verify(password, hash):
    return pwd.verify(password, hash)


def random_alnum_string(length):
    return ''.join([random.choice('0123456789abcdefghijklmnopqrstuvwxyz')
                    for x in range(length)])
