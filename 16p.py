dic={"b":20, "a":35}
# problem a
dic["b"] = -dic["b"]
print("Replace the value at the key “b” in data with that value’s negation.",dic)
#problem b
dic["c"]=40
print("Add the key/value pair “c”:40 to data.",dic)
#problem c
print("Print the keys in data in alphabetical order")
for key in sorted(dic.keys()):
    print(key)
#problem d
dic.pop("b", None)
print("Remove the value at key “b” in data, safely.",dic)
