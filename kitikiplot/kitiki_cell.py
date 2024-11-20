"""
File Name: kitiki_cell.py
Description: This file defines the 'KitikiCell' class for each rectangular cell in kitiki plot
Author: Boddu Sri Pavan
Date Created: 20-10-2024
Last Modified: 20-11-2024
"""

from .kitiki_color_config import ColorConfig
from matplotlib.patches import Rectangle

class KitikiCell(ColorConfig):
    """
        Plot each KitikiCell (Rectangular patch) in KitikiPlot
        Inherits 'ColorConfig' class

        Parameters
        ----------
        data: pd.DataFrame, list
            - Data to generate kitikiplot. 
            - This can be considered to be as "Categorical Time-Series Data"
        stride: int
            - No.of steps the sliding window jumps across bwtween consecutive timestamps
            - Default is '1' indicating sliding window moves one position forward between any consewcutive timestamps
        window_length:  int
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
        create

        """
    
    def __init__(self, data, stride= 1, window_length= 10):

        super().__init__(data=data, stride= stride, window_length= window_length)


    def create( self,
                x,
                y,
                each_sample,
                cell_width,
                cell_height,
                cmap,
                fallback_color,
                edge_color,
                window_gap,
                hmap,
                fallback_hatch,
                display_hatch,
                transpose,
                **kitiki_cell_kwargs):

        rect_dim= (window_gap*(x+1)+ cell_width*(x+1) , cell_height*(y+1))

        if transpose== True:
            
            rect_dim= (cell_height*(y+1), window_gap*(x+1)+ cell_width*(x+1))

        return Rectangle( rect_dim,
           width= cell_width, 
           height= cell_height,
           facecolor= cmap[0][ each_sample[y] ],
           edgecolor= cmap[1],
           hatch= hmap[each_sample[y]],
           **kitiki_cell_kwargs
           )