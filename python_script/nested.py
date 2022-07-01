d = {"a":{"b":{"c":"d"}}} # we can also ask user to give  input like below and can be validated by writing some try catch blocks

#str1 = input("Enter key values pairs: ")
#d1 = dict(x.split() for x in str1.splitlines())
#print(d1)
key = []
value = []
def rec1(d,key,value):
    for k, v in d.items():
        key.append(k)
        if isinstance(v, dict):
            rec1(v,key,value)
        else:
            value.append(v)
rec1(d, key, value)
print(key)
print(value)