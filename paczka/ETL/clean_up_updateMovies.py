import glob
from zipfile import ZipFile
from datetime import date
import os

def rename_file(filename):
    return "{0}_{2}.{1}".format(*filename.rsplit('.', 1) + [date.today().strftime('%Y-%m-%d')])



filenames = glob.glob("C:\\Users\\adria\\Desktop\\semestr_6\\Hurtownie danych\\projekt\\ETL\\UpdateData\\*.csv")

zipObj = ZipFile(f'C:\\Users\\adria\\Desktop\\semestr_6\\Hurtownie danych\\projekt\\ETL\\Archive\\movies_update_{date.today().strftime("%Y-%m-%d")}.zip', 'w')


for filename in filenames:
    os.rename(filename, rename_file(filename))
    zipObj.write(rename_file(filename), filename.split('\\')[-1])
    os.remove(rename_file(filename))
zipObj.close()