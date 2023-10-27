import hashlib
import random
import streamlit as st


def generate_sha256_hash(name, birthday, id_number):
    user_info = f"{name}{birthday}{id_number}"
    sha256_hash = hashlib.sha256(user_info.encode()).hexdigest()
    return sha256_hash


def generate_random_sha256():
    data = str(random.getrandbits(256)).encode('utf-8')
    sha256_hash = hashlib.sha256(data).hexdigest()
    return sha256_hash


def check_hash_in_sample(hash_to_check, sample_hashes):
    return hash_to_check in sample_hashes
