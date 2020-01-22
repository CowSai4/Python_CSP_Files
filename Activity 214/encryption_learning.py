from passlib.hash import pbkdf2_sha256

hash = pbkdf2_sha256.using(salt_size=8).hash('yummy')

print(hash)

print(pbkdf2_sha256.using(salt_size=8).verify('yummy',hash))
print(pbkdf2_sha256.using(salt_size=8).verify('incorrect',hash))