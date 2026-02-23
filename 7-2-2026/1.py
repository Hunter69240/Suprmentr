
# REGISTER
print("=== REGISTER ===")

username = input("Create username: ")
password = input("Create password: ")

# Simple manual hashing (basic transformation)
hashed_password = ""

for ch in password:
    # convert character to ASCII number and shift it
    num = ord(ch) + 5
    hashed_password = hashed_password + str(num)

# Store credentials
stored_username = username
stored_password = hashed_password

print("Account created successfully!\n")



# LOGIN


print("=== LOGIN ===")

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    login_username = input("Enter username: ")
    login_password = input("Enter password: ")

    # Apply same transformation
    login_hash = ""
    for ch in login_password:
        num = ord(ch) + 5
        login_hash = login_hash + str(num)

    if login_username == stored_username and login_hash == stored_password:
        print("Login Successful ✅")
        break
    else:
        attempts = attempts + 1
        print("Incorrect credentials ❌")
        print("Attempts left:", max_attempts - attempts)

        if attempts == max_attempts:
            print("Too many failed attempts. Account blocked.")
