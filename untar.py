
print('The Great Tarzaar')

import tarfile
name = ('name')
name = str(name)
for file in range(1000,0,-1):
    file = str(file)
    name=(file) + (".tar")
    print('Working on file ' + name + ' right now.')
    tar=tarfile.open(name)
    tar.extractall()
    print('Extracted file.')
    tar.close