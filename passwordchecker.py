def passwordchecker():
    from getpass import getpass
    username = input("Enter your username:")
    password = getpass("Enter your password:")

    password_length = len(password)
    password_string = "*" * password_length

    print(
        f"{username} - your password {password_string} is {password_length} characters long"
    )
