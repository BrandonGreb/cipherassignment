# T L Byers
# 20160127
'''*
Description: Caesar cipher uses keys, which encrypt
the message in a different way depending on which key is used.
*'''
#code for encrypting cipher
myMessage = "Help will always be given to those who ask. Albus Dumbledore"
key = 13

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

myTranslated = ''
myMessage = myMessage.upper()

for symbol in myMessage:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        num = num - key
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
        myTranslated = myTranslated + LETTERS[num]

    else:
        myTranslated = myTranslated + symbol

print(myTranslated)

for key in range(len(LETTERS)):
    myTranslated = ''
    for symbol in myMessage:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(LETTERS)
            myTranslated = myTranslated + LETTERS[num]
        else:
            myTranslated = myTranslated + symbol

    print('Key #%s: %s' % (key, myTranslated))

#reverse cipher
myMessage = "Three can keep a secret, " \
            "if two of them are dead. James Bond"

myTranslation = ""
cnt = len(myMessage) - 1

while cnt >= 0:
    myTranslation = myTranslation + myMessage[cnt]
    cnt = cnt - 1

print(myTranslation.lower() + "\n")
print(myTranslation.upper())
#end of reverse cipher

#code for decrypting cipher
