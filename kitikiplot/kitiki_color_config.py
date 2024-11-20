"""
File Name: kitiki_color_config.py
Description: This file defines the 'ColorConfig' class for managing input data(list, dataframe) and configuring color, hatch of kitiki plot
Author: Boddu Sri Pavan
Date Created: 20-10-2024
Last Modified: 20-11-2024
"""

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import random
import math

class ColorConfig:
    """
    Set data, color, and hatch configurations required for kitikiplot

    Parameters
    ----------
    data: pd.DataFrame, list
        - Data to generate kitikiplot. 
        - This can be considered to be as "Categorical Time-Series Data" 
    stride: int
        - No.of steps the sliding window jumps across bwtween consecutive timestamps
        - Default is '1' indicating sliding window moves one position forward between any consewcutive timestamps
    window_length: int
        - Length/ Size of sliding window
        - Default is '10'

    Attributes
    ----------
    data: pd.DataFrame
        - The dataset with which kitikiplot is initialized
    row: int
        - No.of rows in dataframe (defaultly considered as each sliding window)
    cols: int
        - No.of columns in dataframe (defaulty considered as value at each instance in corresponding sliding window)

    
    Methods
    -------
        Instance Methods:
            color_config
            hatch_config
            unique_config
        Static Methods:
            _convert_list_to_dataframe
    """

    def __init__(self, data, stride= 1, window_length= 10):

        if isinstance( data, pd.DataFrame):
            self.data= data

        elif isinstance( data, list):
            self.data= self._convert_list_to_dataframe( data, stride, window_length)

        self.rows= self.data.shape[0]
        self.cols= self.data.shape[1]

    @staticmethod
    def _convert_list_to_dataframe( data, stride= 1, window_length= 10):

        n_rows= math.ceil(max(len(data)-window_length, 0)/ stride +1)

        l= []

        for i in range( n_rows ):

            row_data= data[i*stride: i*stride+window_length]

            if len(row_data)< window_length:

                row_data+= ["No_Data"]* (window_length- len(row_data))
            
            l.append( row_data )
        
        print( "Inside list: ", l)

        return pd.DataFrame( l )

    def unique_config(self):

        unique_values= pd.unique( self.data.values.ravel())

        n_unique= unique_values.shape[0]

        return unique_values, n_unique

    def color_config(self, cmap, edge_color, fallback_color):

        unique_values, n_unique= self.unique_config()

        if type(cmap)== str:
            
            cmap = plt.get_cmap( cmap, n_unique)

            custom_palette = [matplotlib.colors.rgb2hex(cmap(i)) for i in range(cmap.N)]

            color_map= dict(zip(unique_values, custom_palette))

        elif type(cmap)==dict:
            
            color_map= cmap

            if len(cmap)!= n_unique:
                for each_unique in unique_values:
                    if each_unique not in color_map:
                        color_map.update( {each_unique: fallback_color} )

        return color_map, edge_color
    
    def hatch_config(self, h_map, fallback_hatch, display_hatch):

        HATCH_PATTERN= ['o', '/', '*', '\\','..', '+o', 'x*', 'o-', '|', '-', '+', 'x', 'O', '.',  '//', '\\\\', '||', '--', '++', 'xx', 'oo', 'OO',  '**', '/o', '\\|', '|*', '-\\', 'O|', 'O.', '*-']

        unique_values, n_unique= self.unique_config()

        if display_hatch== False:

            h_map= dict(zip(unique_values, [" "]*n_unique))

        elif display_hatch== True and len(h_map)== n_unique:
            h_map= dict(zip(unique_values, h_map))
        
        elif display_hatch== True and 0<len(h_map)< n_unique:
            h_map= h_map
            for each_unique_value in unique_values:
                if each_unique_value not in h_map:
                    h_map.update( {each_unique_value: fallback_hatch} )
        
        elif display_hatch== True and len(h_map)==0:
            h_map= dict(zip(unique_values, HATCH_PATTERN[:n_unique]))

        return h_map
        # if len(h_map)!= n_unique:


