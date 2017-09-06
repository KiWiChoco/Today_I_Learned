import os
import glob

print(os.getcwd())

print(os.listdir('.'))

print(os.path.isfile(r'C:\\Users\\User\\Desktop\\Family_Song.zip'))

print(glob.glob("C:\\Users\\User\\*\\q*"))

pyfiles = glob.iglob('*.py')
for pyfile in pyfiles:
    print(pyfile)

