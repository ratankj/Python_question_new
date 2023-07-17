"""


Count Characters in a String:
Description: Write a program that counts the occurrences of each character in a given string.
Example:
Input: "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

Find Maximum and Minimum:
Description: Write a program to find the maximum and minimum numbers in a given list.
Example:
Input: [4, 9, 2, 7, 5]
Output: Maximum: 9, Minimum: 2

Calculate Average:
Description: Write a program that calculates the average of a given list of numbers.
Example:
Input: [2, 4, 6, 8]
Output: 5.0

Check Palindrome:
Description: Write a program to check if a given string is a palindrome.
Example:
Input: "racecar"
Output: True
Remove Duplicates:

Description: Write a program that removes duplicates from a given list.
Example:
Input: [1, 2, 3, 2, 4, 1, 5]
Output: [1, 2, 3, 4, 5]

Reverse List Order:
Description: Write a program that reverses the order of elements in a given list.
Example:
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]

Check Armstrong Number:
Description: Write a program to check if a given number is an Armstrong number.
Example:
Input: 153
Output: True

Remove Characters:
Description: Write a program that removes specified characters from a given string.
Example:
Input: "Hello World", ['l', 'o']
Output: "He Wrld"

Check Perfect Number:
Description: Write a program to check if a given number is a perfect number.
Example:
Input: 28
Output: True

Print Prime Factors:
Description: Write a program that prints all the prime factors of a given number.
Example:
Input: 24
Output: 2, 3

Calculate GCD:
Description: Write a program to calculate the greatest common divisor (GCD) of two given numbers.
Example:
Input: 24, 36
Output: 12

Count Words in a Sentence:
Description: Write a program that counts the number of words in a given sentence.
Example:
Input: "Hello, how are you?"
Output: 4

Find Common Elements:
Description: Write a program that finds common elements between two given lists.
Example:
Input: [1, 2, 3, 4, 5], [4, 5, 6, 7, 8]
Output: [4, 5]

Calculate Square Root:
Description: Write a program to calculate the square root of a given number using the Newton-Raphson method.
Example:
Input: 16
Output: 4.0

Swap Case:
Description: Write a program that swaps the case (upper to lower and vice versa) of each character in a given string.
Example:
Input: "Hello, World!"
Output: "hELLO, wORLD!"


Password Strength Checker:
Description: Write a program that checks the strength of a password based on the following criteria:

Contains at least 8 characters
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit
Example:
Input: "Passw0rd"
Output: Strong password

Sentence Capitalizer:
Description: Write a program that capitalizes the first letter of each word in a given sentence.
Example:
Input: "hello world"
Output: "Hello World"

Word Frequency Counter:
Description: Write a program that counts the frequency of each word in a given text.
Example:
Input: "Hello world. Hello Python. Python is awesome."
Output: {'Hello': 2, 'world': 1, 'Python': 2, 'is': 1, 'awesome': 1}

Anagram Checker:
Description: Write a program that checks if two given strings are anagrams of each other.
Example:
Input: "listen", "silent"
Output: True

Matrix Transpose:
Description: Write a program that calculates the transpose of a given matrix.
Example:
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

Binary to Decimal Converter:
Description: Write a program that converts a binary number to its decimal equivalent.
Example:
Input: "1010"
Output: 10

Caesar Cipher:
Description: Write a program that encrypts a given string using the Caesar cipher technique.
Example:
Input: "Hello", shift=3
Output: "Khoor"




"""

print("************************************* NEXT PROGRAM ********************************************** ")


"""

Count Characters in a String:
Description: Write a program that counts the occurrences of each character in a given string.
Example:
Input: "hello"
Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

"""

input_string = input("Enter a string: ")
char_count = {}

for char in input_string:
    if char in char_count:

        char_count[char] += 1

    else:
        char_count[char] = 1

print(char_count)




print("************************************* NEXT PROGRAM ********************************************** ")


"""

Find Maximum and Minimum:
Description: Write a program to find the maximum and minimum numbers in a given list.
Example:
Input: [4, 9, 2, 7, 5]
Output: Maximum: 9, Minimum: 2

"""

l= [4, 9, 21,1, 7, 5]
max=l[0]
min=l[0]
for i in l:
    if i > max:
        max=i
    elif i < min:
        min = i


print(f"Minimum : {min}, maximum : {max}")



print("************************************* NEXT PROGRAM ********************************************** ")

"""


Calculate Average:
Description: Write a program that calculates the average of a given list of numbers.
Example:
Input: [2, 4, 6, 8]
Output: 5.0

"""


