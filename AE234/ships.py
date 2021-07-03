import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

X = np.array([22.570197196339215, 24.770763559917114, 27.185882427329428, 29.836472402833373, 32.74549162877728, 35.93813663804626, 38.535285937105314, 41.32012400115339])
Y = np.array([0.0029255450038596486, 0.0030968881146748633, 0.003403332726680874, 0.003670736610253667, 0.003959150733697869, 0.0043509183292762205, 0.004691887849162773, 0.005059578213867156])

#Before
X1 = np.array([1.3571428571428577,
1.3775510204081631,
1.4081632653061225,
1.4387755102040818,
1.4591836734693877,
1.479591836734694,
1.5102040816326534,
1.5408163265306127,
1.5816326530612246,
1.612244897959184,
#1.6428571428571428,  # These have been removed since they come under different
#1.6632653061224492,  category, this is done from the adat extracted in webplotdigitizer thing.
#1.6734693877551021,  Last 7 entries have been removed
#1.6938775510204085,
#1.7040816326530615,
#1.7244897959183678,
#1.7448979591836733
])

Y1 = np.array([-2.5335988053758087,
-2.5090426414468223,
-2.492533598805376,
-2.4678944748631158,
-2.4514683922349425,
-2.426912228305956,
-2.386012941762071,
-2.3613738178198105,
-2.328521652563464,
-2.2876223660195785,
#-2.246723079475693,
#-2.20590675294508,
#-2.1651733864277416,
#-2.116226978596317,
#-2.091753774680604,
#-2.0265472042475525,
#-1.9694707151153144
])

#AFTER
X2 = np.array([1.5918367346938775,
1.5918367346938774,
1.5918367346938773,
1.5714285714285716,
1.5714285714285715,
1.5714285714285714,
1.5612244897959182,
1.5510204081632653,
1.5306122448979593,
1.5204081632653064,
1.5204081632653063,
1.5204081632653062,
1.5204081632653061,
1.5204081632653060,
1.5204081632653059,
1.5102040816326534,
1.5102040816326533,
1.5102040816326532])

Y2 = np.array([-2.547950887672142,
-2.5723411315745803,
-2.5967313754770194,
-2.6212875394060062,
-2.637547702007632,
-2.661937945910071,
-2.694541231126597,
-2.7108843537414957,
-2.7435705989712953,
-2.7843039654886343,
-2.8005641280902602,
-2.8249543719926993,
-2.8493446158951383,
-2.88186494109839,
-2.8981251037000164,
-2.9225983076157287,
-2.9469885515181677,
-2.987638958022233])

#f = interp1d(X2, Y2, kind='cubic')

#plt.plot(X, Y, 'r', label="Commercial Ships/Oil Tankers")
plt.plot(X1, Y1, 'b', label="Commercial Ships/Oil Tankers Before")
plt.plot(X2, Y2, 'r', label="Commercial Ships/Oil Tankers After")
plt.plot(1.77815125, -1.951718578, 'rx', label="USS Theodore Roosevelt")
plt.plot(1.716003344, -1.666838389, 'bx', label="INS Vikrant")
plt.plot(1.662757832, -1.824754508, 'gx', label="HMS Hercules")
plt.plot(1.485721426, -2.917436801, 'go', label='Seawise Giant')
plt.plot(1.477121255, -2.302029468, 'gx', label='MV Edwin H. Gott')
plt.xlabel("LOG10 Velocity in kmph")
plt.ylabel("LOG10 Specific Tractive Force (epsilon) in kW/tonne-g m/s")
plt.title("LOG10 Specific Tractive Force versus LOG10 Velocity")
plt.grid(True)
plt.legend(loc="best")
plt.show()
