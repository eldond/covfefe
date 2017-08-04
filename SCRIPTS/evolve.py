#-*-Python-*-
# Created by eldond at 2017 Aug 04  14:34

"""
This script evolves the COVFEFE model distribution

defaultVars parameters
----------------------

:param nt: Number of time steps to take

:param dt: Time step size in seconds

:param temp: Temperature of the coffee in K

:param mass: Mass of milk solid particles in g. From http://www4.ncsu.edu/~adpierce/u03_characteristics_milk.pdf, a milk
    fat globule has a diameter of 1-18 um. Call its radius 9 um and call the density 1000 kg/L. Then the mass is about
    3 ug = 3e-6 g.

:param random_thermal_motion_enable: T/F: random thermal motions are on
"""
defaultVars(
    nt=root['SETTINGS']['PHYSICS']['nt'],
    dt=root['SETTINGS']['PHYSICS']['dt'],
    temp=root['SETTINGS']['PHYSICS']['temp'],
    mass=root['SETTINGS']['PHYSICS']['mass'],
    random_thermal_motion_enable=True,
)

# Make sure we're ready to run
if 'initial_distribution' not in root['OUTPUTS']:
    root['SCRIPTS']['set_initial_distribution'].runNoGUI(plot_after=False)
if 'distribution' not in root['OUTPUTS']:
    root['OUTPUTS']['distribution'] = copy.deepcopy(root['OUTPUTS']['initial_distribution'])

# Setup
dist = root['OUTPUTS']['distribution']  # Shortcut
t0 = dist['t']
t = linspace(t0, t0+dt*nt, nt+1)
N = len(dist['x'])
thermal_speed = sqrt(2*temp*constants.k/mass)
vt_comp = thermal_speed/sqrt(3)  # Each of the x, y, z, components will have this typical thermal velocity

# Set up histories
hist = dist.setdefault('history', OMFITtree())
hist['x'] = zeros([nt+1, N])
hist['y'] = zeros([nt+1, N])
hist['z'] = zeros([nt+1, N])
hist['x'][0, :] = dist['x']
hist['y'][0, :] = dist['y']
hist['z'][0, :] = dist['z']
hist['t'] = t

for i in range(1, nt+1):
    if random_thermal_motion_enable:
        for a in ['x', 'y', 'z']:
            v = np.random.normal(0, vt_comp, N)
            hist[a][i, :] = hist[a][i-1, :] + v * dt

dist['x'] = hist['x'][-1, :]
dist['y'] = hist['y'][-1, :]
dist['z'] = hist['z'][-1, :]
dist['t'] = t[-1]
dist['t0'] = t0
