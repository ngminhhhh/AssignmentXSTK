from utils.preprocess.extract_func import *
from utils.preprocess.handle_missing import *
from utils.show_data_func import *

def extract(data):
    split_resolution(data, 'Best_Resolution')
    split_resolution(data, 'Resolution_WxH')
    split_PSU(data, 'PSU')

    erase_unit(data, 'Boost_Clock')
    erase_unit(data, 'Core_Speed')
    erase_unit(data, 'Max_Power')
    erase_unit(data, 'Memory')
    erase_unit(data, 'Memory_Bandwidth')
    erase_unit(data, 'Memory_Bus')
    erase_unit(data, 'Memory_Speed')
    erase_unit(data, 'Pixel_Rate')
    erase_unit(data, 'Process')
    erase_unit(data, 'Release_Price')
    erase_unit(data, 'Texture_Rate')

    split_cores(data, 'L2_Cache', 'L2')
    split_cores(data, 'ROPs', 'ROPs')

    data['Release_Date'] = pd.to_datetime(data['Release_Date'], errors='coerce')

def process_missing(data, min_threshold = 5, max_threshold = 20):
    handle_low_null(data, min_threshold)
    handle_med_null(data, min_threshold, max_threshold)
    data = handle_high_null(data, max_threshold)

def preprocess(data):
    extract(data)
    process_missing(data)