lst = [2, 4, 6, 8]
add= 0
count =0

for i in lst:
    add=add+i
    count=count+1

avg=add/count

print(f"final output is  {avg}")



print("************************************* NEXT PROGRAM ********************************************** ")



"""


Check Palindrome:
Description: Write a program to check if a given string is a palindrome.
Example:
Input: "racecar"
Output: True
Remove Duplicates:


"""


pal= input("enter a string to check the string is palinedrom or not : ")
new_rev = pal[::-1]

if pal==new_rev:
    print("True")

else:
    print("False")



print("************************************* NEXT PROGRAM ********************************************** ")



"""


Description: Write a program that removes duplicates from a given list.
Example:
Input: [1, 2, 3, 2, 4, 1, 5]
Output: [1, 2, 3, 4, 5]



"""


lst= [1, 2, 3, 2, 4, 1, 5]
print(f"older list: {lst}")
new_l= []
for i in lst:
    if i not in new_l:
        new_l = new_l + [i]
print(f"new list after duplication of list  :  {new_l}")


print("************************************* NEXT PROGRAM ********************************************** ")




"""


Reverse List Order:
Description: Write a program that reverses the order of elements in a given list.
Example:
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]


"""


lst= [1, 2, 3, 4, 5]
new_l =[]
while lst:
    max=lst[0]
    for i in lst:
        if i > max:
            max=i

    new_l=new_l+[max]
    lst.remove(max)

print(f"new list: {new_l}")



#------------------------------------------------------------------------------------

"""Reverse List Order:
Description: Write a program that reverses the order of elements in a given list.
Example:
Input: [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]"""

list = [4,5,8,9,7,2]
first_index = 0
last_index = len(list) - 1
while first_index < last_index:
    temp = list[first_index]
    list[first_index],list[last_index] = list[last_index],temp
    #list[last_index] = temp
    first_index += 1
    last_index -= 1
print(list)




print("************************************* NEXT PROGRAM ********************************************** ")


"""


Check Armstrong Number:
Description: Write a program to check if a given number is an Armstrong number.
Example:
Input: 153
Output: True

"""


num = input("Enter the number: ")
sum = 0
length = len(num)
for digit in num:
      digit_int = int(digit)
      sum += digit_int ** length

#print(sum)
sum = str(sum)
if sum == num:
      print ("The number is armstrong number")
else:
      print("The number is not an armstrong number")




# -----------------------------------------------------------------------------------


num=int(input("enter a num:"))
order =len(str(num))
sum=0
temp=num
while temp>0:
    digit = temp % 10  # 153%10 =3
    sum = sum + digit**int(order)
    temp//=10
if num == sum:
    print("Given ",num, "is an Armstrong number")
else:
    print("Given ",num, "is not an Armstrong number")




print("************************************* NEXT PROGRAM ********************************************** ")


"""


Remove Characters:
Description: Write a program that removes specified characters from a given string.
Example:
Input: "Hello World", ['l', 'o']
Output: "He Wrld"


"""
new_l =[]
new_s=""
user_str = input("enter the string: ")
print(f"given string is {user_str}")
letter_remove = int(input("how many letter do u want to remove: "))

for i in range(letter_remove):
    enter_str = input("enter the char u want to remove: ")
    new_l =new_l+[enter_str]
print(f"The strings u want to remove are : {new_l}")


for i in user_str:
    if i not in new_l:
        new_s=new_s+i
print(f"Final string is : {new_s}")





print("************************************* NEXT PROGRAM ********************************************** ")


"""

Check Perfect Number:
Description: Write a program to check if a given number is a perfect number.
Example:
Input: 28
Output: True


"""


num=int(input("enter a number: "))
add=0
for i in range(1,num):
    if num%i==0:
        add=add+i
#print(add)
if add == num:
    print(f"True: this is a perfect number : {num}")
else:
    print(f"False: this is not a perfect number : {num}")






print("************************************* NEXT PROGRAM ********************************************** ")


"""

Print Prime Factors:
Description: Write a program that prints all the prime factors of a given number.
Example:
Input: 24
Output: 2, 3


"""








number = int(input("Enter a number: "))
factors = []
divisor = 2

while number > 1:
    if number % divisor == 0:
        #print(divisor)
        factors.append(divisor)
        #print(factors)
        number //= divisor
        #print(number)
    else:
        divisor += 1

print("Prime factors:")
print(*factors, sep=', ')




print("************************************* NEXT PROGRAM ********************************************** ")


"""

Print Prime Factors:
Description: Write a program that prints all the prime factors of a given number.
Example:
Input: 24
Output: 2, 3


"""


