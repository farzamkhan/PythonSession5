import hashlib
MyHashList = {}
my_input = None
while my_input != "exit" :
    my_input = input ("Enter your text:")
    if my_input != "exit":
        MyHashList.update({my_input : hashlib.md5(my_input.encode())})
        MyHashList.update({my_input+'_un' : my_input})

print("=======================================")

YourReq =str(input ("Enter your Req :"))
if YourReq == "exit":
    print()
elif YourReq == "all":
    print(MyHashList)
else: 
    YourModel = str(input("Enter your model :"))
    if YourModel == "md5":
        print(MyHashList[YourReq])
    elif YourModel == "string" :
        print(MyHashList[YourReq+'_un'])



