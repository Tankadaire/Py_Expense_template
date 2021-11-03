from PyInquirer import prompt
import json

from questions import expense, person




def new_expense(*args):
    infos = prompt(expense)

   #list_benificiaire = []

    #while len(list_benificiaire) == 0 or benificiaire['someone_else']:
        #benificiaire = prompt(person)
        #list_benificiaire.append(benificiaire['person'])
    
    try:
        with open(infos['spender'] + '.json', 'r') as json_file:
            data = json.load(json_file)
            print('exist')
    except:
        data = {"name": infos['spender'], "solde": 0, "expenses" : []}

    with open(infos['spender'] + '.json', 'w') as json_file:
        data['expenses'].append(infos)
        data['solde'] += int(infos['amount'])
        json.dump(data, json_file, indent=4)
        print('test')

    print("Expense Added !")
    print(infos)
    return True


