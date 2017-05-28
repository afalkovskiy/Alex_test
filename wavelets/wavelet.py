# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 21:29:15 2016

@author: falkov
"""

#from bokeh.layouts import column
from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import Figure, output_file, show

import math
import numpy as np

output_file("callback.html")

pi = np.pi

f = 25
phase = 0

x = [-.2 + x*0.002 for x in range(0, 200)]
#y = x
x = np.array(x)

for i in range(len(x)):
    y[i] = (1 - 2*pi*pi*f*f*x[i]*x[i]) * math.exp(-pi*pi*f*f*x[i]*x[i])



#for i in range(len(x)):
#    y[i] = (1 - 2*pi*pi*f*f*x[i]*x[i]) * math.exp(-pi*pi*f*f*x[i]*x[i])

source = ColumnDataSource(data=dict(x=x, y=y))

plot = Figure(title="RICKER WAVELET", plot_width=400, plot_height=400)
plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)

callback = CustomJS(args=dict(source=source), code="""
        var data = source.get('data');
        var f1 = cb_obj.get('value')
        var pi = Math.PI
        x = data['x']
        y = data['y']
        for (i = 0; i < x.length; i++) {
            y[i] = (1 - 2*pi*pi*f1*f1*x[i]*x[i]) * Math.exp(-pi*pi*f1*f1*x[i]*x[i])        
        }
        source.trigger('change');
    """)
       

slider = Slider(start=0.1, end=40, value=25, step=.1, title="frequency", callback=callback)

layout = column(plot, slider)

show(layout)