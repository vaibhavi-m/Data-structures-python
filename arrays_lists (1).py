#!/usr/bin/env python
# coding:

# In[7]:

#1
#is unique:
#implement an algo to detrmine if a string has all unique characters
def isunique(str):
    l=[]
    for i in str:
        if i not in l:
            l.append(i)
    if len(l)==len(str):
        print("True")
    else:
        print("false")
n=str(input("enter a string "))
isunique(n)


# In[11]:

#2
#Check Permutation
#Given two strings write a method to decide if one is a permutation of another

#Method 1
def permutation(a,b):
    if len(a)!=len(b):
        print("Not permutation")
    else:
        if sorted(a)==sorted(b):
            print("permutation")
        else:
            print("Not permutation")
permutation("abc","dabc")


# In[18]:

#method 2
# Python program to check if two strings are
# Permutations of each other
NO_OF_CHARS = 256
 
# Function to check whether two strings are
# Permutation of each other
def arePermutation(str1, str2):
 
    # Create two count arrays and initialize
    # all values as 0
    count1 = [0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
 
    # For each character in input strings,
    # increment count in the corresponding
    # count array
    for i in str1:
        count1[ord(i)]+=1
 
    for i in str2:
        count2[ord(i)]+=1
 
    # If both strings are of different length.
    # Removing this condition will make the
    # program fail for strings like
    # "aaca" and "aca"
    if len(str1) != len(str2):
        return 0
 
    # Compare count arrays
    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return 0
 
    return 1
 
# Driver program to test the above functions
str1 = "geeksforgeeks"
str2 = "forgeeksgeeks"
if arePermutation(str1, str2):
    print ("Yes")
else:
    print ("No")


# In[31]:

#3
#URLify
#replace spaces in a string with %20
n='abc def ghi'
n.replace(' ','%20')


# In[5]:

#4
#palindrome permutation
#Write a function to check if it is a permutation of a palindrome
from collections import Counter
def any_palindrome(myString):
    alpha_chars_only = [x for x in myString.lower() if x.isalpha()]
    counts = Counter(alpha_chars_only)
    number_of_odd = sum(1 for letter, cnt in counts.items() if cnt%2)
    return number_of_odd <= 1
n=input("enter a string ")
print(any_palindrome(n))
#True


# In[35]:

#method 2
def permutation_palindrome(n):
    a='Tact Coa'
    b=(a.replace(' ','')).lower()
    c=(n.replace(' ','')).lower()
    if c==c[::-1]:
        if sorted(b)==sorted(c):
            print("True")
        else:
            print("false")
    else:
        print("false")
permutation_palindrome('atco cta')


# In[39]:

#5
#ONE away
#Given two strings write a function to check if they are one edit away
def one_away(s1,s2):
    a=len(s1)
    b=len(s2)
    i=0
    j=0
    count=0
    if abs(a - b) > 1:
        return False
    while i<a and j<b:
        if s1[i]!=s2[j]:
            if count==1:
                return False
            if a>b:
                i+=1
            if b>a:
                j+=1
            else:
                i+=1
                j+=1
            count+=1
        else:
            i+=1
            j+=1
    if i<a or j<b:
        count+=1
    
    return count==1
one_away('pale','bail')


# In[87]:

#6
#string Compression
#Implement a method to perform basic string compression using the count of repeated characters
def compression(s):
    res=''
    count=1
    for i in range(1,len(s)):
        if s[i-1]==s[i]:
            count+=1
        else:
            res=res+s[i-1]
            if count>1:
                res+=str(count)
            count=1 #reset the value for next alphabet
    res = res + s[-1]
    if count > 1:
        res += str(count)
    return res
s = "abbbccddddde"
print(compression(s))  


# In[89]:

#method 2
def compress(string):
    index = 0
    compressed = ""
    len_str = len(string)
    while index != len_str:
        count = 1
        while (index < len_str-1) and (string[index] == string[index+1]):
            count = count + 1
            index = index + 1
        if count == 1:
            compressed += str(string[index])
        else:
            compressed += str(string[index]) + str(count)
        index = index + 1
    return compressed
s = "abbbccddddde"
print(compress(s))

