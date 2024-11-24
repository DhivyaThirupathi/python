from itertools import permutations
string=input("enter a string:")
permutations=[''.join(p) for p in permutations(string)]
print(f"the permutayioons of this string'{string}are")
print(str(permutations))