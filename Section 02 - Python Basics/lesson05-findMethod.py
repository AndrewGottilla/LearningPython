statement = "My favorite video game is Persona 5 Royale!"
print(statement.find('video game')) #returns 12 (first positionn where the string that was found started)

statement02 = "I love video games!".find('video game')
print(statement02) #returns 7 (first position where the string that was found started)

spam_mail = "SAVE NOW!! $$$ COUPONNS INSIDE $$$ 24 HOURS LEFT!!".find('$$$')
print(spam_mail) #returns 11 (find method will return first instance only)
