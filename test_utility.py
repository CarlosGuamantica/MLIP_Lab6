import pytest
import pandas as pd
import numpy as np
from prediction_demo import data_preparation, data_split, train_model, eval_model

# Fixture de muestra con solo 2 filas (toy dataset)
@pytest.fixture
def housing_data_sample():
    return pd.DataFrame(
        data={
            'price': [13300000, 12250000],
            'area': [7420, 8960],
            'bedrooms': [4, 4],
            'bathrooms': [2, 4],
            'stories': [3, 4],
            'mainroad': ["yes", "yes"],
            'guestroom': ["no", "no"],
            'basement': ["no", "no"],
            'hotwaterheating': ["no", "no"],
            'airconditioning': ["yes", "yes"],
            'parking': [2, 3],
            'prefarea': ["yes", "no"],
            'furnishingstatus': ["furnished", "unfurnished"]
        }
    )

# Prueba para verificar que data_preparation separe bien los features y el target
def test_data_preparation(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)

    # Mismo número de filas
    assert feature_df.shape[0] == len(target_series)

    # Solo columnas numéricas en feature_df
    assert feature_df.shape[1] == feature_df.select_dtypes(include=(np.number, np.bool_)).shape[1]

# Fixture que aplica data_preparation para luego usar en el split
@pytest.fixture
def feature_target_sample(housing_data_sample):
    feature_df, target_series = data_preparation(housing_data_sample)
    return (feature_df, target_series)

# Prueba para verificar que data_split funcione bien
def test_data_split(feature_target_sample):
    return_tuple = data_split(*feature_target_sample)

    # Verifica que devuelva una tupla con 4 elementos
    assert isinstance(return_tuple, tuple)
    assert len(return_tuple) == 4

    X_train, X_test, y_train, y_test = return_tuple

    # Verifica que el total de datos se mantenga
    assert len(X_train) + len(X_test) == 2
    assert len(y_train) + len(y_test) == 2

    # Asegura que no haya traslape entre train y test
    assert set(X_train.index).isdisjoint(X_test.index)
    assert set(y_train.index).isdisjoint(y_test.index)
