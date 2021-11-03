from PyInquirer import prompt
from questions import user

def add_user():
    
    infos = prompt(user())

    with open('users' , 'a') as f:
        print("est")
        f.write(infos['name'] + "\n")