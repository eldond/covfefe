#-*-Python-*-
# Created by eldond at 2017 Aug 04  07:26

"""
This script sets up the initial distribution of particles for the COVFEFE model

defaultVars parameters
----------------------

:param R: Radius of the cup (cm)

:param Z: Height of the cup (cm)

:param N: Number of particles to simulate

:param plot_after: T/F: plot distribution after initializing
"""
defaultVars(
    R=root['SETTINGS']['PHYSICS'].setdefault('R', 3.5),
    Z=root['SETTINGS']['PHYSICS'].setdefault('Z', 5.5),
    N=root['SETTINGS']['PHYSICS'].setdefault('N', 1000),
    plot_after=root['SETTINGS']['EXPERIMENT']['plot_after'],
)

z = random(N) * Z
r = random(N)**0.5 * R
theta = random(N) * 2 * pi

x = r * cos(theta)
y = r * sin(theta)

init = root['OUTPUTS'].setdefault('initial_distribution', OMFITtree())
init['x'] = x
init['y'] = y
init['z'] = z
init['t'] = 0

if plot_after:
    root['PLOTS']['plot_distribution'].plot(t=0)
