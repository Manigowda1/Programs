import pandas as pd
with open('C:/Users/HP/OneDrive/Desktop/Mani.text','w') as f:
    df = pd.read_csv('C:/Users/HP/OneDrive/Desktop/Mani.csv', low_memory=True)
    print(df)
    f.write(df)





