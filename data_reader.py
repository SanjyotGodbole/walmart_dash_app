import pandas as pd
from pathlib import Path 

p = Path('./data/')

# print(list(p.glob('*.csv')))
# print(list(p.glob('*.csv')))

l = list(p.glob('*.csv'))
data_dict={}
for f in l:
    # print(f.parts[-1])
    filename=f.parts[-1]
    dfname = filename.split('.')[0]
    data_dict[dfname] = pd.read_csv(f,index_col=False)
    # print(data_dict)
# pd.read_csv('')

print(data_dict['ssd22'])
