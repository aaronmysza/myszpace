
def user_prompt(msg):
    user_input = input(f'{msg}: ')
    return user_input.lower() in ['yes', 'y']
