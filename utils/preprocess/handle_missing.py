from sklearn.linear_model import Ridge
import pandas as pd

def handle_low_null(data, threshold):
    null_percent = data.isnull().mean() * 100
    low_percent_null = null_percent[null_percent < threshold]
    data = data.dropna(subset=low_percent_null.index, inplace=True)


def handle_med_null(data, min_threshold, max_threshold):
    null_percent = data.isnull().mean() * 100
    med_percent_null = null_percent[(null_percent >= min_threshold) & (null_percent <= max_threshold)]

    for col in med_percent_null.index:
        
        if data[col].dtype in ['float64', 'int64']:
            if data[col].skew() < 1:
                data[col] = data[col].fillna(data[col].mean())
            else:
                data[col] = data[col].fillna(data[col].median())
        else:
            data[col] = data[col].fillna(data[col].mode()[0])
        
    return data


def handle_high_null(data, threshold):
    null_percent = data.isnull().mean() * 100
    high_percent_null = null_percent[null_percent > threshold] 
    
    for col in high_percent_null.index:
        data.pop(col)

    return data

