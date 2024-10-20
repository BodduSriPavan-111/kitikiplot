import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

class ColorConfig:

    def __init__(self, data):

        self.data= data



    def config(self, cmap= "rainbow", edge_color= "#000000"):

        unique_values= pd.unique( self.data.values.ravel())

        n_unique= unique_values.shape[0]

        cmap = plt.get_cmap( cmap, n_unique)

        custom_palette = [matplotlib.colors.rgb2hex(cmap(i)) for i in range(cmap.N)]

        color_map= dict(zip(unique_values, custom_palette))

        return color_map, edge_color