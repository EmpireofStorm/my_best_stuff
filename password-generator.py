from random import*
letters=["Q","W","E","R","T","Y","U","I","O","P","A","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M","q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
symbols=["[","]",";","'",'''"''',"/",".",",","`","~","?",">","<","|",":","{","}"]
countletters=int(input("How many letters do you want to have in your password?"))
countnumbers=int(input("How many numbers do you want to have in your password?"))
countsymbols=int(input("How many symbols do you want to have in your password?"))
summ=countsymbols+countnumbers+countletters
currentcountletters=0
currentcountnumbers=0
currentcountsymbols=0
currentsumm=0
randomletter=0
randomnumber=0
randomsymbol=0
password=""
something=""
while currentcountnumbers!=countnumbers or currentcountsymbols!=countsymbols or currentcountletters!=countletters:
    randomvariable=randint(0, 2)
    if randomvariable==0:
        if currentcountletters!=countletters:
            randomletter=randint(0, 51)
            something=letters[randomletter]
            password=password+something
            currentcountletters=currentcountletters+1
    elif randomvariable==1:
        if currentcountnumbers!=countnumbers:
            randomnumber=randint(0, 9)
            something=numbers[randomnumber]
            password=password+something
            currentcountnumbers=currentcountnumbers+1
    elif randomvariable==2:
        if currentcountsymbols!=countsymbols:
            randomsymbol=randint(0,16)
            something=symbols[randomsymbol]
            password=password+something
            currentcountsymbols=currentcountsymbols+1
print(password)