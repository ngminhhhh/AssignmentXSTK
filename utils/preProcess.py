from utils.preprocess.extractFunction import *
from utils.preprocess.handleMissing import *
from utils.showData import *

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

def process_missing(data, min_threshold = 5, max_threshold = 75):
    null_percent = data.isnull().mean() * 100

    low_percent_null = null_percent[null_percent < min_threshold]
    med_percent_null = null_percent[(null_percent >= min_threshold) & (null_percent <= max_threshold)]
    high_percent_null = null_percent[null_percent > max_threshold]

    handle_low_null(data, low_percent_null)
    handle_med_null(data, med_percent_null)
    handle_high_null(data, high_percent_null)

def preprocess(data):
    extract(data)
    process_missing(data)
