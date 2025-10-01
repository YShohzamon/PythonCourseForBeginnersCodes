from pathlib import Path

path = Path("functions")
print(path.exists())
path2 = Path("emails")
# path2.mkdir()
# path2.rmdir()
path3 = Path()

for file in path3.glob("*"):
    print(file)