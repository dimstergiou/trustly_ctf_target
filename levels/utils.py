def valid_credentials(username, password):
    USERNAMES = ["Cisco", "admin", "none", "root"]
    PASSWORDS = ["Cisco", "admin", "none", "password", "changeme"]

    if username in USERNAMES and password in PASSWORDS:
        return True
    else:
        return False