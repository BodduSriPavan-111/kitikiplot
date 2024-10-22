from .kitiki_cell import KitikiCell
import matplotlib.pyplot as plt

class kitikiplot(KitikiCell):

    def __init__(self, data):

        super().__init__(data=data)
        self.rows= self.data.shape[0]
        self.cols= self.data.shape[1]

    def plot( self, 
              window_range= "all",
              figsize= (25, 5),
              cell_width= 0.5,
              cell_height= 2,
              window_gap= 1,
              cmap= "rainbow", 
              edge_color= "#000000", 
              title= "KitikiPlot: Intuitive Visualization for Sliding Window", 
              xtick_prefix= "Window",
              ytick_prefix= "Frame",
              xlabel= "Sliding Windows", 
              ylabel= "Frames", 
              xticks_rotation= 0, 
              yticks_rotation= 0 ):

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
                                           cmap= cmap
                                           )
                patches.append( cell_gen )

        for each_patch in patches:
            ax.add_patch( each_patch )

        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        plt.xticks( [(i+1)*window_gap+(i+1)*cell_width+cell_width/2 for i in range(self.rows)],
                    [xtick_prefix+'_'+str(i+1) for i in range(self.rows)], rotation= xticks_rotation)
        
        plt.yticks( [(i+1)*cell_height+cell_height/2 for i in range(self.cols)],
                    [ytick_prefix+"_"+str(i) for i in range(self.cols)], rotation= yticks_rotation)
        
        # automatically scale the plot
        ax.relim()
        ax.autoscale_view() 
        plt.show()