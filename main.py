# main.py

from password_cracker import crack_sha1_hash

# Test without salts
print(crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"))  # Expected: "password"
print(crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec"))  # Expected: "sammy123"

# Test with salts
print(crack_sha1_hash("53d8b3dc9d39f0184144674e310185e41a87ffd5", use_salts=True))  # Expected: "superman"
print(crack_sha1_hash("ea3f62d498e3b98557f9f9cd0d905028b3b019e1", use_salts=True))  # Expected: "bubbles1"
