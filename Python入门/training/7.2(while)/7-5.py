prompt = 'How old are you,kid?'
prompt +="\n(You can input the 'quit' to end)"
active = True
while active:
    age=input(prompt)
    
    if age == 'quit':
        active = False
        break
    if int(age) < 3:
        print('You are free.')
        continue
    elif int(age) <=12:
        print('You need to pay $10')
        continue
    else:
        print('You need to pay $15')
        continue
    


