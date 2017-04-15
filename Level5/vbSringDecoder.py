
gc000A = "http://www.try2hack.nl/levels/level6-ksghvb.xhtml"
gc0006 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,:;-*+=~|&!_$#@()[]{}<\/>"


def decode_func(string, index, length):
    if index != 0:
        index -= 1
    return string[index:index+length]

base_url = decode_func(gc000A, 0, 37)
decoded = decode_func(gc0006, 21, 1)
decoded += decode_func(gc0006, 14, 1)
decoded += decode_func(gc0006, 29, 1)
decoded += decode_func(gc0006, 32, 1)
decoded += decode_func(gc0006, 12, 1)
decoded += decode_func(gc0006, 14, 1)
decoded += decode_func(gc000A, 44, 7)

username = decode_func(gc0006, 56, 1)
username += decode_func(gc0006, 28, 1)
username += decode_func(gc0006, 35, 1)
username += decode_func(gc0006, 3, 1)
username += decode_func(gc0006, 44, 1)
username += decode_func(gc0006, 11, 1)
username += decode_func(gc0006, 13, 1)
username += decode_func(gc0006, 21, 1)

password = decode_func(gc0006, 45, 1)
password += decode_func(gc0006, 48, 1)
password += decode_func(gc0006, 25, 1)
password += decode_func(gc0006, 32, 1)
password += decode_func(gc0006, 15, 1)
password += decode_func(gc0006, 40, 1)
password += decode_func(gc0006, 25, 1)
password += decode_func(gc0006, 14, 1)
password += decode_func(gc0006, 19, 1)


print("Username: {0}".format(username))
print("Password: {0}".format(password))
print(base_url + decoded)
