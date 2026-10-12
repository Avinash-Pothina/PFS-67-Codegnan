#regular expression: it is a pattern used to search, match, extract or validate text
#re.search()- search looks for a pattern anywhere inside string
#we need to use search when we want to know as "does this pattern occur somewhere in the text"
#re.match()- checks the pattern only at the beginning
#re.fullmatch()- it requires entire string to match the pattern
#re.findall()- finds all occurences of the pattern and returns as a list
#^ - start of a string (the pattern must start at beginning)
import re
text="I'm Learning Python from 2 weeks 3 days"
res=re.search("Python",text)  #prints none or raises an error based on the compiler if there was no word found in the given text
print(res)
res=re.match("I",text)  #checks the pattern only at the beginning.
print(res)
res=re.fullmatch("I'm Learning Python from 2 weeks 3 days",text)  #fullmatch checks whether the entire string is equal to the given string or not
print(res)
#\d-digits (digits from 0-9)  
#\d+- combination of 1 or more digits
res=re.findall(r"\d+",text)   #returns all the numericals
print(res)
'''
\w -words
\l-letters
'''
res=re.findall(r"\w",text) #outputs each and every letter in the list
print(res)
res=re.findall(r"\w+",text) #outputs words in list just like split() method
print(res)
text=r"^Python"
print(re.search(text,"Python is a programming language")) #returns if the starting striong is as same as the text else returns None

text=r"Python$"
print(re.search(text,"is easy Python")) #returns if the ending string is as same as the text else returns None


#quantifiers: it tells regex how many times something can occur
#it contains: *, +, ?, {}
# * - zero or more
#r"ab*" - a,ab,abb,aabb,abbbbb,abbbbbbbb    these are eligible for "ab*" because b can occur zero or more times
#+ - one or more
#r"ab+"- ab,abb,abbbbb,abbbbb <--acceptable.--> not accceptable a. beacuse atleast one occurence should be of "b" character
#? - Zero or one
#r"colou?r" - color, colour. "u" occurence should be either once or zero times
#{} - exact number
# r"^\d{4}$" - means exactly 4 digits
#1234,3456,5398 <--acceptable. not acceptable-->1,23,763,12387
# r"^\d{4,6}$" - means exactly 4 to 6 digits
#1234,3456,5398,648937,63548 <--acceptable. not acceptable-->1,23,763,1238765

#digits validation:
val=input("enter num: ")
pattern=r"^\d+$"
if re.fullmatch(pattern,val):
    print("Only Digits")
else:
    print("Invalid")


#phone number validation
ph_no=input("Enter Phone Number: ")
ptrn=r"^[6-9]\d{9}$"
if re.fullmatch(ptrn,ph_no):
    print("Valid")
else:
    print("Invalid")

#email validation
em_vld=input("Enter email:")
ptrn=r"^[\w.-]+@[\w.-]+\.\w+$"   #[\w.-]  <-- username. [\w.-]  <-- domain
if re.fullmatch(ptrn,em_vld):
    print("Valid Email")
else:
    print("Invalid Email")

#name and password validation
name=input("Enter Name: ")
pswrd=input("Enter Password: ")
#Name
if re.fullmatch(r"[A-Za-z]+",name):
    print("Name is Valid")
else:
    print("Name is Invalid")
ptrn=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
'''
r --> raw String
^ --> start of String
Part	Meaning
^	Start of the string
(?=.*[A-Z])	Must contain at least one uppercase letter
(?=.*[a-z])	Must contain at least one lowercase letter
(?=.*\d)	Must contain at least one digit
.+	One or more characters
$	End of the string
'''
if re.fullmatch(ptrn,pswrd):
    print("Password is Strong")
else:
    print("Password is too weak")

