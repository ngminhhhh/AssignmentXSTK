import pandas as pd
import numpy as np

def chararistic_numerical_cal(data):
    numerical_data = data.select_dtypes(include=[np.number])
    stats = {
        'Mean': numerical_data.mean(),
        'Variance': numerical_data.var(),
        'Standard Deviation': numerical_data.std(),
        'Median:': numerical_data.median(),
        'Mode': numerical_data.mode().iloc[0]
    }
    return stats
