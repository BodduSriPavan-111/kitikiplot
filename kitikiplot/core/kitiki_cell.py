"""
File Name: kitiki_cell.py
Description: This file defines the 'KitikiCell' class for each rectangular cell in KitikiPlot
Author: Boddu Sri Pavan
Date Created: 21-10-2024
Last Modified: 31-05-2025
"""

# Import necessary libraries
from typing import List, Dict, Union
import pandas as pd
import matplotlib.patches as mpatches
from matplotlib.patches import Rectangle
from .kitiki_color_config import ColorConfig

class KitikiCell(ColorConfig):
    """
    Represents a cell in the KitikiPlot visualization.

    This class extends the ColorConfig class to add functionality for creating 
    individual cells in a grid-based visualization.

    Parameters
    ----------
    data : pd.DataFrame or list
        - The input data which can be either a 'pd.DataFrame' or a 'list'.
        - If a list is provided, it will be converted into a DataFrame using specified stride and window length.
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
    
    def __init__(self, data: Union[pd.DataFrame, list], stride: int = 1, window_length: int = 10) -> None:
        """
        Initialize the KitikiCell object by inheriting from ColorConfig.

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
        
        Attributes
        ----------
        stride : int
            - The number of elements to move the window after each iteration when converting a list to a DataFrame.
            - Default is 1.
        """

        super().__init__(data=data, stride= stride, window_length= window_length)


    def create( self,
                x: int,
                y: int,
                each_sample: List,
                cell_width: float,
                cell_height: float,
                window_gap: float,
                align: bool,
                cmap: Union[str, Dict],
                edge_color: str,
                fallback_color: str,
                hmap: Dict,
                fallback_hatch: str,
                display_hatch: bool,
                transpose: bool,
                focus,
                focus_alpha,
                **kitiki_cell_kwargs: dict) -> mpatches.Rectangle:
        
        """
        Create a rectangular cell for the KitikiPlot visualization.

        Parameters
        ----------
        x : int
            - The x-coordinate of the cell in the grid.
        y : int
            - The y-coordinate of the cell in the grid.
        each_sample : list
            - A list containing each data record used for determining color and hatch patterns to plot KitikiPlot.
        cell_width : float
            - The width of each cell in the grid.
            - Default is 0.5.
        cell_height : float
            - The height of each cell in the grid.
            - Default is 2.0.
        window_gap : float
            - The gap between cells in the grid.
            - Default is 1.0.
        align : bool
            - A flag indicating whether to shift consecutive bars vertically (if transpose= False), and
              horizontally(if transpose= True) by stride value.
            - Default is True.
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
        hmap : dict
            - A dictionary mapping unique values to their corresponding hatch patterns.
            - Default is '{}'.
        fallback_hatch : str
            - The hatch pattern to use as fallback if no specific hatch is assigned.
            - Default is '" "' (string with single space).
        display_hatch : bool
            - A flag indicating whether to display hatch patterns on cells.
            - Default is False.
        transpose : bool
            - A flag indicating whether to transpose the dimensions of the cells.
            - Default is False.
        kitiki_cell_kwargs : keyword arguments
            - Additional keyword arguments passed to customize the Rectangle object.
            - Default is {}.

        Returns
        -------
        matplotlib.patches.Rectangle: A Rectangle object representing the configured cell for KitikiPlot visualization.
        """

        # Adjust dimensions if 'transpose' is set to 'False'
        if not transpose:

            # Calculate alignment factor based on whether alignment is enabled
            align_factor= (self.rows-x)*self.stride*cell_height if align else 0

            # Calculate dimensions for the rectangle based on grid position and size parameters
            dim_x= window_gap*(x+1)+ cell_width*(x+1)
            dim_y= cell_height*(self.cols-y-1)+align_factor

            if focus == None:   
                rect_dim= ( dim_x, dim_y )
                print( x, y, dim_x, dim_y )

            else:

                align_factor= (self.rows)*self.stride*cell_height
                focus_dim_y= cell_height*(self.cols-y-1)+align_factor

                # Calculate dimensions for the rectangle based on grid position and size parameters
                rect_dim= ( dim_x, focus_dim_y )

                max_y= cell_height*(self.cols-1)+ ((self.rows)*self.stride*cell_height)

                if (focus_dim_y > max_y - (cell_height*self.window_length + cell_height*x*self.stride)) and  (focus_dim_y <= max_y - (cell_height*x*self.stride)):
                    kitiki_cell_kwargs["alpha"]= 1
                else:
                    kitiki_cell_kwargs["alpha"]= focus_alpha

        # Adjust dimensions if 'transpose' is set to 'True'
        else:

            # Set cell width to 2.0 for transposed cells to enhance visualization
            # cell_width= 2.0

            # Calculate alignment factor for transposed configuration based on whether alignment is enabled
            align_factor= x*self.stride*cell_height if align else 0

            # Calculate dimensions for the rectangle based on grid position and size parameters for transposed layout
            dim_x= cell_height*(y+1)+ align_factor
            dim_y= window_gap*(self.rows- x+1)+ cell_width*(self.rows- x+1)

            rect_dim= (dim_x, dim_y)
    
            if focus != None:
               
                align_factor= x*self.stride*cell_height

                min_dim_x= cell_height + align_factor
                max_dim_x= cell_height*(self.cols)+ align_factor

                if (min_dim_x <= dim_x) and (dim_x <= max_dim_x):
                    kitiki_cell_kwargs["alpha"]= 1
                else:
                    kitiki_cell_kwargs["alpha"]= focus_alpha


        # Clean up all local variables for efficient memory management
        # del align_factor, rect_dim, x, y, cell_width, cell_height, align, window_gap
        locals().clear() 

        # Return a Rectangle object with specified dimensions and styles based on input parameters
        return Rectangle( rect_dim,
           width= cell_width, 
           height= cell_height,
           facecolor= cmap[0][ each_sample[y] ],
           edgecolor= cmap[1],
           hatch= hmap[each_sample[y]],
           **kitiki_cell_kwargs
           )
