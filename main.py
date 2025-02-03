import random

lower = "abcdefghijklmnopqrstuvwxyz"
uper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%¨^&*().'"

string = lower + uper + numbers + symbols
length = 16
password = "".join(random.sample(string,length))
print("your password is:" + password)
