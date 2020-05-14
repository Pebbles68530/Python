def encode():
    i = 0
    x = []
    encrypted = []

    user = input('Enter a sentence ')
    while True:
        try:
            cipher = int(input('Enter the cipher '))
            break
        except ValueError:
            print('Wrong value inputted')
    length = len(user)

    if cipher > 25:
        print ('Cipher too big')
    elif cipher <= 0:
        print ('Cipher too small')
    else:
        while i != length:
            for char in user:
                x = ord(user[i])
                x += cipher
                if x > 122:
                    x -= 26
                encrypted.append(x)
                print (chr(encrypted[i]), end='')
                i += 1
                break

def decode():
    i = 0
    x = []
    decrypted = []

    user = input('Enter the encrypted sentence ')
    while True:
        try:
            cipher = int(input('Enter the cipher '))
            break
        except ValueError:
            print ('Wrong value inputted')
    length = len(user)

    if cipher > 25:
        print ('Cipher too big')
    elif cipher <= 0:
        print ('Cipher too small')
    else:
        while i != length:
            for char in user:
                x = ord(user[i])
                x -= cipher
                if x < 97:
                    x += 26
                decrypted.append(x)
                print (chr(decrypted[i]), end=' ')
                i += 1
                break

start = input('Would you like to encode or decode? ')
start.lower()

if start == 'encode':
    encode()
elif start == 'decode':
    decode()
else:
    print('Invalid responce')