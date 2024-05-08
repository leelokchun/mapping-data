import os
dict = {}
for root, directory, files in os.walk(r'D:\Download\Notes'):
    for file in files:
        fullpath = os.path.join(root, file)
        size = os.path.getsize(fullpath)
        dict[fullpath] = size

for path, size in dict.items():
    if size < 100000:
        print(f'Path: {path}, Size: {size}')
