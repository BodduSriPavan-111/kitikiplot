"""
File Name: Kiti.py
Description: This file defines the 'KitikiPlot' class for generating kitki plot for categorical sequential& time-series data
Author: Boddu Sri Pavan
Date Created: 21-10-2024
Last Modified: 23-11-2024
"""

from typing import List, Union
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from .kitiki_cell import KitikiCell

class KitikiPlot(KitikiCell):
    """
    A class to create a Kitikiplot visualization based on sliding window data.

    This class extends the KitikiCell class to provide functionality for plotting 
    KitikiPlot, where each cell can be customized with colors, hatches, 
    and other visual properties.

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
     
    def __init__(self, data: Union[pd.DataFrame, List], stride: int = 1, window_length: int = 10) -> None:
        """
        Initialize the KitikiPlot object by inheriting from KitikiCell.

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

    def plot( self, 
              figsize: tuple = (25, 5),
              cell_width: float = 0.5,
              cell_height: float = 2.0,
              window_gap: float = 1.0,
              window_range: str | tuple = "all",  
              align: bool = True,         
              cmap: str | dict = "rainbow",
              edge_color: str = "#000000", 
              fallback_color: str = "#FAFAFA",
              hmap: dict = {},
              fallback_hatch: str = " ",
              display_hatch: bool = False,
              transpose: bool = False,
              xlabel: str = "Sliding Windows", 
              ylabel: str = "Frames", 
              display_xticks: bool = True,
              display_yticks: bool = True,
              xtick_prefix: str = "Window",
              ytick_prefix: str = "Frame",
              xticks_values: list = [],
              yticks_values: list = [],
              xticks_rotation: int = 0, 
              yticks_rotation: int = 0,
              title: str = "KitikiPlot: Intuitive Visualization for Sliding Window",
              display_grid: bool = False,
              display_legend: bool = False,
              legend_hatch: bool = False,
              legend_kwargs: dict = {},
              kitiki_cell_kwargs: dict = {}
            ) -> None:
        """
        Create and display the Kitikiplot visualization.

        This method generates a plot based on the provided parameters and data. It configures 
        colors, hatches, and dimensions for each cell in the grid.

        Parameters
        ----------
        figsize : tuple (optional)
            - The size of the figure (width, height).
            - Default is (25, 5).
        cell_width : float
            - The width of each cell in the grid.
            - Default is 0.5.
        cell_height : float
            - The height of each cell in the grid.
            - Default is 2.0.
        window_gap : float
            - The gap between cells in the grid.
            - Default is 1.0.
        window_range : str or tuple (optional)
            - The range of windows to display.
            - Use "all" to show all windows or specify a tuple (start_index, end_index). 
            - Default is "all".
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
        transpose : bool (optional)
            - A flag indicating whether to transpose the KitikiPlot. 
            - Default is False.
        xlabel : str (optional)
            - Label for the x-axis. 
            - Default is "Sliding Windows".
        ylabel : str (optional)
            - Label for the y-axis. 
            - Default is "Frames".
        display_xticks : bool (optional)
            - A flag indicating whether to display xticks
            - Default is True
        display_yticks : bool (optional)
            - A flag indicating whether to display yticks
            - Default is True
        xtick_prefix : str (optional)
            - Prefix for x-axis tick labels. 
            - Default is "Window".
        ytick_prefix : str (optional)
            - Prefix for y-axis tick labels. 
            - Default is "Frame".
        xticks_values : list (optional)
            - List containing the values for xticks
            - Default is []
        yticks_values : list (optional)
            - List containing the values for yticks
            - Default is []
        xticks_rotation : int (optional)
            - Rotation angle for x-axis tick labels. 
            - Default is 0.
        yticks_rotation : int (optional)
            - Rotation angle for y-axis tick labels. 
            - Default is 0.
        title : str (optional)
            - The title of the plot. 
            - Default is "KitikiPlot: Intuitive Visualization for Sliding Window".
        display_grid : bool (optional)
            - A flag indicating whether to display grid on the plot.
            - Default is False.
        display_legend : bool (optional)
            - A flag indicating whether to display a legend on the plot. 
            - Default is False.
        legend_hatch : bool (optional)
            - A flag indicating whether to include hatch patterns in the legend. 
            - Default is False.
        legend_kwargs : dict (optional)
            - Additional keyword arguments passed to customize the legend.
            - Default is {}.
        kitiki_cell_kwargs : dict (optional)
            - Additional keyword arguments passed to customize individual cells.
            - Default is {}.
        
        Returns
        -------
        None: Displays the plot directly.
        """       

        # Configure color mapping based on user input
        self.color_map= self.color_config( cmap= cmap, edge_color= edge_color, fallback_color= fallback_color )
        
        # Determine if hatching should be displayed based on 'hmap' presence
        if len(hmap)> 0:
            display_hatch= True

        # If 'display_hatch' is False and 'hmap' not given; default hatch settings are applied
        if not display_hatch:
            hmap= " "
            fallback_hatch= " "

        # Configure hatch mapping based on user input and conditions
        self.hatch_map= self.hatch_config( h_map= hmap, fallback_hatch= fallback_hatch, display_hatch= display_hatch)

        # Create figure and axis for plotting
        fig, ax = plt.subplots( figsize= figsize)

        # List to hold cell patches
        patches= [] 

        # Prepare data for plotting
        data= self.data.values

        # Check if the specified window range is set to "all"
        if window_range== "all":

            # If "all" is specified, set window_range to cover all rows in the data
            window_range= range(self.rows)

        else:

            # If a specific range is provided, create a range object from the start to end index
            # This allows for plotting only a subset of the data based on the user-defined range
            window_range= range( window_range[0], window_range[1])

        # Generate cells for each sample in the specified window range and time frame columns
        for index in window_range:

            each_sample= data[ index ]

            for time_frame in range(self.cols):

                # Create each cell using specified parameters and add it to patches list 
                cell_gen= self.create(  x= index,
                                        y= time_frame,
                                        each_sample= each_sample,
                                        cell_width= cell_width,
                                        cell_height= cell_height,
                                        window_gap= window_gap,
                                        align= align,
                                        edge_color= edge_color,
                                        cmap= self.color_map,
                                        fallback_color= fallback_color,
                                        hmap= self.hatch_map,
                                        fallback_hatch= fallback_hatch,
                                        display_hatch= display_hatch,
                                        transpose= transpose,
                                        **kitiki_cell_kwargs
                                    )
                patches.append( cell_gen )

        # Set plot titles
        plt.title(title)

        # Configure ticks based on transposition setting
        if not transpose:

            # Calculate x and y positions for ticks when not transposed
            x_positions= [(i+1)*window_gap+(i+1)*cell_width+cell_width/2 for i in range(self.rows)]
            y_positions= [(self.rows+ self.cols- self.stride- i)*cell_height+cell_height/2 for i in range(self.stride*self.rows+self.cols)]

            # Display xticks if 'display_xticks' is True
            if display_xticks:

                # Configure xticks based on input 'xticks_values'
                if xticks_values:
                    
                    # Find no.of 'xticks_values'
                    n_xticks_values= len(xticks_values)

                    # Set x-ticks with the input 'xticks_values'
                    plt.xticks( x_positions[:n_xticks_values], xticks_values, rotation= xticks_rotation)

                # Configure default xticks
                else:

                    # Set x-ticks with appropriate labels (with default prefixes) and rotation
                    plt.xticks( x_positions, [xtick_prefix+'_'+str(i+1) for i in range(self.rows)], rotation= xticks_rotation)
            
            # Else turn off the xticks
            else:
                plt.xticks([], [])
            
            # Display yticks if 'display_yticks' is True
            if display_yticks:

                # Configure yticks based on input 'yticks_values
                if yticks_values:

                    # Find no.of 'yticks_values'
                    n_yticks_values= len(yticks_values)

                    # Set y-ticks with the input 'yticks_values'
                    plt.yticks( y_positions[:n_yticks_values], yticks_values, rotation= yticks_rotation)

                # Configure default yticks
                else:

                    print( "Y positions: ",len(y_positions))
                    print( "cols: ", self.cols)

                    # Set y-ticks with appropriate labels and rotation
                    plt.yticks( y_positions, [ytick_prefix+"_"+str(i) for i in range(self.stride*self.rows+self.cols)], rotation= yticks_rotation)
            
            # Else turn off the yticks
            else:
                plt.yticks([], [])
                
            # Draw grid lines if display_grid is True
            if display_grid:
                line_positions= [(i+1)*cell_height for i in range(self.rows+ self.cols- self.stride+ 1)]
                ax.hlines(y= y_positions, xmin=0, xmax=max(x_positions) + cell_width, colors='gray', linestyles='--', linewidth=0.5)

        else:

            # Calculate x and y positions for ticks when transposed
            x_positions= [(i+1)*cell_height+cell_height/2 for i in range(self.stride*(self.rows-1)+ self.cols)]
            y_positions= [(self.rows-i+1)*window_gap+(self.rows-i+1)*cell_width+cell_width/2 for i in range(self.rows)]

            # Display xticks if 'display_xticks' is True
            if display_xticks:

                # Configure xticks based on input 'xticks_values'
                if xticks_values:

                    # Find no.of 'xticks_values'
                    n_xticks_values= len( xticks_values )

                    # Set x-ticks with the input 'xticks_values'
                    plt.xticks( x_positions[:n_xticks_values], xticks_values, rotation= xticks_rotation)

                # Configure default xticks
                else:

                    # Set x-ticks with appropriate labels and rotation (note the switch of prefixes)
                    plt.xticks( x_positions, [xtick_prefix+"_"+str(i+1) for i in range(self.stride*(self.rows-1)+ self.cols)], rotation= xticks_rotation)
            
            # Else turn off the xticks
            else:
                plt.xticks([], [])


            # Display yticks if 'display_yticks' is True
            if display_yticks:

                # Configure yticks based on input 'yticks_values'
                if yticks_values:

                    # Find no.of 'yticks_values'
                    n_yticks_values= len( yticks_values )

                    # Set y-ticks with the input 'yticks_values'
                    plt.yticks( y_positions[:n_yticks_values], yticks_values, rotation= yticks_rotation)
                
                # Configure default yticks
                else:

                    # Set y-ticks with appropriate labels and rotation (note the switch of prefixes)
                    plt.yticks( y_positions, [ytick_prefix+'_'+str(i+1) for i in range(self.rows)], rotation= yticks_rotation)
            
            # Else turn off the yticks
            else:
                plt.yticks([], [])
                
            
            # Draw vertical grid lines if display_grid is True
            if display_grid:
                line_positions= [(i+1)*cell_height for i in range(self.rows+ self.cols- self.stride+ 1)]
                ax.vlines(x= line_positions, ymin=0, ymax=max(y_positions) + cell_width, colors='gray', linestyles='--', linewidth=0.5)

        # Set label for 'x'-axis
        plt.xlabel(xlabel)

        # Set label for 'y'-axis
        plt.ylabel(ylabel)
            
        # Add all created patches (cells) to axes for rendering
        for each_patch in patches:
            ax.add_patch( each_patch )

        # Update the limits of the axes based on the current data
        ax.relim()

        # Automatically adjust the view limits to fit the data within the axes
        ax.autoscale_view() 

        # Check if a legend should be displayed based on user input
        if display_legend:

            # Call the legend method to create and display the legend on the specified axes
            # Pass in the color map, hatch map, and any additional keyword arguments for customization
            self.legend( ax= ax, color_map= self.color_map,hatch_map= self.hatch_map, legend_hatch= legend_hatch, **legend_kwargs  )

        # Show the plot with all configurations applied
        plt.show()

    def legend(self, ax: matplotlib.axes.Axes, color_map: dict, hatch_map: dict, legend_hatch: bool, **legend_kwargs: dict ) -> matplotlib.legend.Legend:
        """
        Create and display legend for the KitikiPlot visualization.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
            - The axes object where the legend will be placed.
        color_map : dict
            - A dictionary mapping unique values to their corresponding colors.
        hatch_map : dict
           -  A dictionary mapping unique values to their corresponding hatch patterns.
        legend_hatch : bool (optional)
            - A flag indicating whether to include hatch patterns in the legend. 
            - Default is False.
        legend_kwargs: dict (optional) 
            - Additional keyword arguments passed to customize the legend.
            - Default is {}.

        Returns 
        -------
        matplotlib.legend.Legend: The created legend object.
       """
        
        # Check if hatch patterns should be included in the legend 
        if not legend_hatch:

            # Create legend patches without hatching
            # Each patch corresponds to a color in the color map and is labeled with its key
            legend_patches = [mpatches.Patch(facecolor=color, label=label) for label, color in color_map[0].items()]


        else:
            # Create legend patches that include hatching
            # Each patch corresponds to a color in the color map and is labeled with its key
            # The hatch pattern is specified based on the 'hatch_map', multiplied by 2 for visibility
            legend_patches= [mpatches.Patch(facecolor= color_map[0][key], label= key, hatch= r"{}".format(hatch_map[key]*2)) for key in color_map[0]]
            
        kwargs= legend_kwargs

        # Return the created legend object, attaching the generated patches and any additional kwargs
        return ax.legend(handles=legend_patches, **legend_kwargs)
        