import json
import pickle
import numpy as np
import os

__locations = None
__data_columns = None
__model = None


def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0], 2)


def get_location_names():
    global __locations
    return __locations


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations
    global __model

    # Get the directory where this file is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Load column names
    columns_path = os.path.join(base_dir, 'artifacts', 'columns.json')
    with open(columns_path, 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 are numeric features, rest are locations

    # Load trained model
    model_path = os.path.join(base_dir, 'artifacts', 'bengalore_home_price_model.pickle')
    with open(model_path, 'rb') as f:
        __model = pickle.load(f)

    print('loading saved artifacts.....done')
    print(f"Loaded {len(__locations)} locations")


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar', 1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Vijayanagar', 1000, 2, 2))
    print(get_estimated_price('Whitefield', 1000, 2, 2))

