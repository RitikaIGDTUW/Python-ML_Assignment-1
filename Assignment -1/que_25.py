sourcefile='text1.txt'
destination='text2.txt'
with open(sourcefile, 'r') as src:
        contents = src.read()
with open(destination, 'w') as dest:
        dest.write(contents)        