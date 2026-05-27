print('=== REGISTER ===')

registered_username = input('Create your username: ')
registered_password = input('Create your password: ')

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    print('\n=== LOGIN ===')

    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == registered_username and password == registered_password:
        print('Login successful!')
        break

    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts

        print('Invalid username or password.')
        print(f'Remaining attempts: {remaining_attempts}')

if attempts == max_attempts:
    print('Access blocked.')
    