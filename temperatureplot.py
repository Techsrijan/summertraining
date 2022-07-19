#from matplotlib.pyplot import *
import matplotlib.pyplot as plt
day=[1,2,3,4,5,6,7]
temp=[40,38,39,44,55,20,22]
plt.title("weather Graph")
#matplotlib.pyplot.ylabel('Temperature')
#matplotlib.pyplot.xlabel('Day')
plt.ylabel('Temperature')
plt.xlabel('Day')
plt.plot(day,temp,color='red',linewidth=5,linestyle="dotted")
plt.show()