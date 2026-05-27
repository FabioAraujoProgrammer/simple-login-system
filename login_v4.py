print('=== REGISTER ===')

registered_username = input('Create your username: ')
registered_password = input('Create your password: ')

file = open('users.txt', 'w')

file.write(f'{registered_username}\n')
file.write(f'{registered_password}')

file.close()

print('\nUser successfully registered!')

print('\n=== LOGIN ===')

username = input('Enter your username: ')
password = input('Enter your password: ')

file = open('users.txt', 'r')

saved_username = file.readline().strip()
saved_password = file.readline().strip()

file.close()

if username == saved_username and password == saved_password:
    print('Login successful!')
else:
    print('Invalid username or password.')
    