import pandas as pd
data = {'name': ['mohamed','ahmed', 'ali'],
        'sales': [300, 800, 500],
        'city': ['bahri', 'khartoum', 'omdrman']}
df = pd.DataFrame(data)
print(df)
print("------")
print(df['sales'].sum()) 