number = int(input("Enter a number: "))
factors = []
divisor = 2

for i in range(number):
    if number%divisor==0:
        factors=factors+[divisor]

        number=number//divisor
    else:
        divisor=divisor+1

print(factors)




print("************************************* NEXT PROGRAM ********************************************** ")


"""

Calculate GCD:
Description: Write a program to calculate the greatest common divisor (GCD) of two given numbers.
Example:
Input: 24, 36
Output: 12


"""


number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a number: "))
factors = []
divisor=2

if number_1 < number_2:
    print(number_1)
else:
    print(number_2)

for i in range(number_1):
    if number_1 % divisor == 0 and number_2 % divisor ==0:
        factors=factors+[divisor]
        divisor = divisor + 1

    else:
        divisor=divisor+1
print(factors)

max=factors[0]
for i in factors:
    if i>max:
        max=i


print(f"The greatest common divisor (GCD) of {number_1} and {number_2} is : {max} ")



# ---------------------------------------------------------------------------------------------

"""
Calculate GCD:
Description: Write a program to calculate the greatest common divisor (GCD) of two given numbers.
Example:
Input: 24, 36
Output: 12
"""

num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))
while num2 != 0:
  temp = num1 % num2
  num1 = num2
  num2 = temp
print(num1)


print("************************************* NEXT PROGRAM ********************************************** ")


"""

Count Words in a Sentence:
Description: Write a program that counts the number of words in a given sentence.
Example:
Input: "Hello, how are you?"
Output: 4



"""

strr = "Hello, how are you?"
count=1
for i in strr:
    if i==' ':
        count=count+1

print(count)


print("************************************* NEXT PROGRAM ********************************************** ")




"""

Find Common Elements:
Description: Write a program that finds common elements between two given lists.
Example:
lst_1: [1, 2, 3, 4, 5]
 lst_2: [4, 5, 6, 7, 8]
Output: [4, 5]

"""


lst_1 = [1, 2, 3, 4, 5]
lst_2 =[4, 5, 6, 7, 8]

new_l =[]

for i in lst_1:
    for j in lst_2:
        if i == j:
            new_l=new_l + [i]
print(f"The new list is : {new_l}")


print("************************************* NEXT PROGRAM ********************************************** ")


"""

Calculate Square Root:
Description: Write a program to calculate the square root of a given number using the Newton-Raphson method.
Example:
Input: 16
Output: 4.0


"""



input_number = float(input("Enter a number: "))

if input_number < 0:
    print("Invalid input: Cannot calculate square root of a negative number.")
else:
    num = input_number / 2  # Initial guess
    epsilon = 0.0001  # Desired level of accuracy

    while abs(num * num - input_number) > epsilon:
        num = (num + input_number / num) / 2

    print(num)



print("************************************* NEXT PROGRAM ********************************************** ")



""""

Swap Case:
Description: Write a program that swaps the case (upper to lower and vice versa) of each character in a given string.
Example:
Input: "Hello, World!"
Output: "hELLO, wORLD!"

"""




input_user = input("Enter the string: ")
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
output_string = ""

for i in input_user:
    if i in capital:
        output_string += i.lower()
    elif i in lower:
        output_string += i.upper()
    else:
        output_string += i

print(output_string)



print("************************************* NEXT PROGRAM ********************************************** ")


"""

Password Strength Checker:
Description: Write a program that checks the strength of a password based on the following criteria:

Contains at least 8 characters
Contains at least one uppercase letter
Contains at least one lowercase letter
Contains at least one digit
Example:
Input: "Passw0rd"
Output: Strong password

"""


capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'
num = '0123456789'
special_char = "!@#$%^&*-+=~`|\/:;\"'?.,_()[]{}<>"

flag_a = False
flag_b = False
flag_c = False
flag_d = False

length = 0
password_strength = input("Enter your password: ")

for i in password_strength:
    length += 1

print(f"The length of the password is: {length}")

count = 0

if length > 7:
    count += 1

for i in password_strength:
    if i in capital:
        flag_a = True
    elif i in small:
        flag_b = True
    elif i in num:
        flag_c = True
    elif i in special_char:
        flag_d = True
    else:
        print("empty")



if flag_d:
    count += 1

if flag_a:
    count += 1

if flag_b:
    count += 1

if flag_c:
    count += 1

print(count)

if count == 5:
    print("very strong")

elif count == 4:
    print('Very strong')
elif count == 3:
    print('Strong')
elif count == 2:
    print('Moderate')
