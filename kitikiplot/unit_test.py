"""
------------------------------------------------------------------------------
File: unit_test.py
Description: This file contains test cases for the KitikiPlot class, ensuring 
             its functionality across different data types and edge cases.
Created On: March 22, 2025
------------------------------------------------------------------------------
"""

""" Import necessary libraries """
import pytest
import pandas as pd
import matplotlib.patches as mpatches
from kitikiplot import KitikiPlot

""" Fixtures for providing sample data """

@pytest.fixture
def sample_data():
    """ 
    Returns a sample Pandas DataFrame for testing.
    """
    return pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

@pytest.fixture
def sample_list():
    """ 
    Returns a sample list for testing list-based initialization.
    """
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.fixture
def kitiki_plot(sample_data):
    """ 
    Creates an instance of KitikiPlot using sample data.
    """
    return KitikiPlot(data=sample_data)

@pytest.fixture
def cmap():
    """ 
    Returns a colormap dictionary for testing color mapping.
    """
    return {0: {1: "red", 2: "blue", 3: "green"}, 1: "black"}

@pytest.fixture
def hmap():
    """ 
    Returns a hatch map dictionary for testing hatch patterns.
    """
    return {1: "//", 2: "\\", 3: "||"}

""" Testing Initialization with Different Data Types """

def test_kitiki_plot_initialization(sample_data):
    """ 
    Tests if KitikiPlot initializes properly with a DataFrame. 
    """
    plot = KitikiPlot(data=sample_data)
    assert isinstance(plot, KitikiPlot)

def test_kitiki_plot_with_empty_dataframe():
    """ 
    Tests if KitikiPlot initializes properly with an empty DataFrame. 
    """
    empty_df = pd.DataFrame()
    plot = KitikiPlot(data=empty_df)
    assert isinstance(plot, KitikiPlot)

def test_kitiki_plot_with_list(sample_list):
    """ 
    Tests if KitikiPlot initializes properly with a list.
    """
    plot = KitikiPlot(data=sample_list, stride=2, window_length=5)
    assert isinstance(plot, KitikiPlot)

def test_kitiki_plot_with_nested_list():
    """ 
    Tests if KitikiPlot initializes properly with a nested list. 
    """
    nested_list = [[1, 2], [3, 4], [5, 6]]
    plot = KitikiPlot(data=nested_list, stride=1, window_length=2)
    assert isinstance(plot, KitikiPlot)

""" Testing Edge Cases for 'create' Method """

def test_create_rectangle(kitiki_plot, cmap, hmap):
    """ 
    Tests if the 'create' method generates a valid rectangle object.
    """
    rect = kitiki_plot.create(
        x=0, y=0, each_sample=[1, 2, 3], cell_width=0.5, cell_height=2.0, 
        window_gap=1.0, align=True, cmap=cmap, edge_color='black', 
        fallback_color='white', hmap=hmap, fallback_hatch=' ', 
        display_hatch=True, transpose=False
    )
    assert isinstance(rect, mpatches.Rectangle)

def test_create_invalid_rectangle(kitiki_plot, cmap, hmap):
    """ 
    Tests if the 'create' method raises a KeyError for missing cmap/hmap values. 
    """
    with pytest.raises(KeyError):  
        kitiki_plot.create(
            x=0, y=0, each_sample=[10], cell_width=0.5, cell_height=2.0, 
            window_gap=1.0, align=True, cmap=cmap, edge_color='black', 
            fallback_color='white', hmap=hmap, fallback_hatch=' ', 
            display_hatch=True, transpose=False
        )

def test_create_rectangle_with_unknown_values(kitiki_plot, cmap, hmap):
    """ 
    Tests if the 'create' method raises a KeyError for unknown cmap/hmap values.
    """
    with pytest.raises(KeyError):
        kitiki_plot.create(
            x=0, y=0, each_sample=[99], cell_width=0.5, cell_height=2.0,
            window_gap=1.0, align=True, cmap=cmap, edge_color='black',
            fallback_color='white', hmap=hmap, fallback_hatch=' ',
            display_hatch=True, transpose=False
        )
