def isometric_strings(str1: str, str2: str) -> bool:
    for  x, y in zip(str1, str2):
        str1 = str1.replace(x, y)
        print(str1)
    return str1 == str2  


a = "122"
b = "453"
for x, y in zip(a,b):
    a = a.replace(x, y)
    print(a)