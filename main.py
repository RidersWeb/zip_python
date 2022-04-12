import os
from zipfile import ZipFile

def zip(path, zipname):
    with ZipFile(zipname, 'w') as myzip:
        if os.path.isfile(path):
            myzip.write(path)
        else:
            for root, dirs, files1 in os.walk(path):
                for file in files1:
                    myzip.write(f'{root}/{file}')

zip('img', "newzip.zip")