elif count < 2:
    print('Weak')





print("********************************** NEXT PROGRAM ***************************************************** ")



""""

Sentence Capitalizer:
Description: Write a program that capitalizes the first letter of each word in a given sentence.
Example:
Input: "hello world"
Output: "Hello World"

"""





input_str = "hello world cat dog"
output_str = ""
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'
if input_str[0] in small:
    output_str += chr(ord(input_str[0]) - 32)
for i in range(1,len(input_str)):

    if input_str[i] == ' ':
        output_str += ' '
        if input_str[i+1] in small:
            output_str += chr(ord(input_str[i+1]) - 32)
            i = i+1
        else:
            output_str += input_str[i+1]
    else:
        output_str += input_str[i]

print(output_str)


# ------------------------------------------------------------------------------------


input_str = "hello world cat dog"
print(input_str)
output_str = ""
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'

prev_char = ' '

for char in input_str:
    if prev_char == ' ' and char in small:
        output_str += chr(ord(char) - 32)
    else:
        output_str += char
    prev_char = char

print(output_str)



print("********************************** NEXT PROGRAM ***************************************************** ")


"""

Word Frequency Counter:
Description: Write a program that counts the frequency of each word in a given text.
Example:
Input: "Hello world. Hello Python. Python is awesome."
Output: {'Hello': 2, 'world': 1, 'Python': 2, 'is': 1, 'awesome': 1}

"""




"""

Word Frequency Counter:
Description: Write a program that counts the frequency of each word in a given text.
Example:
Input: "Hello world. Hello Python. Python is awesome."
Output: {'Hello': 2, 'world': 1, 'Python': 2, 'is': 1, 'awesome': 1}

"""


input_string = "Hello world. Hello Python. Python is awesome."
words = input_string.split()
print(words)
word_frequency = {}

for word in words:

    word = word.strip(".,")

    if word in word_frequency:
        word_frequency[word] += 1

    else:
        word_frequency[word] = 1

print(word_frequency)







print("********************************** NEXT PROGRAM ***************************************************** ")



"""
Task 20: Number System Converter
Description: Develop a program that converts a given number from one number system to another (e.g., binary to decimal).
Example Input: Binary number = "10101"
Example Output: "The decimal equivalent is 21.
"""


number_system = "binary"
number = "10101"

if number_system == "binary":
  decimal_equivalent = int(number, 2)
elif number_system == "decimal":
  decimal_equivalent = int(number)
elif number_system == "octal":
  decimal_equivalent = int(number, 8)
elif number_system == "hexadecimal":
  decimal_equivalent = int(number, 16)
else:
  raise ValueError(f"Invalid number system: {number_system}")

print(f"The decimal equivalent is {decimal_equivalent}")








print("********************************** NEXT PROGRAM ***************************************************** ")
""""


Caesar Cipher:
Description: Write a program that encrypts a given string using the Caesar cipher technique.
Example:
Input: "Hello", shift=3
Output: "Khoor"


"""






input_str = "hello"
print(input_str)
output_str = ""
capital = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small = 'abcdefghijklmnopqrstuvwxyz'

for i in input_str:

    if i in small:
        output_str += chr(ord(i) - 29)
    elif i in capital:
        output_str += chr(ord(i) + 35)
    else:
        output_str += " "

print(output_str)



print("********************************** NEXT PROGRAM ***************************************************** ")




""""


Matrix Transpose:
Description: Write a program that calculates the transpose of a given matrix.
Example:
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

"""



input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output_matrix = []

# Determine the dimensions of the input matrix
rows = len(input_matrix)
print(rows)
cols = len(input_matrix[0])
print(cols)

# Create an empty output matrix with swapped dimensions
for i in range(cols):
    output_matrix.append([0] * rows)

# Calculate the transpose by swapping the elements
for i in range(rows):
    for j in range(cols):
        output_matrix[j][i] = input_matrix[i][j]

print(output_matrix)


print("********************************** NEXT PROGRAM ***************************************************** ")


"""

Anagram Checker:
Description: Write a program that checks if two given strings are anagrams of each other.
Example:
Input: "listen", "silent"
Output: True

"""





str1 = "listen"  #1.covert lower 2. check length 3. sort the string 4. check same char or  not
str2 = "silent"

str1 = str1.lower()
str2 = str2.lower()

if(len(str1) == len(str2)):

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    if(sorted_str1 == sorted_str2):
        print("str1 and str2 are  anagram ")
    else:
        print("str1 and str2 are not anagram ")

else:
    print( "str1 and str2 are not anagram.")