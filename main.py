import re
import pandas as pd


with open('123Done.txt', 'r', encoding = 'Latin-1') as myfile:
    data = myfile.read()

    match = re.findall(r'('To:(.*?)Subject:',fin)', data)
    match = set(match)
    match = list(match)

    df = pd.DataFrame(match, columns=['Address'])
    df = df.sort_values(by=['Address'])
    df.to_csv("emailsadresses4.csv", index=False)




