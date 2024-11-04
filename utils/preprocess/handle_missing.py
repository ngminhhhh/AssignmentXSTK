from sklearn.ensemble import RandomForestRegressor
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


def handle_high_null(data, threshold):
    null_percent = data.isnull().mean() * 100
    high_numeric_null = null_percent[(null_percent > threshold) & (data.dtypes.isin(['float64', 'int64']))]
    # high_object_null = null_percent[(null_percent > threshold) & ~(data.dtypes.isin(['float64', 'int64']))]

    for col in high_numeric_null.index:

        data_with_values = data[data[col].notnull()]
        data_with_nulls = data[data[col].isnull()]

        X_train = data_with_values.drop(columns=[col])
        y_train = data_with_values[col]
        
        X_train = X_train.select_dtypes(include=['float64', 'int64'])
        X_test = data_with_nulls.drop(columns=[col]).select_dtypes(include=['float64', 'int64'])
        
        model = RandomForestRegressor(random_state=0, n_estimators=100)
        model.fit(X_train, y_train)
        
        predicted_values = model.predict(X_test)
        
        data.loc[data[col].isnull(), col] = predicted_values

    # for col in high_object_null:
    #     data[col] = data[col].fillna(data[col].mode()[0])


