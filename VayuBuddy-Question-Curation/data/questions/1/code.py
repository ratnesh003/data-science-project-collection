def true_code():
    import pandas as pd
    
    df = pd.read_csv('data/raw_data/Data.csv', sep=",")
    
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    
    df['Year'] = df['Timestamp'].dt.year
    df['Month'] = df['Timestamp'].dt.month
    data = df[(df['Year'] == 2020) & (df['Month'] == 8)]
    ans = data.groupby('station')['PM2.5'].max().idxmax()
    print(ans)

true_code()