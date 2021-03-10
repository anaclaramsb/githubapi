import pandas as pd

df1 = pd.DataFrame({'colA': [10, 20, 30],
                    'colB': [100, 200, 300]})

df2 = pd.DataFrame({'colA': [40, 20, 50],
                    'colB': [400, 200, 500]})
print(type(df1))
new_df = pd.concat([df1, df2]).drop_duplicates().reset_index(drop=True)
print(new_df)

for index, row in new_df.iterrows():
    print(row['colA'])
    print(" index " + str(index))
    print(type(index))