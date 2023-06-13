from sys import argv

script, user_name = argv
prompt = '> '

print(f'Hi {user_name}, I am the {script} script')
print(f'Do you like me, {user_name}?')
likes_you = input(prompt)

print(f'Where do you live {user_name}?')
lives = input(prompt)

print(f'''
Alright, so you said {likes_you} about liking me. \
You live in {lives}.
''')
