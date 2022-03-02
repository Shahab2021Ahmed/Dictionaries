#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[ ]:



product_num = eval(input("Enter Number of products: "))
my_dict ={}
for x in range(product_num):
    productName = input("Enter Product Name: ")
    productPrice = int(input("Enter Product Price"))
    my_dict[productName] = productPrice


while True:
    productName = input("Enter Product name to get Price")
    if productName in my_dict:
        print("The price for your product is ", my_dict[productName])

    else:
        print("This product is not found in dictionary")
    


print(my_dict)


# # Question 2

# In[55]:



my_dict ={'Mercedez': '100','Ferrari':'200','Bugatti':'300'}
print(my_dict)

amt =eval(input("Enter Amount: $$"))
for key ,values in my_dict.items():
    if  int(values) < amt:
        print (key ,"->",values)


# # Question 3

# In[58]:


import operator

year ={"January":"31","Febuary":"28","March":"30","April":"30","May":"31","June":"30"}

#a
user_input= input("Enter Name of a month: ")
#user_input = "March"
for key, values in year.items():
     if user_input == key:  #change equality sign to in to answer d
        print( values)
        #break


#b
sorted_year ={key:year[key] for key in sorted(year)}
print(sorted_year.keys())

#c
for keys,values in year.items():
    if int(values) == 31:

        print(keys)


# # Question 4

# In[52]:


user_dict ={"Henry":"1234","Thomas":"Larissa","Monique":"Gaga"}
def CheckUser_Pass(x,y):
    for keys ,values in user_dict.items():
        if keys == x  and y == user_dict[keys]:
            return ("you are succesfully logged in",keys,user_dict[keys])
        else:
            return  ("Please do check your login details")



x = input("Enter Username: ")    
y = input("Enter Your Password ")
print(CheckUser_Pass(x,y))


# # Question 5

# In[51]:



def teamWIn():
    numberofTeams = int(input("Enter Number of Teams: "))
    team_dict={}
    score_list =[]
    winning_record =[]
    percentage_score = 0
    for team in range(numberofTeams):
        team_name = input("Enter Team Name: ")
        team_winning_score = int(input("Team Winning game: "))
        team_dict.update({team_name:team_winning_score})
        score_list.append(team_winning_score)
        winning_record.append(team_name)

    userinput = input("Enter team to check % of wins: ")
    for  keys,values in team_dict.items():

         if userinput == keys:
            score = team_dict[keys]
            percentage_score = (score/100)* 100

    return "Your teams list is {},Percentage win of team {}%, All team with winning record  {}".format(team_dict,percentage_score,winning_record)

print(teamWIn())


# # Question 6

# In[43]:


def teamInfo():
   num_team =int(input("Enter Number Of Teams: "))
   team_dict={}
   for team in range(num_team):
       key = input("Enter Team name: ")
       value =[]
       wins = int(input("Enter Win: "))
       losses = int(input("Enter Losses: "))
       value.extend((wins,losses))
       team_dict.update({key:value})
       
   return team_dict

print(teamInfo())


# # Question 7

# In[42]:


matrix_5= [1,2,3,4,5,
           5,6,7,4,5,
           6,7,8,0,3,
           4,2,1,5,6,
           7,8,9,0,5]

def creatList():
    matrix_dict={}
    for num in range(len(matrix_5)):
        key = matrix_5[num]
        value = matrix_5.count(key)
        matrix_dict.update({key:value})
    return matrix_dict



print(creatList())


# # Question 8

# In[41]:


import random

