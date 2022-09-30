import matplotlib.pyplot as plt

def err(A,B=1,report=False):
    """Fractional error of A with respect to B.
       Optionally print errors.
    """
    e = abs(A-B)/abs(B)

    if report : print("T, S, |T-S|/|S| : {:>8.2e}, {:>8.2e}, {:>8.2e}".format(A,B,e))

    return e

class show_plots:
    
    def __init__(self,linewidth=2.5,fontsize=20,titlesize=15,legendsize=12,
                 xy=['$x$','$f(x)$'],title='',style='plot',figsize=None):
        
        
        self.linewidth  = linewidth
        self.fontsize   = fontsize
        self.titlesize  = titlesize
        self.legendsize = legendsize
        self.xlabel     = xy[0]
        self.ylabel     = xy[1]
        self.title      = title
                
        self.fig, self.ax = plt.subplots(figsize=figsize)
        
        self.ax.set_xlabel(self.xlabel,fontsize=fontsize)
        self.ax.set_ylabel(self.ylabel,fontsize=fontsize)
        self.ax.set_title(self.title,fontsize=titlesize)
        self.ax.tick_params(axis='both',labelsize=fontsize)
        self.ax.invert_xaxis()

        self.style = style
        
    def __call__(self,x,y,color=None):
        
        if self.style == 'plot':
            self.ax.plot(x,y,linewidth=self.linewidth,color=color)
            
        if self.style == 'log':
            self.ax.semilogy(x,y,linewidth=self.linewidth,color=color)
            
        if self.style == 'log-log':
            self.ax.loglog(x,y,linewidth=self.linewidth,color=color)
        
        
    def __getitem__(self,*args):
        
        self.ax.legend(list(args[0]),prop={'size': self.legendsize})
