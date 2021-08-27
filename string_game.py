'''Game Rules
Both players are given the same string,
Both players have to make substrings
to make words starting with consonants
Kevin has to make words starting with
The game ends when both players have
Scoring
A player gets point for each
For Example:
String = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA
points.
For better understanding, see the image
Your task is to determine the winner
Input Format
A single line of input containing the
Note: The string will contain only
Constraints'''

print("welcome kiran and abhay")
word= input("enter the word : ")
print("kirans turn                                                              press x to give up")
import re
kiran_score = 0
abhay_score = 0
kirans_list = list()
abhay_list = list()
com = ["a","e","i","o","u"]

while(True):
    x = input("enter the string : ")
    if x=="x":
        break
    l = re.findall(x,word)
    score = len(l)
    if x in word:
        if x[0] not in com:
            if x not in kirans_list:
                kirans_list.append(x)
                kiran_score=kiran_score+score
print(kirans_list)
print(kiran_score)

print("abhays turn                                                              press x to give up")

while(True):
    x = input("enter the string : ")
    if x=="x":
        break
    l = re.findall(x,word)
    score = len(l)
    print(score)
    if x in word:
        if x[0] in com:
            if x not in abhay_list:
                abhay_list.append(x)
                abhay_score=abhay_score+score
print(abhay_list)
print(abhay_score)

if abhay_score>kiran_score:
    print("abhay wins")
else:
    print("kiran wins")
