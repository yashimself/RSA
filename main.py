import random
import gen_prime
import time


def genkeys(p1, p2):
    # Generating Public key
    n = p1 * p2
    phi = (p1 - 1) * (p2 - 1)
    r = random.randint(2, 100)  # For efficiency 2 < e < 100
    while True:
        if gcd(r, phi) == 1:
            break
        else:
            r += 1
    e = r

    # Generating Private key

    # k = random.randrange(1, 10)
    d = modinv(e, phi)
    return n, d, e


def gcd(a, b):  # Finding GCD
    while b:
        a, b = b, a % b
    return a


# function to find modular inverse
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


# function to find extended gcd
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


# Encrypting details
def encrypt(plaintext, n, e):
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher


# Decrypting details
def decrypt(cipher, d, n):
    msg = [chr((char ** d) % n) for char in cipher]
    return ''.join(msg)


if __name__ == '__main__':
    p1 = gen_prime.genprime()
    p2 = gen_prime.genprime()
    # print("First prime: ", p1, "\nSecond prime: ", p2)
    n, d, e = genkeys(p1, p2)
    print("\nGenerating unique prime numbers for you. Please wait...")
    time.sleep(1)
    print("\nGenerating keys...")
    time.sleep(1)
    print("\n***Public key is: ", n, "and e= ", e, "***", "\n***Private key is: ", d, "***")
    pub = open('public_key.txt', 'w')
    priv = open('private_key.txt', 'w')
    publick = "n= " + str(n) + "e= " + str(e)
    pub.writelines(publick)
    priv.writelines(str(d))
    pub.close()
    priv.close()
    print("\n\n***Your public key and private key are successfully stored in files 'public_key.txt' and "
          "'private_key.txt' respectively***")
    time.sleep(3)
    plaintext = input("\nEnter card details: ")
    encrypted_msg = encrypt(plaintext, n, e)
    print("Encrypted string is: ", ''.join(map(lambda x: str(x), encrypted_msg)))
    c = input("Do you want to decrypt the string using private key? (Y/n)")
    if c == 'Y' or c == 'y':
        print("\nDecrypting...")
        time.sleep(1)
        decrypted_text = decrypt(encrypted_msg, d, n)
        print("\nDecrypted details are: ", decrypted_text)
    print("\n\n<---RSA demonstrated successfully--->")
