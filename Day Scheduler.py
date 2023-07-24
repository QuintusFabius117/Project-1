import random

Studies = ['Security+', 'Python', 'HTB']
Hobbies = ['Japanese', 'Driving', 'Fiction Book', 'Non-Fiction Book', 'Journal', 'Drawing']
Other = ['Excersise', 'Maths', 'Physics', 'Story']



SecPlus = 'Security+'


def weekday():
    
    Hobi = True
    while Hobi == True: 
        Train_Journey_Hobby = (random.choices(Hobbies, weights=(70, 70, 20, 30, 15, 10), k=1))

        if Train_Journey_Hobby == ['Drawing']: 
            pass
        elif Train_Journey_Hobby ==['Journal']:
            pass
        else: 
            global day
            day = SecPlus, 'and', *Train_Journey_Hobby
            break
            Hobi == False
        
        
    


def week():

    weekday()
    Monday = 'On Monday this week you will do', *day , 'on the train.\n'
    print (*Monday)

    weekday()
    Tuesday = 'On Tuesday this week you will do', *day , 'on the train.\n'
    print (*Tuesday)

    weekday()
    Wednesday = 'On Wednesday this week you will do', *day , 'on the train.\n'
    print (*Wednesday)

    weekday()
    Thursday = 'On Thursday this week you will do', *day , 'on the train.\n'
    print (*Thursday)

    weekday()
    Friday = 'On Friday this week you will do', *day , 'on the train.\n'
    print (*Friday)





def weekend_day():
    
    global Day_Hobby
    global Day_Study
    global Third_Topic

    Day_Hobby = (random.choices(Hobbies, weights=(70, 70, 20, 30, 15, 10), k=1))
    Day_Study = (random.choices(Studies, weights=(50, 40, 20), k=1))

    
    Third_Topic = Day_Hobby or Day_Study

    


def weekend(): #trying to figure out how to have a 3 part combination of hobby/study without doubling

    global Saturday
    global Sunday

    Third = True
    while Third == True:
        weekend_day()
        if Third_Topic == Day_Hobby:
            pass
        else:
            print(Third_Topic)
            break
            Third = False






    weekend_day()
    Saturday = ('On Saturday you will do', str(*Day_Study)+ ',', str(*Day_Hobby), 'and', str(*Third_Topic)+'.\n')

    weekend_day()
    Sunday = ('On Saturday you will do', str(*Day_Study)+ ',', str(*Day_Hobby), 'and', str(*Third_Topic)+'.\n')

    print (*Saturday)
    print (*Sunday)

#week()
#weekend()