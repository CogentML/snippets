import pandas as pd

def dataframe_to_dict(df):
    my_dict = {}
    for col in df.columns:
        my_dict[col] = df[col].tolist()
    return my_dict

# Example usage
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6], 'col3': [7, 8, 9]})
my_dict = dataframe_to_dict(df)
print(my_dict)


