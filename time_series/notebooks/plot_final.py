import datetime as dt
import os
import netCDF4 as nc

import numpy as np
from scipy.spatial import distance
import matplotlib
from matplotlib import pyplot as plt
import matplotlib.colors as mpl_colors
from matplotlib import rc
from mpl_toolkits.axes_grid1 import make_axes_locatable


from salishsea_tools import geo_tools
from salishsea_tools import viz_tools


plt.ioff()



# activate latex text rendering
rc('text', usetex=True)


class Traj:
    def __init__(self, traject, t0, deltat = 20):
        
        self.deltat = deltat
        
        self.traj = traject
    
        self.points = [(x[1], x[2]) for x in self.traj]

        self.particles = [x[0] for x in self.traj]
        
        self.t0 = t0
        
    def closest_p(self, p2):
        
        closest_p = self.points[distance.cdist([p2], self.points).argmin()]
        
        return closest_p
    
    def find_particle (self,point):

        when = self.points.index(point)

        P = self.particles[when]
        
        return P
    
    def time (self, point):
        return self.t0 + dt.timedelta(minutes= self.deltat * self.points.index(point))
    
    def timec (self, point):
        return self.t0 + dt.timedelta(minutes= self.deltat * self.points.index(self.closest_p(point)))
    
    def sub_traj(self, particle):
        T = [i for i in self.traj if i[0] == particle]
        b= Traj(traject = T, t0 = self.t0+dt.timedelta(minutes = particle*60), deltat = self.deltat)
        return b



# In[ ]:




# In[ ]:

