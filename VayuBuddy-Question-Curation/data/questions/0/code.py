def true_code():
    import pandas as pd
    
    df = pd.read_csv('data/raw_data/Data.csv', sep=",")
    
    data = df.groupby(['state','station'])['PM2.5'].mean()
    ans = data.idxmax()[0]
    print(ans)

true_code()