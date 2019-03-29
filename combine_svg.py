import sys
import numpy as np
import svgutils.transform as sg
from svgmanip import Element

FREECADPATH = '/usr/lib/freecad/lib'
sys.path.append(FREECADPATH)

import FreeCAD
import importSVG


coordinates = np.genfromtxt('coordinates_A11.csv', delimiter=',')

#fig_main = sg.fromfile('all_objects_A11.svg')
el_main = Element('all_objects_A11.svg')
#import ipdb; ipdb.set_trace()
#fig = sg.SVGFigure(fig_main.width, fig_main.height)
el = Element(el_main.width, el_main.height)

i = 0

for c in coordinates:
    #fig_t = sg.fromfile('out/A11_' + str(int(c[0])) + 'f.svg')
    el_t = Element('out/A11_' + str(int(c[0])) + 'f.svg')
    #plot_t = fig_t.getroot()
    #i += 1
    #plot_t.moveto(int(c[1]), int(c[2]))
    #fig.append(plot_t)
    #print 'out/A11_' + str(int(c[0])) + 'f.svg'
    el.placeat(el_t, c[1], c[2])
    #el = Element(el.width, el.height, el, el_t)

#fig.save("fig_final.svg")
el.dump('el_final.svg')
print 'uh'
'''
fig = sg.SVGFigure("100cm", "100cm")
fig1 = sg.fromfile('out/A11_109f.svg')
fig2 = sg.fromfile('out/A11_110f.svg')
plot1 = fig1.getroot()
plot2 = fig2.getroot()
import ipdb; ipdb.set_trace()
fig.append([plot1, plot2])
fig.save('fig_final.svg')
'''
