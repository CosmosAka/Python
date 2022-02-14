import hashlib


hash0 = input(f"Chose algorithm: \n1 - md5\n2 - sha1\n3 - sha224\n4 - sha256\n5 - sha384\n6 - sha512\n7 - blake2b\n8 - blake2s\n9 - sha3_224\n10 - sha3_256\n11 - sha3_384\n12 - sha3_512\n13 - shake_128\n14 - shake_256\n")


if hash0 == '1':
    md5 = input("You chose algorithm: md5\nNow, write down word or number to convert:\n")
    md5 = hashlib.md5(bytes(md5, encoding='utf-8')).hexdigest()
    print(md5)
elif hash0 == '2':
    sha1 = input("You chose algorithm: sha1\nNow, write down word or number to convert:\n")
    sha1 = hashlib.md5(bytes(sha1, encoding='utf-8')).hexdigest()
    print(sha1)
elif hash0 == '3':
    sha224 = input("You chose algorithm: sha224\nNow, write down word or number to convert:\n")
    sha224 = hashlib.sha224(bytes(sha224, encoding='utf-8')).hexdigest()
    print(sha224)
elif hash0 == '4':
    sha256 = input("You chose algorithm: sha256\nNow, write down word or number to convert:\n")
    sha256 = hashlib.sha256(bytes(sha256, encoding='utf-8')).hexdigest()
    print(sha256)
elif hash0 == '5':
    sha384 = input("You chose algorithm: sha384\nNow, write down word or number to convert:\n")
    sha384 = hashlib.sha384(bytes(sha384, encoding='utf-8')).hexdigest()
    print(sha384)
elif hash0 == '6':
    sha512 = input("You chose algorithm: sha512\nNow, write down word or number to convert:\n")
    sha512 = hashlib.sha512(bytes(sha512, encoding='utf-8')).hexdigest()
    print(sha512)
elif hash0 == '7':
    blake2b = input("You chose algorithm: blake2b\nNow, write down word or number to convert:\n")
    blake2b = hashlib.blake2b(bytes(blake2b, encoding='utf-8')).hexdigest()
    print(blake2b)
elif hash0 == '8':
    blake2s = input("You chose algorithm: blake2s\nNow, write down word or number to convert:\n")
    blake2s = hashlib.blake2s(bytes(blake2s, encoding='utf-8')).hexdigest()
    print(blake2s)
elif hash0 == '9':
    sha3_224 = input("You chose algorithm: sha3_224\nNow, write down word or number to convert:\n")
    sha3_224 = hashlib.sha3_224(bytes(sha3_224, encoding='utf-8')).hexdigest()
    print(sha3_224)
elif hash0 == '10':
    sha3_256 = input("You chose algorithm: sha3_256\nNow, write down word or number to convert:\n")
    sha3_256 = hashlib.sha3_256(bytes(sha3_256, encoding='utf-8')).hexdigest()
    print(sha3_256)
elif hash0 == '11':
    sha3_384 = input("You chose algorithm: sha3_384\nNow, write down word or number to convert:\n")
    sha3_384 = hashlib.sha3_384(bytes(sha3_384, encoding='utf-8')).hexdigest()
    print(sha3_384)
elif hash0 == '12':
    sha3_512 = input("You chose algorithm: sha3_512\nNow, write down word or number to convert:\n")
    sha3_512 = hashlib.sha3_512(bytes(sha3_512, encoding='utf-8')).hexdigest()
    print(sha3_512)
elif hash0 == '13':
    shake_128 = input("You chose algorithm: shake_128\nNow, write down word or number to convert:\n")
    shake_128 = hashlib.shake_128(bytes(shake_128, encoding='utf-8')).hexdigest()
    print(shake_128)
elif hash0 == '14':
    shake_256 = input("You chose algorithm: shake_256\nNow, write down word or number to convert:\n")
    shake_256 = hashlib.shake_256(bytes(shake_256, encoding='utf-8')).hexdigest()
    print(shake_256)
else:
    print("Sorry! Try again!")

print("Here we go! Run the program again to try one more time!")