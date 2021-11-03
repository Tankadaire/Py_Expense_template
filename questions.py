def prettyfi(s):
    pretty = ""
    for l in s:
        if l == '\n':
            return pretty
        
        pretty = pretty + l

def list_users():
    list_user = []
    with open("users", 'r') as f:
        
        myline = f.readline()
        
        while myline:
            list_user.append(prettyfi(myline))
            myline = f.readline()

    return list_user

expense = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message": "Spender",
        "choices":list_users(),
    },

]



user = [
    {
        "type":"input",
        "name":"name",
        "message":"name",
    },

]


person = [
    {
        "type":"input",
        "name":"person",
        "message":"person that need to pay",
    },
    {
        "type":"input",
        "name":"someone_else",
        "message":"is there someone else?",
    },
]

