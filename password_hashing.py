import hashlib

def hash_password(password):
    sha_signature = hashlib.sha256(password.encode()).hexdigest()
    return sha_signature

def verify_password(stored_hash, input_password):
    return stored_hash == hash_password(input_password)
