import pathlib 

print(str(pathlib.Path().cwd()))  # Prints the path to your current working directory

import pathlib
path = pathlib.Path().cwd()
str(path)
for filepath in path.iterdir():
    print(filepath.name)


