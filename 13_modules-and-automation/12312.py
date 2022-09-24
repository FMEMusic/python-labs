import pathlib

a= pathlib.Path()
path = str(a)

for filepath in a.iterdir():
    print(filepath.name)



