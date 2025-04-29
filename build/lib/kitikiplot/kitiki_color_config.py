"""
File Name: kitiki_color_config.py
Description: This file defines the 'ColorConfig' class for managing input data(list, dataframe) and configuring color, hatch of KitikiPlot
Author: Boddu Sri Pavan
Date Created: 21-10-2024
Last Modified: 29-04-2025
"""

# Import necessary libraries
from typing import Tuple, Union, Dict
import random
import math
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import gc

class ColorConfig:
    """
    Configure data, color, and hatch settings for KitikiPlot visualization.

    Parameters
    ----------
    data : pd.DataFrame or list or str
        - The input data which can be either a pandas DataFrame or a list or a str.
        - If a list is provided, it will be converted into a DataFrame using specified stride and window length.
    stride : int (optional)
        - The number of elements to move the window after each iteration when converting a list to a DataFrame. 
        - Default is 1.
    window_length : int (optional)
        - The length of each window when converting a list to a DataFrame.
        - Default is 10.

    Attributes
    ----------
    data : pd.DataFrame
        - The DataFrame containing the input data.
    stride : int
        - The number of elements to move the window after each iteration when converting a list to a DataFrame.
        - Default is 1.
    rows : int
        - The number of rows in the DataFrame.
    cols : int
        - The number of columns in the DataFrame.

    Methods
    -------
    Instance Methods
        - color_config: Configure colors for unique values in the DataFrame.
        - hatch_config: Configure hatch patterns for unique values in the DataFrame.
        - unique_config: Find unique values and their count from the input DataFrame.
    
    Static Methods
        - _convert_list_to_dataframe: Convert a list into a pandas DataFrame using sliding window.
    """

    def __init__(self, data: Union[pd.DataFrame, list, str], stride: int = 1, window_length: int = 10) -> None:
        """
        Initialize the ColorConfig object with data and optional parameters.
        Also checks the type of input data and initializes the corresponding attributes.
        
        Parameters
        ----------
        data : pd.DataFrame or list or str
            - The input data to be processed.
        stride : int (optional)
            - The number of elements to move the window after each iteration when converting a list to a DataFrame. 
            - Default is 1.
        window_length : int (optional)
            - The length of each window when converting a list to a DataFrame. 
            - Default is 10.

        Attributes
        ----------
        stride : int
            - The number of elements to move the window after each iteration when converting a list to a DataFrame.
            - Default is 1.
        """

        # Check if 'data' is of type 'pd.DataFrame' and initialize 'data' attribute.
        if isinstance( data, pd.DataFrame):
            self.data= data

        # Check if 'data' is of type 'list'.
        elif isinstance( data, list):

            # Convert 'list' to 'pd.DataFrame' using stride and window_length, and initialize 'data' attribute.
            self.data= self._convert_list_to_dataframe( data, stride, window_length)

        elif isinstance( data, str):

            # Convert 'list' to 'pd.DataFrame' using stride and window_length, and initialize 'data' attribute.
            self.data= self._convert_list_to_dataframe( list(data), stride, window_length)

        # Store the stride value
        self.stride= stride

        # Set 'rows' to number of rows in the DataFrame.
        self.rows= self.data.shape[0]

        # Set 'cols' to number of columns in the DataFrame.
        self.cols= self.data.shape[1]

    @staticmethod
    def _convert_list_to_dataframe( data: Union[pd.DataFrame, list], stride: int = 1, window_length: int = 10) -> pd.DataFrame:
        """
        Convert list into a 'pd.DataFrame' by creating sliding window of specified window length.

        Parameters
        ----------
        data : pd.DataFrame or list
            - The input data to be processed.
        stride : int (optional)
            - The number of elements to move the window after each iteration when converting a list to a DataFrame. 
            - Default is 1.
        window_length : int (optional)
            - The length of each window when converting a list to a DataFrame. 
            - Default is 10.

        Returns
        -------
        pd.DataFrame: A DataFrame containing the sliding window of data.
        """

        # Calculate the number of rows needed in the DataFrame
        n_rows= math.ceil(max(len(data)-window_length, 0)/ stride +1)

        # Initialize an empty list to hold the rows of data
        l= []

        # Generate each row based on the sliding window approach
        for i in range( n_rows ):

            # Extract a slice from the data based on current stride and window length
            row_data= data[i*stride: i*stride+window_length]

            # If the extracted row is shorter than the window length, pad it with "No_Data"
            if len(row_data)< window_length:
                row_data+= ["No_Data"]* (window_length- len(row_data))
            
            # Append the row to the list
            l.append( row_data )
        
        # Clean up all local variables for efficient memory management
        # del n_rows, data, window_length, stride, i, row_data
        locals().clear()
        
        # Trigger garbage collection for efficient memory management
        gc.collect()

        # Convert the list of rows into a 'pda.DataFrame' and return it
        return pd.DataFrame( l )

    def unique_config(self) -> Tuple[np.ndarray, int]:
        """
        Find unique values and no.of unique values from input DataFrame.

        Returns
        -------
        tuple: (unique_values, n_unique)
            unique_values : numpy.ndarray
                - Array of unique values present in the input DataFrame.
            n_unique : int
                - Number of unique values present in the input DataFrame.
        """

        # Extract unique values from the input DataFrame by flattening it
        unique_values= pd.unique( self.data.values.ravel())

        # Calculate the number of unique values found in the DataFrame
        n_unique= unique_values.shape[0]

        # Trigger garbage collection for efficient memory management
        gc.collect()

        # Return both the array of unique values and their count
        return unique_values, n_unique

    def color_config(self, cmap: Union[str, Dict], edge_color: str, fallback_color: str) -> Tuple[Dict, str]:
        """
        Configure colors for unique values in the DataFrame.

        Parameters
        ----------
        cmap : str or dict
            - If a string, it should be a colormap name to generate colors.
            - If a dictionary, it should map unique values to specific colors.
            - Default is 'rainbow'.
        edge_color : str
            - The color to use for the edges of the rectangle.
            - Default is '#000000'.
        fallback_color : str
            - The color to use as fallback if no specific color is assigned.
            - Default is '#FAFAFA'.

        Returns
        -------
        tuple: (color_map, edge_color)
            color_map : dict
                - A dictionary mapping unique values to their corresponding colors.
            edge_color : str
                - The specified edge color.
        """

        # Find unique values and their count from the input DataFrame
        unique_values, n_unique= self.unique_config()

        # Check if cmap is a string representing a colormap name
        if type(cmap)== str:
            
            # Get the colormap and create a custom palette based on the number of unique values
            cmap = plt.get_cmap( cmap, n_unique)
            custom_palette = [matplotlib.colors.rgb2hex(cmap(i)) for i in range(cmap.N)]

            # Create a mapping of unique values to their corresponding colors
            color_map= dict(zip(unique_values, custom_palette))

        # Check if cmap is a dictionary
        elif type(cmap)==dict:

            color_map= cmap

            # Ensure all unique values are represented in the color_map
            if len(cmap)!= n_unique:
                for each_unique in unique_values:
                    if each_unique not in color_map:

                        # Assign fallback color for any missing unique value
                        color_map.update( {each_unique: fallback_color} )

        # Clean up all local variables for efficient memory management
        # del unique_values, n_unique, cmap, custom_palette, i
        locals().clear()

        # Trigger garbage collection for efficient memory management
        gc.collect()

        # Return the final color mapping and the specified edge color
        return color_map, edge_color
    
    def hatch_config(self, h_map: Dict, fallback_hatch: str, display_hatch: bool) -> dict:
        """
        Configure hatch patterns for unique values in the DataFrame.

        Parameters
        ----------
        hmap : dict
            - A dictionary mapping unique values to their corresponding hatch patterns.
            - Default is '{}'.
        fallback_hatch : str
            - The hatch pattern to use as fallback if no specific hatch is assigned.
            - Default is '" "' (string with single space).
        display_hatch : bool
            - A flag indicating whether to display hatch patterns on cells.
            - Default is False.

        Returns
        -------
            dict: A dictionary mapping each unique value to its corresponding hatch pattern.
        """

        # Define a list of available hatch patterns
        HATCH_PATTERN= ['o', '/', '*', '\\','..', '+o', 'x*', 'o-', '|', '-', '+', 'x', 'O', '.',  '//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO',  '**', '/o', '\\|', '|*', '-\\', 'O|', 'O.', '*-']

        # Retrieve unique values and their count from the DataFrame
        unique_values, n_unique= self.unique_config()

        # If 'display_hatch' is False, set all hatch patterns to a space
        if display_hatch== False:
            h_map= dict(zip(unique_values, [" "]*n_unique))

        # If 'display_hatch' is True and the length of 'h_map' matches the number of unique values
        elif display_hatch== True and len(h_map)== n_unique:
            h_map= dict(zip(unique_values, h_map))
        
        # If 'display_hatch' is True and 'h_map' has fewer entries than unique values
        elif display_hatch== True and 0<len(h_map)< n_unique:
            h_map= h_map
            for each_unique_value in unique_values:
                if each_unique_value not in h_map:

                    # Assign fallback hatch pattern for any missing unique value
                    h_map.update( {each_unique_value: fallback_hatch} )
        
        # If 'display_hatch' is True and 'h_map' is empty, assign default hatch patterns
        elif display_hatch== True and len(h_map)==0:
            h_map= dict(zip(unique_values, HATCH_PATTERN[:n_unique]))

        # Clean up all local variables for efficient memory management
        # del HATCH_PATTERN, unique_values, n_unique, display_hatch, each_unique_value, fallback_hatch
        locals().clear()

        # Trigger garbage collection for efficient memory management
        gc.collect()

        # Return the configured 'h_map'
        return h_map