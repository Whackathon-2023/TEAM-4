import pandas as pd
# df = pd.read_excel("data.xls")
df = pd.read_excel("complete_movement.xls")

competitiors = ['Nutrien', 'Summit', 'CBH']
areas = [['Kwinana'], ['Albany','Bunbury','Esperance'], ['Geraldton']]
for a in areas:
    for p in a:
        mask1 = df[df['From Location'].str.contains(p)]['From Location']
        mask2 = df[df['To Location'].str.contains(p)]['To Location']
        print(mask1)
        print(mask2)