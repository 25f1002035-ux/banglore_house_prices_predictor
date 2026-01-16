import json
import pickle
import numpy as np
import os
import warnings
warnings.filterwarnings("ignore", message="X does not have valid feature names")


__locations = None
__data_columns = None
__model = None
def print_all_locations():
    """Print numbered list of all locations"""
    return __locations
# Call in __main__
def predict_price(location,sqft,bath,bhk):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1
    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)





def get_location_names():
    # Lazy load if not yet loaded
    global __locations
    if __locations is None:
        load_saved_artifacts()
    # Fallback to empty list so len() is always safe
    return __locations or []


def load_saved_artifacts():
    global __data_columns, __locations, __model
    print("Loading saved artifacts...start")
    try:
        with open("./artefacts/columns.json", "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]
        with open("./artefacts/banglore_home_prices_model.pickle", "rb") as f:
            __model = pickle.load(f)
        print("Loading saved artifacts...done")
        print(f"📍 Loaded {len(__locations)} locations: {__locations[:240]}...")
    except Exception as e:
        print(f"Load error: {e}")
        __locations = []      # prevent None
        __model = None        # optional safety


if __name__ == "__main__":
    load_saved_artifacts()
    print_all_locations()
    print(predict_price("anekal",1000,2,2))
    print(predict_price("Kalhalli", 1000, 2, 2))
