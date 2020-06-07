import subprocess

user_profile = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
user_profile = [i.split(':')[1][1:-1] for i in user_profile if 'All User Profile' in i]

for i in user_profile:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [key_content.split(':')[1][1:-1] for key_content in results if 'Key Content' in key_content]
    try:
        print(f'{i} | {results[0]}')
    except IndexError:
        print(f'{i} | {""}')