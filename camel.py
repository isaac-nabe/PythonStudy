#prompt input
camelCase = input("camelCase: ")

#search for upper case char
for char in camelCase:
    if char.isupper():
        #replace upper char with "_" + lower char
        #This is camel to snake "conversion"
        camelCase = camelCase.replace(char, "_" + char.lower())

print(camelCase)
