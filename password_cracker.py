# password_cracker.py

import hashlib

def crack_sha1_hash(hash_to_crack, use_salts=False):
    # Load passwords from common-passwords.txt
    with open("common-passwords.txt", "r") as file:
        passwords = [line.strip() for line in file]

    # Load salts from samplesalts.txt if needed
    salts = []
    if use_salts:
        with open("samplesalts.txt", "r") as file:
            salts = [line.strip() for line in file]

    # Function to compute SHA-1 hash
    def sha1_hash(text):
        return hashlib.sha1(text.encode()).hexdigest()

    # Attempt to match the hash
    for password in passwords:
        # If no salts are used
        if not use_salts:
            generated_hash = sha1_hash(password)
            print(f"Checking password '{password}' with hash '{generated_hash}'")  # Debug statement
            if generated_hash == hash_to_crack:
                return password
        # If salts are used, try salt+password and password+salt
        else:
            for salt in salts:
                generated_hash_with_prefix = sha1_hash(salt + password)
                generated_hash_with_suffix = sha1_hash(password + salt)
                print(f"Checking salt+password '{salt + password}' with hash '{generated_hash_with_prefix}'")  # Debug statement
                print(f"Checking password+salt '{password + salt}' with hash '{generated_hash_with_suffix}'")  # Debug statement
                
                if generated_hash_with_prefix == hash_to_crack or generated_hash_with_suffix == hash_to_crack:
                    return password

    # If no match is found
    return "PASSWORD NOT IN DATABASE"
