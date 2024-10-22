import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

class ColorConfig:

    def __init__(self, data):

        self.data= data
        self.color_map_cache= {}
        self.edge_color_cache= {}

    def _unique_config(self):

        unique_values= pd.unique( self.data.values.ravel())

        n_unique= unique_values.shape[0]

        return unique_values, n_unique

    def color_config(self, cmap, edge_color, fallback_color):

        if self.color_map_cache!={} and self.edge_color_cache!={}:
            
            return self.color_map_cache, self.edge_color_cache

        unique_values, n_unique= self._unique_config()

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

        self.color_map_cache= color_map
        self.edge_color_cache= edge_color

        return color_map, edge_color
    
    # def hatch_config(self, hmap, fallback_hatch):

    #     unique_values, n_unique= self._unique_config()

    #     if len(hmap)!= n_unique:


