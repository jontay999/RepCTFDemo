
from libnum import *
from Crypto.Util.number import getPrime

"""
RSA uses two keys: a public key that anyone can see and use to send you messages, and a private key that you keep secret and use to decrypt those messages. This is known as asymmetric cryptography because it uses two different keys.
"""

def encrypt():
    flag = b"XXXXXXXXXXX"
    p = getPrime(512)
    q = getPrime(512)
    print(f"{p = }")
    """
    The security of RSA relies on the difficulty of factoring large numbers into their prime components. For example, if you multiply two large prime numbers together, it's easy to get a big number, n, but figuring out which 2 prime numbers were used to generate n is very hard
    """

    # generate your public key
    n = p * q 

    # very common exponent
    e = 2** 16 + 1

    # convert the message from bytes to a number
    m = s2n(flag)

    # you encrypt the message by raising the message to the power of e modulo n
    ct = pow(m,e,n)

    print(f"{n = }")
    print(f"{ct = }")

"""
p = 10679836458193430143497830678162134396048826551887301756213249378863439811922766020344465956518031765349655939523561844892470541276671444733334746032468467
n = 87478637825049284727797834682079248191065978488072748983687134963405597866480664828226255741254655124571681226423968094449113412167498790497232185547760588196064878153905593693588426932934223845156669470233205397947126838002959429121453082953732700969297370557587340519957256994580604093279296972548277423869
ct = 63531691078371858281567702822190147653832427723582395946481329983029728445539975027729903136437268183962892375471384757719441539044586890445989039281610890047988717953346249961623178920299920138132141612821510179905023318395480335786379777584489317089693432932106513590853841935895443700407311590706210875250
"""

def decrypt(prime1, prime2, ciphertext, n):
    # ensure that you have the factorization of n
    assert prime1 * prime2 == n
    # phi = the totient function (can go learn if you want)
    phi = (prime1-1) * (prime2-1)
    e = 2** 16 + 1

    # this raises the exponent to the inverse of phi
    d = pow(e,-1, phi)
    msg = pow(ciphertext, d, n)

    # Now you need to convert the number back into a string
    decrypted_msg = n2s(msg)
    print(decrypted_msg)

# decrypt(?,?,?,?)