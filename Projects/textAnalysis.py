'''
author = Pavel Drexler

'''
import sys


TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]
users = {"bob" :"123",
 		"ann" : "pass123"  ,  
 		"mike": "password123", 
 		"liz":  "pass123" 
}
loginOk = 0
titleNum = 0
upperNum = 0
lowerNum = 0
numericNum = 0
numericValue = 0

wordLenFrq = dict()
sortedDict = dict()


print ('Welcome to the app. Please log in.')
name = input('Name:')
password = input('Password:')

if name in users:
	if users[name] == password :
		print ("Login successful")
		loginOk = 1
	else:
		print ("Wrong password.")
		sys.exit()
else:
		print ("Wrong user name.")
		sys.exit()

#login successful - select Text:  
if loginOk == 1:
	print ("We have three texts to be analyzed.")
	textNum =int(input("Enter a number btw. 1 and 3 to select:"))
	if not (textNum >= 1 and textNum <= 3):
		print("wrong number")
		sys.exit()
	else:
		print("===Text analyzation started===")


#analyze Text
splitText = TEXTS[textNum-1].split()
total = len(splitText)

for word in splitText:
	if word.istitle():
		titleNum += 1
	if word.isupper():
		upperNum += 1
	if word.islower():
		lowerNum += 1
	if word.isnumeric():
		numericNum += 1
		numericValue += int(word)
	length = len(word)
	if (length not in wordLenFrq):
	   wordLenFrq[length] = 0
	wordLenFrq[length] += 1

#write output
for key in sorted(wordLenFrq.keys()):
	print (key,"\t:","*"*int(wordLenFrq[key]), wordLenFrq[key])
print ("Count of numeric only words is: ",numericValue)



