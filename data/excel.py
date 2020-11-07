import pandas as pd
import os
from pathlib import Path
from constants import WORKING_DIR

cwd = WORKING_DIR + "/data"
file = pd.read_csv(cwd + "/flag_data.csv")
print(file['name'].head(5))

lista = []

for index, country in file.iterrows():
    my_file = Path(WORKING_DIR+"/img/flags/" + country['name'] + ".png")
    if my_file.is_file():
        lista.append(country['name'])

print(lista)



