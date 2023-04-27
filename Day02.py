# Q1
"""
Write a function that accepts two arguments (length, start) to
generate an array of a specific length filled with integer numbers
increased by one from start.
"""
# def fun(len,start):
#     arr=[]
#     for i in range(len):
#         arr.insert(i,start)
#         start=start+1
#     return arr

# start=int(input('enter a start: '))
# len=int(input('enter length: '))

# print(fun(len,start))


#========================================================================================


# Q2

"""
write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and if it is divisible by 5 return
"buzz" and if is is divisible by both return "FizzBuzz"
"""

# def reminder(x):
#     if x % 3 == 0 and x % 5 == 0:
#         return 'FizzBuzz'
#     if x % 3 == 0:
#         return 'Fizz'
#     if x % 5 == 0:
#         return 'Bizz'
#     return 'not defined'

# n=int(input('Enter A number: '))
# print(reminder(n))
    

#========================================================================================

#Q3 

"""
Write a function which has an input of a string from user then it
will return the same string reversed.
"""
# def reverse(s1):
#     return s1[::-1]


# text=input('Enter a string to be reversed: ')
# print(reverse(text))

#========================================================================================
# Q4

"""
Ask the user for his name then confirm that he has entered his
name(not an empty string/integers). then proceed to ask him for
his email and print all this data (Bonus) check if it is a valid email
or not
"""
# from validate_email_address import validate_email
    
# def usrname_validate(name):
#     cnt = len(name)
#     for ch in name:
#         code = ord(ch)
#         if 47 < code < 58:
#             cnt = cnt -1
#     return cnt == len(name)  and name!=""



    


# username=input('username: ')
# if usrname_validate(username):
#     mail=input('email: ') # mustaf.essam.abdelmenaem@gmail.com
#     valid=validate_email(mail)
#     if valid == True: 
#         print('Success!')
#     else:
#         print('Failed!')
# else:
#     print('username is not valid !!')



#===========================================================

# Q5
"""
Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For example, if
the string is 'abdulrahman' then the output is: Longest substring in
alphabetical order is: abdu
"""

# def longestSubstr(s):
#     longest = []
#     cur = []
#     for char in s:
#         if not cur or char >= cur[-1]: # m4 faddy aw l current char > mn a5r wa7d m3aia
#             cur.append(char)
#         else: # faddy, htt3ml awl 7rf 
#             cur = [char]
#         if len(cur) > len(longest):
#             longest=cur
#     return ''.join(longest)

# strr=input('Enter a string: ')
# print(longestSubstr(strr))

#=================================================================

# Q6
"""
Write a program which repeatedly reads numbers until the user
enters “done”.
- Once “done” is entered, print out the total, count, and
    average of the numbers.
- If the user enters anything other than a number, detect their
    mistake, print an error message and skip to the next number.
"""

# def read_data():
#     summ = 0
#     cntr = 0
#     while True:
#         x = input('Enter a value(enter done to stop) : ')
#         if x.isdigit():
#             summ = summ + int(x)
#             cntr = cntr + 1
#         elif x == 'done':
#             break
#         else:
#             print('Enter a valid input!!')

#     print('Sum = ',summ)
#     print('cnt = ',cntr)
#     print('avg = ',summ/cntr)

# print('Calling function . . .')
# read_data()


#=================================================================

# Q7
"""
Word guessing game (hangman)
○
A list of words will be hardcoded in your program, out of
which the interpreter will
○choose 1 random word.
○The user first must input their names
○
Ask the user to guess any alphabet. If the random word
contains that alphabet, it
○will be shown as the output(with correct placement)
○Else the program will ask you to guess another alphabet.
○Give 7 turns maximum to guess the complete word.
"""

# import random 
# def hangman():
    
#     words = ['tower','snake','mario']
    
#     rand_idx = random.randint(0,len(words)-1)
    
#     rand_wrd= words[rand_idx]
    
#     print (rand_idx)
    
#     name=input('Enter ur name: ')
    
#     char= input('guess a char: ')[0]
    
#     new_word="-"*len(rand_wrd)
    
#     for t in range(7):
#         char_idx=rand_wrd.find(char)
#         if char_idx !=-1:
    
#             print("correct suggestion found at position ",char_idx)
            
#             new_word=new_word[:char_idx]+rand_wrd[char_idx]+new_word[char_idx+1:]
            
#             print('gussed: ',new_word)
#             if new_word == rand_wrd:
#                 print("correct word!")    
            
#         else:
#             print('guess another alphabet.')

#         char= input('guess a char: ')[0]





# hangman()