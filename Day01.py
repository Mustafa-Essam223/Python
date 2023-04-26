# # Q1

"""
Write a program that counts up the number of vowels [a, e, i, o,
u] contained in the string.
"""
# s1=input('Enter a string: ')
# s1=s1.lower()
# cnt=0
# for i in range(len(s1)):
#     if s1[i] in ['a', 'e', 'i', 'o','u']:
#         cnt = cnt + 1
# print(f"number of vowels= {cnt}")

#========================================================
# #Q2
"""
Fill an array of 5 elements from the user, Sort it in descending
and ascending orders then display the output.
"""
# l1=[]
# for i in range(5):
#     x=input('Enter a value: ')
#     l1.append(x)

# l1.sort()
# print('Ascending:  ',l1)

# l1.reverse()
# print('Descending ',l1)
#========================================================
# #Q3
"""
Write a program that prints the number of times the string 'iti'
occurs in anystring.
"""
# phrase=input('Enter a phrase: ')
# print('number of occurences of iti =',phrase.count('iti'))

#========================================================

# #Q4
"""
Write a program that remove all vowels from the input word and
generate a brief version of it.
"""
# phrase=input('Enter a phrase: ')
# substituted_phrase=""
# for i in range(len(phrase)):
#      if phrase[i] not in ['a', 'e', 'i', 'o','u']:
#         substituted_phrase+=phrase[i]
# print(substituted_phrase)
          
#========================================================

# # Q5
"""
Write a program that prints the locations of "i" character in any
string you added.
"""

# ss=input("Enter a string: ")
# for idx in range(len(ss)):
#     if ss[idx]=='i':
#         print(idx)

#========================================================

# # Q6
"""
Write a program that generate a multiplication table from 1 to the
number passed.
"""

# num=int(input('Enter a number: '))
# out_list=[]
# for x in range(1,num+1):
#     temp_list=[]
#     for times in range(x):
#         temp_list.append((times+1)*x)
#     #print(temp_list)
#     #print('====')
#     out_list.append(temp_list)
# print(out_list)

#========================================================

# #Q7
""" Write a program that build a Mario pyramid like below:
*
**
***
****
"""

x=int(input('number of lines = '))
for line in range(1,x+1):
    print((x-line)*" "+"*"*line)




"""
“It seems impossible until it is done” :) 
"""