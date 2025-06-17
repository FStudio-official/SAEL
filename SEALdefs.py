
def l2i(letter=str()):
    letter=letter.lower()

    if letter==" ":
        li=53 
    if letter=="a":
        li=1 
    if letter=="b":
        li=2    
    if letter=="c":
        li=3    
    if letter=="d":
        li=4    
    if letter=="e":
        li=5    
    if letter=="f":
        li=6    
    if letter=="g":
        li=7    
    if letter=="h":
        li=8    
    if letter=="i":
        li=9    
    if letter=="j":
        li=10    
    if letter=="k":
        li=11   
    if letter=="l":
        li=12   
    if letter=="m":
        li=13   
    if letter=="n":
        li=14   
    if letter=="o":
        li=15   
    if letter=="p":
        li=16   
    if letter=="q":
        li=17   
    if letter=="r":
        li=18   
    if letter=="s":
        li=19   
    if letter=="t":
        li=20   
    if letter=="u":
        li=21    
    if letter=="v":
        li=22   
    if letter=="w":
        li=23   
    if letter=="x":
        li=24   
    if letter=="y":
        li=25   
    if letter=="z":
        li=26
    if letter==",":
        li=58
    if letter=="!":
        li=57
    if letter==".":
        li=56
    if letter=="-":
        li=55
    if letter=="?":
        li=54
    return li-1
def i2l(inti=int()):
    il=str()
    if inti == -26:
        il = "a"
    elif inti == -25:
        il = "b"
    elif inti == -24:
        il = "c"
    elif inti == -23:
        il = "d"
    elif inti == -22:
        il = "e"
    elif inti == -21:
        il = "f"
    elif inti == -20:
        il = "g"
    elif inti == -19:
        il = "h"
    elif inti == -18:
        il = "i"
    elif inti == -17:
        il = "j"
    elif inti == -16:
        il = "k"
    elif inti == -15:
        il = "l"
    elif inti == -14:
        il = "m"
    elif inti == -13:
        il = "n"
    elif inti == -12:
        il = "o"
    elif inti == -11:
        il = "p"
    elif inti == -10:
        il = "q"
    elif inti == -9:
        il = "r"
    elif inti == -8:
        il = "s"
    elif inti == -7:
        il = "t"
    elif inti == -6:
        il = "u"
    elif inti == -5:
        il = "v"
    elif inti == -4:
        il = "w"
    elif inti == -3:
        il = "x"
    elif inti == -2:
        il = "y"
    elif inti == -1:
        il = "z"
    elif inti == 0:
        il = "a"
    elif inti == 1:
        il = "b"
    elif inti == 2:
        il = "c"
    elif inti == 3:
        il = "d"
    elif inti == 4:
        il = "e"
    elif inti == 5:
        il = "f"
    elif inti == 6:
        il = "g"
    elif inti == 7:
        il = "h"
    elif inti == 8:
        il = "i"
    elif inti == 9:
        il = "j"
    elif inti == 10:
        il = "k"
    elif inti == 11:
        il = "l"
    elif inti == 12:
        il = "m"
    elif inti == 13:
        il = "n"
    elif inti == 14:
        il = "o"
    elif inti == 15:
        il = "p"
    elif inti == 16:
        il = "q"
    elif inti == 17:
        il = "r"
    elif inti == 18:
        il = "s"
    elif inti == 19:
        il = "t"
    elif inti == 20:
        il = "u"
    elif inti == 21:
        il = "v"
    elif inti == 22:
        il = "w"
    elif inti == 23:
        il = "x"
    elif inti == 24:
        il = "y"
    elif inti == 25:
        il = "z"
    elif inti == 26:
        il = "a"
    elif inti == 27:
        il = "b"
    elif inti == 28:
        il = "c"
    elif inti == 29:
        il = "d"
    elif inti == 30:
        il = "e"
    elif inti == 31:
        il = "f"
    elif inti == 32:
        il = "g"
    elif inti == 33:
        il = "h"
    elif inti == 34:
        il = "i"
    elif inti == 35:
        il = "j"
    elif inti == 36:
        il = "k"
    elif inti == 37:
        il = "l"   
    elif inti == 38:
        il = "m"         
    elif inti == 39:
        il = "n"         
    elif inti == 40:
        il = "o"         
    elif inti == 41:
        il = "p"         
    elif inti == 42:
        il = "q"         
    elif inti == 43:
        il = "r"         
    elif inti == 44:
        il = "s"         
    elif inti == 45:
        il = "t"         
    elif inti == 46:
        il = "u"         
    elif inti == 47:
        il = "v"         
    elif inti == 48:
        il = "w"         
    elif inti == 49:
        il = "x"         
    elif inti == 50:
        il = "y"         
    elif inti == 51:
        il = "z"         
    elif inti == 52:
        il = " "
    elif inti==56:
        il="!"
    elif inti==57:
        il=","
    elif inti==55:
        il="."
    elif inti==54:
        il="-"
    elif inti==53:
        il="?"
    return str(il)


def encrypt(key=str("a"),msg=str()):
    while len(key)<len(msg):
        key=key+key
    mletters=[mletter for mletter in msg]
    kletters=[kletter for kletter in key]
    kz=list()
    mz=list()
    for mletter in mletters:
        mz.append(l2i(mletter))
    for kletter in kletters:
        kz.append(l2i(kletter))
    els=[]
    for i in range(len(mz)):
        if not (mz[i]==52 or mz[i]==53 or mz[i]==54 or mz[i]==55 or mz[i]==56 or mz[i]==57):
            els.append(i2l(mz[i]-kz[i]))
        else:
            els.append(i2l(mz[i]))
    estr=str()
    for el in els:
        estr=estr+el
    print(estr)
def deencrypt(key="a",msg=str()):
    while len(key)<len(msg):
        key=key+key
    mletters=[mletter for mletter in msg]
    kletters=[kletter for kletter in key]
    kz=list()
    
    mz=list()
    for mletter in mletters:
        mz.append(l2i(mletter))
    for kletter in kletters:
        kz.append(l2i(kletter))
    els=[]
    for i in range(len(mz)):
        if not (mz[i]==52 or mz[i]==53 or mz[i]==54 or mz[i]==55):
            els.append(i2l(mz[i]+kz[i]))
        else:
            els.append(i2l(mz[i]))
    estr=str()
    for el in els:
        estr=estr+el
    print(estr)
