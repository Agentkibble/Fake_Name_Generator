import random
from random import randint
from faker import Faker
import string

def Ran_num():
    number = randint(1234567890,9999999999)
    return number

def name():
    name_gen = Faker()
    fake_name = name_gen.name()
    name_leng = len(fake_name)
    trunc_ammount = fake_name.find(' ')
    First_Name = fake_name[0:trunc_ammount]
    Last_Name = fake_name[(trunc_ammount+1):name_leng]
    return First_Name, Last_Name;
  
def Main(number):
    answer = number
    while 1:
        FIRST_NAME, LAST_NAME = name()
        FIRST_NAME = FIRST_NAME.lower()
        LAST_NAME = LAST_NAME.lower()
        EMAIL = FIRST_NAME + '.' + LAST_NAME
        Ran_Email_num = randint(0,9999)
        Ran_Email_num = str(Ran_Email_num)
        Domain = ['@aol.com', '@gmail.com', '@yahoo.com', '@hotmail.com', '@outlook.com', '@msn.com', '@protonmail.com', '@aim.com', '@icloud.com']
        Ran_Domain_num = randint(0,8)
        PHONE_NUMBER = Ran_num()
        PHONE_NUMBER = str(PHONE_NUMBER)
        EMAIL = EMAIL + Ran_Email_num + Domain[Ran_Domain_num]
        if answer == 1:
            print(PHONE_NUMBER)
        elif answer == 2:
            Ran_Email = randint(0,1)
            if Ran_Email == 1:
                print(EMAIL)
            else:
                letter = random.choice(string.ascii_lowercase)
                letter = str(letter)
                EMAIL = letter + LAST_NAME + Ran_Email_num + Domain[Ran_Domain_num]
                print(EMAIL)
        elif answer == 3:
            print(FIRST_NAME + ':' + LAST_NAME)
        elif answer == 12:
            print(PHONE_NUMBER + ':' + EMAIL)
        elif answer == 13:
            print(PHONE_NUMBER + ':' + FIRST_NAME + ':' + LAST_NAME)
        elif answer == 23:
            print(EMAIL + ':' + FIRST_NAME + ':' + LAST_NAME)
        elif answer == 123:
            print(PHONE_NUMBER + ':' + EMAIL + ':' + FIRST_NAME + ':' + LAST_NAME)
        else:
            break

answer = input('Phone = 1, Email = 2, Names = 3: ')
answer = int(answer)
Main(answer)