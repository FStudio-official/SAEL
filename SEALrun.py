import SEALdefs
while True:
    io=input("Verschlüsseln oder Entschlüsseln (V/E)? ")
    io=io.lower()
    if io=="v":
        msg=input("Nachricht: ")
        key=input("Schlüssel: ")
        SEALdefs.encrypt(key,msg)
    elif io=="e":
        msg=input("Verschlüsselte Nachricht: ")
        key=input("Schlüssel: ")
        SEALdefs.deencrypt(key,msg)