all_card ={"One":1,"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10}
cards = 3
player1Card =[]
player2Card =[]
for card in range(cards):
    c1 =random.choice(list(all_card.values()))
    c2= random.choice(list(all_card.values()))
    player1Card.append(c1)
    player2Card.append(c2)
print(player1Card,player2Card)

if sum(player1Card) > sum(player2Card):
    print("Player 1 wins with ",sum(player1Card)," Against Player 2 with",sum(player2Card))
elif sum(player2Card) > sum(player1Card):
    print("Player 2 wins with ",sum(player2Card)," Against Player 1 with",sum(player1Card))


# # Question 9

# In[40]:



from enum import Enum
from random import sample

class Cards(Enum):
    DECK = [{'value':i, 'suit':c} 
            for c in ['spades', 'clubs', 'hearts', 'diamonds'] 
            for i in range(2,15)]

def get_cards():
    rand_cards = sample(Cards.DECK.value, 3)
    return rand_cards

def flush(hand):
    if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit']:
        print('\nYou have a flush.')
    else:
        print('\nYou don\'t have a flush.')

def three_of_a_kind(hand):
    if hand[0]['value'] == hand[1]['value'] == hand[2]['value']:
        print('\nYou have a three-of-a-kind.')
    else:
        print('\nYou don\'t have a three-of-a-kind.')

def pair(hand):
    try:
        for i in range(3):
            if hand[i]['value'] == hand[i+1]['value']:
                print('\nYou have a pair.')
                break
            else:
                pass
    except IndexError:
        print('\nYou don\'t have a pair.')

def straight(hand):
    face_val = []
    for i in range(3):
        face_val.append(hand[i]['value'])
    face_val.sort(reverse = True)
    try:
        for i in range(3):
            if (face_val[i] - face_val[i+1] == 1) and (face_val[i+1] - face_val[i+2] == 1):
                print('\nYou have a straight.')
                break
            else:
                pass
    except IndexError:
        print('\nYou don\'t have a straight.')

def main():
    hand = get_cards()
    print('The following below is your hand.\n')
    print(hand)
    flush(hand)
    three_of_a_kind(hand)
    pair(hand)
    straight(hand)
    
if __name__ == '__main__':
    main()


# # Question 10

# In[39]:



# Note, chances to get a flush in 5-card is about 1 out of 509 hands.

from enum import Enum
from random import sample

class Cards(Enum):
    DECK = [{'value':i, 'suit':c} 
            for c in ['spades', 'clubs', 'hearts', 'diamonds'] 
            for i in range(2,15)]

def validate_num(message):
    valid = False
    while not valid:
        try:
            user_input = int(input(message))
            if user_input > 0:
                valid = True
            else:
                print('\nEnter a huge number for how many hands to play.')
        except ValueError:
            print('\nEnter a valid integer.')
    return user_input

def flush(COUNT, num):
    for i in range(num):
        hand = get_cards()
        if hand[0]['suit'] == hand[1]['suit'] == hand[2]['suit'] == hand[3]['suit'] == hand[4]['suit']:
            COUNT += 1
        else:
            pass
    return COUNT

def get_cards():
    rand_cards = sample(Cards.DECK.value, 5)
    return rand_cards

def main():
    COUNT = 0
    message = 'Enter the number of hands to play: '
    num = validate_num(message)
    prob = flush(COUNT, num)
    print(f'\n{prob} hand(s) had a flush.\n')
    print(f'The probability to get a flush from {num} hands is {round((prob/num)*100, 3)}%.')

if __name__ == '__main__':
    main()


# # Question 12

# In[35]:


from enum import Enum

class Music(Enum):
    KEY = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    CHORD_STEPS = {1:[4,7], 2:[3,7], 3:[4,8], 4:[4,6], 5:[4,7,9], 6:[3,7,9],
                   7:[4,7,10], 8:[3,7,10], 9:[4,7,11], 10:[3,6,10]}

def validate_key(message_key):
    valid = False
    while not valid:
        try:
            user_input = input(message_key).capitalize()
            if user_input in Music.KEY.value:
                valid = True
            else:
                print('\nPlease enter a valid key.')
        except:
            pass
    return user_input

def validate_chord(message_chord):
    valid = False
    while not valid:
        try:
            user_input = int(input(message_chord))
            if user_input in Music.CHORD_STEPS.value.keys():
                valid = True
            else:
                print('\nEnter a number from the given options.')
        except ValueError:
            print('\nInvalid. Enter an integer.')
    return user_input

def get_notes(user_key, user_chord):
    notes = []
    key_list_transform = []
    for i in range(len(Music.KEY.value)):
        if user_key == Music.KEY.value[i]:
            notes.append(Music.KEY.value[i])
            key_list_transform = Music.KEY.value[i:] + Music.KEY.value[:i]
    for j in range(len(key_list_transform)):
        if j in Music.CHORD_STEPS.value[user_chord]:
            notes.append(key_list_transform[j])            
    return notes

def main():
    print('The following below are the musical keys:')
    print(Music.KEY.value)
    message_key = 'Enter a musical key: '
    user_key = validate_key(message_key)
    print('\nEnter 1 for chord type Major.')
    print('Enter 2 for chord type Minor.')
    print('Enter 3 for chord type Augmented Fifth.')
    print('Enter 4 for chord type Minor Fifth.')
    print('Enter 5 for chord type Major Sixth.')
    print('Enter 6 for chord type Minor Sixth.')
    print('Enter 7 for chord type Dominant Seventh.')
    print('Enter 8 for chord type Minor Seventh.')
    print('Enter 9 for chord type Major Seventh.')
    print('Enter 10 for chord type Diminshed Seventh.')
    message_chord = 'Enter a chord type: '
    user_chord = validate_chord(message_chord)
    chord_notes = get_notes(user_key, user_chord)
    print(f'\nThe following are the chord notes: {chord_notes}.')

if __name__ == '__main__':
    main()


# # Question 14

# In[34]:



d=[{'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
{'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
{'name':'Princess', 'phone':'555-3141', 'email':''},
{'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}]


for dict  in  range(len(d)):
    #print(d[dict])
     dic=d[dict ]
     for keys,values in dic.items():
         #print(keys,values)
         if keys == "phone" and values[-1] == "8":
             print(dic)
         if keys == "email" and values =='':
            print(dic)


# # Question 16

# In[32]:



roman_literal={1 :"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX",10:"X",11:"XI",12:"XII",13:"XIII",14:"XIV",15:"XV",
               16:"XVI",17:"XVII",18:"XVIII",19:"XIX",20:"XX",50:"L",100:"C",500:"D",1000:"M"}


# def roman_Covert(x):
#
#     num_string= str(x)
#     res = [int(x) for x in str(x)]
#
#     for key ,val in roman_literal.items():
#         if x == key:
#            print(roman_literal[key])
#         if x > key and x < key:
#             print(key)
#
#
#
# print(roman_Covert(20))

           #return roman_literal[key]


def int_to_roman(input):
    """ Convert an integer to a Roman numeral. """

    if not isinstance(input, type(1)):
        raise (TypeError,"expected integer, got %s" % type(input))
    if not 0 < input < 4000:
        raise (ValueError, "Argument must be between 1 and 3999")
    ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
    nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
        #print(result,"result")
        #print(input,"Input")
    return ''.join(result)


print(int_to_roman(22))


# In[ ]:




