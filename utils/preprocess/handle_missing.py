import pandas as pd

def handle_low_null(data, low_percent_null):
    data = data.dropna(subset=low_percent_null.index, inplace=True)

    
def handle_med_null(data, med_percent_null):
    for col in med_percent_null.index:
        
        if data[col].dtype in ['float64', 'int64']:
            if data[col].skew() < 1:
                data[col] = data[col].fillna(data[col].mean())
            else:
                data[col] = data[col].fillna(data[col].median())
        else:
            data[col] = data[col].fillna(data[col].mode()[0])
        


def handle_high_null(data, high_percent_null):
    for col in high_percent_null.index:
        data.pop(col)

