correct_username = 'fabio'
correct_password = '1234'

attempts = 0
max_attempts = 3

while attempts < max_attempts:

    username = input('Enter your username: ')
    password = input('Enter your password: ')

    if username == correct_username and password == correct_password:
        print('Login successful!')
        break

    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts

        print('Invalid username or password.')
        print(f'Remaining attempts: {remaining_attempts}')

if attempts == max_attempts:
    print('Access blocked.')

