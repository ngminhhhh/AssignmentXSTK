from utils.main_preprocess import *
from utils.showdata_func import *

if __name__ == "__main__":
    data = pd.read_csv("All_GPUs.csv")

    # Overview of data
    num_data = data.shape[0];
    num_features = data.shape[1];

    preprocess(data)

    # Ghi DataFrame 'data' vào file CSV mới
    data.to_csv('new_file.csv', index=True)
    
    