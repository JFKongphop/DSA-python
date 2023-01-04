#Stack Exercise 1: Creating Stack using list Built-in --> List Functions

cpLanguages = ['Python', 'C', 'Java', 'C++', 'C#', 'R', 'Javascript', 'PHP', 'Go', 'Swift', 'Python', 'Java', 'Python']

pythonCount = cpLanguages.count('Python')
print(pythonCount)
assemblyCount = cpLanguages.count('Assemply')
print(assemblyCount)
javaCount = cpLanguages.count('Java')
print(javaCount)
pythonIndex = cpLanguages.index('Python')
print(pythonIndex)
pythonIndex2 = cpLanguages.index('Python', 4) # key word to count with the starting index
print(pythonIndex2)
cpLanguages.reverse()
print(cpLanguages)
cpLanguages.sort(key=len)
print(cpLanguages)