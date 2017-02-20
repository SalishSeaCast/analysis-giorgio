

from scipy.spatial import distance



import datetime as dt

import matplotlib

import matplotlib as mat

matplotlib.use('Agg')





from matplotlib import pyplot as plt
plt.ioff()


import matplotlib.colors as mpl_colors


import netCDF4 as nc
import numpy as np
from salishsea_tools import geo_tools



from mpl_toolkits.axes_grid1 import make_axes_locatable







class Traj:
    def __init__(self, traject, deltat = 20):
        
        self.deltat = deltat
        
        self.traj = traject
    
        self.points = [(x[1], x[2]) for x in self.traj]

        self.particles = [x[0] for x in self.traj]
        
#        self.t0 = t0
        
    def closest_p(self, p2):
        
        closest_p = self.points[distance.cdist([p2], self.points).argmin()]
        
        return closest_p
    
    def find_particle (self,point):

        when = self.points.index(point)

        P = self.particles[when]
        
        return P
#    
#    def time (self, point):
#        return self.t0 + dt.timedelta(minutes= self.deltat * self.points.index(point))
#    
#    def timec (self, point):
#        return self.t0 + dt.timedelta(minutes= self.deltat * self.points.index(self.closest_p(point)))
    
    def sub_traj(self, particle):
        T = [i for i in self.traj if i[0] == particle]
        b= Traj(traject = T, deltat = self.deltat)
        return b



# In[ ]:




# In[ ]:

def param( ):
    


    size = 40
    
#    fontsize = 50
    
    
    
#    mat.rcParams.update({'font.size': fontsize})
    
    
    ms = 25
    

    
    

    


    
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
    
    time0 = 0
    
    time14 = 5
    
    new_limx = (-124.5,-122.5)
    
    new_limy = (48.7,49.5)

    
    
#    original_limx = (-123.5, -123.1)
#    
#    original_ticksx = (-123.5, -123.3, -123.1)
#    
#    original_limy = (49.05, 49.35)
#    
#    original_ticksy = (49.1, 49.2, 49.3)
    
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

        
    global fig, axs
    
    fig, axs = plt.subplots(LIN,COL, figsize = (size,size))

    
    if LIN == 1 or COL == 1:
        
        axs=np.reshape(axs,(1,1))
    
    
    
    for j in range(LIN):
        for k in range (COL):
            
            divider = make_axes_locatable(axs[j,k])
            
            cax_w = divider.append_axes("right", size="5%", pad=0.05)
            
            cax_p = divider.append_axes("bottom", size="5%", pad=1.6)
            
            
            cb_w = fig.colorbar(mesh_w, cax = cax_w)
            
            cb_p = fig.colorbar(mesh_p, cax = cax_p, orientation = "horizontal")
            
            cb_w.set_label("Water Depth (m)")
            
            cb_p.set_label("will fix")
    
    
    
    
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
        
    
    
    plt.tight_layout()
    return axs

# In[31]:





# In[58]:

# what to plot, how many plots, how many particles, for how long?
# how many columns?
# create trajectories[], create axes parameters



def loadtraj(directory):

    trajr = np.loadtxt(directory+"/traj.txt", delimiter = ' ')


    return trajr




def create_Traj(p, trajr, total = None):
    


    otraj = Traj(traject=trajr) 

    straj = otraj.sub_traj(p)



    points = straj.points
    

    return points
    
    
    






#results: PARTCLES, title                       


# In[59]:

def create_title(d, length):

    

            
            
    title = "INITIAL DAY: July {} (PDT) ;  LENGTH: length ; INITIAL DEPTHS(m): will add ".format (d)

    
    return title



def makeplot(axs, points):
    
    
    end = len(points)

    




        
    for t in range(len(points)):
        scaled_t = 1-(end - t)/ end
        cmap = plt.cm.plasma_r
        color = cmap(scaled_t)
        axs.scatter(points[t][0], points[t][1], c = color, edgecolor = "none")
         





# In[ ]:
    
def savefig(fig):
    
    url = resultsdir + "/plot"
    
    fig.savefig(url)
    
    print ("plot was saved on ", url)
    

#def go(d, r, f, p, axs, l = "2 weeks", c=1,):
#    global directory, COL, first_date, length, P, resultsdir
#    directory = d
#    COL = c
#    first_date = f
#    length = l
#    P = p
#    resultsdir = r
#    
#    
#
#    trajr = loadtraj (directory)
#    
#    print ("done2")
#    
#    
#    trajp = create_Traj(P, total=None, trajr = trajr)
#    
#    print ("done3")
#    
#    title = create_title(length, P, trajp)
#    
#    print ("done4")
#    
#    makeplot(axs = axs, title = title, trajp = trajp, fig = fig)
#    
#    print ("plot was made")
#    
#    return fig
    

    



LIN = 4
COL = 2                                                                         
plt.clf()
                 

length = "5 days"                                                        
axs = param()

LIN = 4
COL = 2   

for j in range(LIN):
    for k in range (COL):
        c = j*COL + k
        d = 14 + c

        direct = "/ocean/gsgarbi/analysis-giorgio/time_series/results/2016/07/{}/5 day(s)"
        
                                                                     
                                                                              
        trajr = loadtraj (direct.format(d))
        
        
        for p in (1,7, 13, 19):
            points = create_Traj(p, total=None, trajr = trajr)
            
   
            
            print (j,k)
            makeplot(axs[j,k], points)
        
        axs[j,k].set_title(create_title(d, length), fontsize = 25)
            
            
                                                                      




resultsdir = "/home/gsgarbi/Desktop"
savefig(fig)


