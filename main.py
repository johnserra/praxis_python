print('Enter your username:')
username = input()
print('Enter your passwoord:')
passwd = input()
passwd_length = len(passwd)
hidden_passwd = '*' * passwd_length
print(f'{username}, your password, {hidden_passwd}, is {passwd_length} characters long.')
