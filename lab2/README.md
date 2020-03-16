# Lab 2
The RSA Cryptosystem programming

### About
```
1. Generate two distinct primes, p and q. Since they can be used to generate the secret key, they must be kept hidden. 
```
```
2. Let n=pq, phi(n)=((p-1)(q-1))=1.
```
```
3. Select an integer e such that gcd(e,(p-1)(q-1)). The public key is the pair (e,n). This should be distributed widely.
```
```
4. Compute d such that de=1(mod(p-1)(q-1)). This can be done using the Pulverizer. The secret key is the pair (d,n). This should be kept hidden!
```

### Requirements
- Inputs:
```
Two prime numbers: p and q
The message to be encrypted: m
```
- Features:
```
Compute gcd(a,b)
Find values of two integers s and t using Pulverizer or the Extended Euclidean algorithm method
Compute the public and private keys
Perform encryption and decryption.
