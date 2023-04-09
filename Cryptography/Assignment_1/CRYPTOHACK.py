import sys
import base64
from crypto.Util.number import *
from pwn import *
import function

# Second_Problem ******
# if sys.version_info.major == 2:
#     print("You are running Python 2, which is no longer supported. Please update to Python 3.")
#
# ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]
#
# print("Here is your flag:")
# print("".join(chr(o ^ 0x32) for o in ords))

# Third_Problem
# l=[99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
# flag=""
# for i in range(len(l)):
#     flag+=chr(l[i])
# print(flag)

# Fourth_Problem ******
# C="63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
# print(bytes.fromhex(C).decode())

# Fifth_Problem
# C=bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
# print(base64.b64encode(C).decode())

# Sixth_problem ******
# C=11515195063862318899931685488813747395775516287289682636499965282714637259206269
# print(long_to_bytes(C).decode())

# Seventh_Problem ******
# x="label"
# key=""
# for i in range(len(x)):
#     ASCII=int(ord(x[i]))
#     key+=xor(ASCII,13).decode()
#
# print(key)

# Eighth problem ******
# key1=bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
# x=bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
# key2=xor(x,key1)
# x=bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
# key3=xor(x,key2)
# x=bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
# flag=xor(x,key1,key2,key3)
# print(flag.decode())

# Ninth_Problem ******
# C=bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
# check=1
# for x in range(256):
#     flag = ""
#     for i in range(len(C)):
#         flag+=xor(C[i],x).decode()
#         if i==5 and flag != "crypto":
#             break
#         elif i==5 and flag == "crypto":
#             check=0
#     if check==0:
#         b=x
#         break
# print(flag)
