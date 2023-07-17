


"""

Word Frequency Counter:
Description: Write a program that counts the frequency of each word in a given text.
Example:
Input: "Hello world. Hello Python. Python is awesome."
Output: {'Hello': 2, 'world': 1, 'Python': 2, 'is': 1, 'awesome': 1}

"""






""""


Matrix Transpose:
Description: Write a program that calculates the transpose of a given matrix.
Example:
Input: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

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