def param(start, length):
    
  
    
    COL = 1


    
    size = 40
    
    fontsize = 70
    
    
    
    matplotlib.rcParams.update({'font.size': fontsize})
    
    
    ms = 25 #marksize

    LIN = 1
    

    S15 = (-123.3114, 49.130412)
    S16 = (-123.317415, 49.1214)
    
    
    
    
    bathy = nc.Dataset("/ocean/gsgarbi/bathy_meter_SalishSea2.nc")
    model_lats = bathy.variables['nav_lat'][:]
    model_lons = bathy.variables['nav_lon'][:]
    depth = bathy.variables['Bathymetry'][:]
    
    
    
    
    
    #End of spit
    late = 49.205
    lone = -123.26
    #Further up spit
    lats = 49.214
    lons = -123.22
    
    
    
    dx = 1.2
    lat = late + dx * (late - lats)
    lon = lone + dx * (lone - lons)
    y, x = geo_tools.find_closest_model_point(lon, lat, model_lons, model_lats)

    outy = y - 1
    outx = x - 1
    
    deep = 110
    shallow = 35
    
    time0 = start
    
    time14 = length
    
    new_limx = (-124.5,-122.5)
    
    new_limy = (48.7,49.5)

    
    
    
    new_ticksx = (new_limx[0], float(sum(new_limx))/2, new_limx[1])
    
    new_ticksy = (new_limy[0], float(sum(new_limy))/2, new_limy[1])
                       
    
    Iona =(model_lons[outy, outx], model_lats[outy, outx])
    
    
    
    #norm_p = mpl_colors.Normalize(vmin=deep, vmax=shallow)
    norm_p = mpl_colors.Normalize(vmin=shallow, vmax=deep)
    cmap_p = plt.cm.plasma_r
    
    norm_w = None
    cmap_w = "winter_r"
    
    norm_p = mpl_colors.Normalize(vmin=time0, vmax=time14)
    cmap_p = plt.cm.plasma_r
    
    meshes = plt.figure(figsize=(4,4))
    
    ax_w = meshes.add_subplot(131)
    
    ax_p = meshes.add_subplot(132)
    
    ax_t = meshes.add_subplot(133)
    

    
    mesh_w = ax_w.pcolormesh(model_lons, model_lats, depth, cmap=cmap_w, norm = norm_w)
            
    mesh_p = ax_p.pcolormesh(model_lons, model_lats, depth, cmap=cmap_p, norm = norm_p)
    
    mesh_t = ax_t.pcolormesh(model_lons, model_lats, depth, cmap=cmap_p, norm = norm_p)
    
    fig, axs = plt.subplots(LIN,COL, figsize = (size,size))
    
    axs=np.reshape(axs,(1,1))
    
    
    
    for j in range(LIN):
        for k in range (COL):
            
            divider = make_axes_locatable(axs[j,k])
            
            cax_w = divider.append_axes("right", size="5%", pad=0.05)
            
            cax_p = divider.append_axes("bottom", size="5%", pad=1.9)
            
            
            cb_w = fig.colorbar(mesh_w, cax = cax_w)
            
            cb_p = fig.colorbar(mesh_p, cax = cax_p, orientation = "horizontal")
            
            cb_w.set_label("Water Depth (m)")
            
            cb_p.set_label(r"Time \textbf{t} in days")
    
    
    
    
            mesh_w = axs[j,k].pcolormesh(model_lons, model_lats, depth, cmap=cmap_w)
    
    

            
    
            axs[j,k].set_xlim(new_limx)
            axs[j,k].set_xticks(new_ticksx)
            axs[j,k].set_xticklabels(('%s W' %-new_limx[0], '%s W' %-round(float(sum(new_limx))/2,2), '%s W' %-new_limx[1]))
            axs[j,k].set_xlabel('Longitude')
            
            axs[j,k].set_ylim(new_limy)
            axs[j,k].set_yticks(new_ticksy)
            axs[j,k].set_yticklabels(('%s N' %new_limy[0], '%s N' %round(float(sum(new_limy))/2,1), '%s N' %new_limy[1]))
            axs[j,k].set_ylabel('Latitude')
            
            
            #Iona
            axs[j,k].plot(Iona[0], Iona[1], 'wo', ms = ms)
            #New Stations
    
            axs[j,k].plot(S15[0],S15[1], 'wo', ms = ms)
            
            axs[j,k].plot(S16[0],S16[1], 'wo', ms = ms)
            
            axs[j,k].annotate(
            "Iona outfall",
            xy=(model_lons[outy, outx], model_lats[outy, outx]), xytext=(50, 10),
            textcoords='offset points', ha='left', va='bottom',
            #bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
            
            axs[j,k].annotate(
            "Station 15",
            xy=(S15[0],S15[1]), xytext=(50, 10),
            textcoords='offset points', ha='left', va='bottom',
            #bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
    
            axs[j,k].annotate(
            "Station 16",
            xy=(S16[0],S16[1]), xytext=(50, 10),
            textcoords='offset points', ha='left', va='top',
            #bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
            arrowprops=dict(arrowstyle = '->', connectionstyle='arc3,rad=0'))
            
            viz_tools.set_aspect(axs[j,k])
        
    
    
    plt.tight_layout()
    return axs, fig

# In[31]:





# In[58]:

# what to plot, how many plots, how many particles, for how long?
# how many columns?
# create trajectories[], create axes parameters



def loadplot(directory):


    
    trajectories1 =[]
    init1 = []


    trajectories1.append(np.loadtxt(directory+"/traj.txt", delimiter = ' '))
    init1.append(np.loadtxt(directory+"/initial_positions.txt"))
    
    trajr = np.loadtxt(directory+"/traj.txt", delimiter = ' ')
    






    return trajr




def get_lasts(trajr):
    
    

    plot = []
 
    for P in range (1, 25):
    
        date_0 = first_date
        otraj = Traj(t0 = date_0, traject=trajr) 
    
        straj = otraj.sub_traj(P)
    
    
    
        plot.append(straj.traj[-1])
    
    return plot
    
    
    






#results: PARTCLES, title                       


# In[59]:

def create_title(first_date):

    

       
            
    title = r"Position after \textbf{t} " + "days for initial day {:%Y/%m/%d} ".format(first_date)

    
    return title

    
def makeplot(axs, title, totalplot, fig, t):
    
    j = 0
    k = 0
    
    tfs = 80 #title font
    
    axs[j,k].set_title(title, fontsize = tfs)
    


    
    LIN = 1
    
    COL = 1
    
    end = len(totalplot)
    
    s= 300
    



    for j in range(LIN):
        for k in range (COL):


            
            for i in range(len(totalplot)):
                if totalplot[i] != "empty":
                    for l in range(len(totalplot[i])):
                        scaled_t = 1-(end - i)/ end
                        cmap = plt.cm.plasma_r
                        color = cmap(scaled_t)
                        axs[j,k].scatter(totalplot[i][l][1], totalplot[i][l][2], c = color, edgecolor = "none", s =s)
    return fig           



def savefig(start, length, fig):
    
    url = resultsdir + "/plot_{}-{} day(s)".format(start, length)
    
    fig.savefig(url)
    
    print ("plot was saved on ", url)

    
start = 1   
trajlength = 30

first_date = dt.datetime(year = 2016, month = 7, day = 1)

axs, fig = param(start, trajlength+1)


totalplot = [] 
for d in range (start,trajlength+1):
    
    direct = "/ocean/gsgarbi/analysis-giorgio/time_series/results/2016/07/01/{} day(s)"

    if not os.path.isfile(direct.format(d)+"/traj.txt") or os.path.getsize(direct.format(d) + "/traj.txt") == 0:
        totalplot.append("empty")
        continue

    else:
        trajr = loadplot(direct.format(d))
        totalplot.append(get_lasts(trajr))

title = create_title(first_date)
    
resultsdir = "/ocean/gsgarbi/analysis-giorgio/time_series/results/2016/07/01/"
makeplot(axs, title, totalplot, fig, d)

savefig(start, trajlength, fig)