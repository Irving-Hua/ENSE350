'''

The RSA Cryptosystem

350 - Lab Assignment #2
Jiahao Li(200368215)

The receiver creates a public key and a secret key as follows.
1.	Generate two distinct primes,   and . Since they can be used to generate the secret key, they must be kept hidden.
2.	Let   , phi(n) = ((p-1)*(q-1))
3.	Select an integer   such that . The public key is the pair . This should be distributed widely.
4.	Compute   such that . This can be done using the Pulverizer. The secret key is the pair . This should be kept hidden!

Encoding:
Given a message , the sender ﬁrst checks that . The sender then encrypts message m to produce   using the public key:

Decoding:
The receiver decrypts message   back to message   using the secret key:

'''

import random

'''
Using Euclidean Algorithm to find gcd(a,b)
'''
def gcd(a,b):
    while b!= 0:
        a,b = b, a % b
    return a

'''
Using Extended Euclidean Algorithm to find multiplicative inverse of two numbers
'''
def multi_inverse(e, phi):
    #
    x1 = 0
    x2 = 1
    y1 = 1
    d = 0
    temp = phi

    while e > 0:
        #get the quotient
        temp1 = temp // e
        #calculate (next) temp(s)
        temp2 = temp - temp1 * e
        temp = e
        e = temp2

        #calculate (next) temp(t)
        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

        #Until remainder is 1
        if temp == 1:
            return d + phi


'''
Generate two distinct primes, but we need to check whether is prime
Compute totient of n: phi(n) = ((p-1)*(q-1))
'''
def generate_key_pair(p, q):
    if p ==q:
        print("Can not be equal.")
    elif not (is_prime(p) and is_prime(q)):
        print("Numbers should be primes.")

    n = p * q
    phi = (p-1) * (q-1)
    e = random.randrange(1, phi)
    co_prime = gcd(e, phi)
    while co_prime != 1:
        e = random.randrange(1, phi)
        co_prime = gcd(e, phi)

    d = multi_inverse(e, phi)

    return (e, n), (d, n)

#check input numbers wether primes
def is_prime(num):
    if num == 2:
        return True
    elif num < 2 or num % 2 == 0:
        return False

    for n in range(3, int(num ** 0.5) + 2, 2):
        if num % n == 0:
            return False
    return True

'''
Encoding process
Encrypt a message m using public key
'''
def encryption(public_key, plaintext):
    key, n = public_key
    cipher = [pow(ord(char),key,n) for char in plaintext]
    return cipher

'''
Decoding process
Decrypt a message m using private key
'''
def decryption(public_key, ciphertext):
    key, n = public_key
    plain = [chr(pow(char,key,n)) for char in ciphertext]

    return "".join(plain)


if __name__ == '__main__':
    print("The RSA Cryptosystem Program")

    p = int(input("Enter a prime number for p:\n "))
    q = int(input("Enter another prime number for q:\n "))

    public_key, private_key = generate_key_pair(p, q)
    print("The generated public and private key pairs are: ")
    print(str(public_key) + " , " + str(private_key))
    print("\n")

    message = input("Enter a message that to be encrypted:\n ")
    encrypted_message = encryption(private_key, message)
    print("The encrypted message is:")
    print ("".join(map(lambda x: str(x), encrypted_message)))
    print("\n")

    print("Using the public key " + str(public_key) + " to decrypt the encrypted message...")
    decrypted_message = decryption(public_key, encrypted_message)
    print("The decrypted message is: " + decrypted_message)
    print("\n")
    print("Encryption/Decryption program is done!")