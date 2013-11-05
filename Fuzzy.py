import numpy
import peach


def inf(a,b):
    y=numpy.linspace(0,1,1000)
    i_zero = peach.Triangle(-0.1,0,0.1)
    i_low = peach.Triangle(0,0.25,0.5)
    i_medium = peach.Triangle(0.2,0.5,0.8)
    i_high = peach.Trapezoid(0.5,0.8,1,1.1)
    o_zero,o_low,o_medium,o_high,o_veryhigh = peach.FlatSaw((0,1),5)
    Points = 100
    yrange = numpy.linspace(0.,1.,1000)
    c = peach.Controller(yrange)
    c.add_rule(((i_zero,i_zero), o_zero))
    c.add_rule(((i_zero,i_low), o_low))
    c.add_rule(((i_zero,i_medium), o_medium))
    c.add_rule(((i_zero,i_high), o_medium))
    c.add_rule(((i_low,i_zero), o_low))
    c.add_rule(((i_low,i_low), o_medium))
    c.add_rule(((i_low,i_medium), o_medium))
    c.add_rule(((i_low,i_high), o_high))
    c.add_rule(((i_medium,i_zero), o_medium))
    c.add_rule(((i_medium,i_low), o_medium))
    c.add_rule(((i_medium,i_medium), o_medium))
    c.add_rule(((i_medium,i_high), o_high))
    c.add_rule(((i_high,i_zero), o_medium))
    c.add_rule(((i_high,i_low), o_high))
    c.add_rule(((i_high,i_medium), o_high))
    c.add_rule(((i_high,i_high), o_veryhigh))
    c.defuzzy = peach.Centroid

    x = numpy.linspace(0,1,Points)
    y = []
    for x0 in x:
        y.append(c(x0))
    y=numpy.array(y)

    return c(a,b)
