from .kitiki_cell import KitikiCell
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

class kitikiplot(KitikiCell):

    def __init__(self, data, stride= 1, window_length= 10):

        super().__init__(data=data, stride= stride, window_length= window_length)
        self.rows= self.data.shape[0]
        self.cols= self.data.shape[1]

    def plot( self, 
              window_range= "all",
              figsize= (25, 5),
              cell_width= 0.5,
              cell_height= 2,
              window_gap= 1,
              cmap= "rainbow",
              fallback_color= "#FAFAFA", 
              edge_color= "#000000", 
              hmap= {},
              fallback_hatch= " ",
              display_hatch= False,
              legend_hatch= False,
              title= "KitikiPlot: Intuitive Visualization for Sliding Window", 
              xtick_prefix= "Window",
              ytick_prefix= "Frame",
              xlabel= "Sliding Windows", 
              ylabel= "Frames", 
              xticks_rotation= 0, 
              yticks_rotation= 0,
              display_legend= False,
              kitiki_cell_kwargs= {},
              legend_kwargs= {},
              transpose= False ):


        self.color_map= self.color_config( cmap= cmap, edge_color= edge_color, fallback_color= fallback_color )
        print("Color COnfig beofre start: ", self.color_map)
        
        if len(hmap)> 0:
            display_hatch= True

        # If display_hatch is False and hmap not given
        if display_hatch== False:
            hmap= " "
            fallback_hatch= " "

        self.hatch_map= self.hatch_config( h_map= hmap, fallback_hatch= fallback_hatch, display_hatch= display_hatch)

        fig, ax = plt.subplots( figsize= figsize)

        patches= [] 

        data= self.data.values

        if window_range== "all":
            window_range= range(self.rows)
        else:
            window_range= range( window_range[0], window_range[1])


        for index in window_range:

            each_sample= data[ index ]

            for time_frame in range(self.cols):

                cell_gen= self.create(x= index,
                                        y= time_frame,
                                        each_sample= each_sample,
                                        cell_width= cell_width,
                                        cell_height= cell_height,
                                        window_gap= window_gap,
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

        for each_patch in patches:
            ax.add_patch( each_patch )

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        if transpose==False:

            plt.xticks( [(i+1)*window_gap+(i+1)*cell_width+cell_width/2 for i in range(self.rows)],
                        [xtick_prefix+'_'+str(i+1) for i in range(self.rows)], rotation= xticks_rotation)
            
            plt.yticks( [(i+1)*cell_height+cell_height/2 for i in range(self.cols)],
                        [ytick_prefix+"_"+str(i) for i in range(self.cols)], rotation= yticks_rotation)
        else:
            plt.yticks( [(i+1)*window_gap+(i+1)*cell_width+cell_width/2 for i in range(self.rows)],
                        [xtick_prefix+'_'+str(i+1) for i in range(self.rows)], rotation= yticks_rotation)
            
            plt.xticks( [(i+1)*cell_height+cell_height/2 for i in range(self.cols)],
                        [ytick_prefix+"_"+str(i) for i in range(self.cols)], rotation= xticks_rotation)
            
        # automatically scale the plot
        ax.relim()
        ax.autoscale_view() 

        if (display_legend== True):

            self.legend( ax= ax, color_map= self.color_map,hatch_map= self.hatch_map, legend_hatch= legend_hatch, **legend_kwargs  )

        plt.show()

    def legend(self, ax, color_map, hatch_map, legend_hatch, **legend_kwargs  ):

        if legend_hatch== False:

            legend_patches = [mpatches.Patch(facecolor=color, label=label) for label, color in color_map[0].items()]


        else:

            legend_patches= [mpatches.Patch(facecolor= color_map[0][key], label= key, hatch= r"{}".format(hatch_map[key]*2)) for key in color_map[0]]
            
            print("=================================")
            print("_____________Legend Patches", legend_patches)
            print("_____________Hatch Map", hatch_map)
            print("_____________Legend Hatch", legend_hatch)
            print("_____________Mapping: ", [hatch_map[key] for key in color_map[0]])

        print( "_________________", legend_kwargs )
        kwargs= legend_kwargs
        print("_______", kwargs)

        return ax.legend(handles=legend_patches, **legend_kwargs)
        