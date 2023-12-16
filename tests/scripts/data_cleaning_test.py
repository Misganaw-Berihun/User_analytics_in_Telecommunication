import pandas as pd
import numpy as np
import pytest

# Assuming your functions are in a module called data_processing.py
from data_processing import (
    drop_high_missing_columns,
    impute_numeric_missing,
    remove_rows_with_missing_values,
    replace_column_with_mode,
    handle_outliers,
)

@pytest.fixture
def sample_data():
    # Create a sample DataFrame for testing
    data = {
        'A': [1, 2, np.nan, 4, 5],
        'B': [np.nan, 10, 11, 12, 13],
        'C': [21, 22, 23, 24, 25],
    }
    return pd.DataFrame(data)

def test_drop_high_missing_columns(sample_data):
    result = drop_high_missing_columns(sample_data, threshold=0.2)
    assert list(result.columns) == ['C']

def test_impute_numeric_missing(sample_data):
    result = impute_numeric_missing(sample_data, columns_list=['A', 'B'], strategy='mean')
    assert result['A'].isnull().sum() == 0
    assert result['B'].isnull().sum() == 0

def test_remove_rows_with_missing_values(sample_data):
    result = remove_rows_with_missing_values(sample_data, columns_to_check=['A', 'B'])
    assert result.shape[0] == 3  # 3 rows should remain after removing rows with missing values

def test_replace_column_with_mode(sample_data):
    result = replace_column_with_mode(sample_data, column_names=['A', 'B'])
    assert result['A'].isnull().sum() == 0
    assert result['B'].isnull().sum() == 0

def test_handle_outliers(sample_data):
    result = handle_outliers(sample_data, columns=['A', 'C'], method='clip')
    assert result['A'].min() >= sample_data['A'].quantile(0.05)
    assert result['A'].max() <= sample_data['A'].quantile(0.95)
    assert result['C'].min() == sample_data['C'].min()
    assert result['C'].max() == sample_data['C'].max()
