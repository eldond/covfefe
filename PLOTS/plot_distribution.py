#-*-Python-*-
# Created by eldond at 2017 Aug 04  07:29

"""
This script plots particle distributions in the COVFEFE model

defaultVars parameters
----------------------
:param t: Select time slice to plot

:param nbins: Number of bins in histogram

:param dt: Time step (s)

:param nt: Number of time steps

:param R: Radius of the cup (cm)

:param Z: Height of the cup (cm)

:param N: Number of tracked test particles
"""
defaultVars(
    t=root['SETTINGS']['EXPERIMENT']['time'],
    nbins=50,
    dt=root['SETTINGS']['PHYSICS']['dt'],
    nt=root['SETTINGS']['PHYSICS']['nt'],
    R=root['SETTINGS']['PHYSICS']['R'],
    Z=root['SETTINGS']['PHYSICS']['Z'],
    N=root['SETTINGS']['PHYSICS']['N'],
)

if t == -1:
    if 'distribution' not in root['OUTPUTS']:
        t = 0

# Select distribution
if t == 0:
    d = root['OUTPUTS']['initial_distribution']
    dist_label = 'initial distribution'
    x = d['x']
    y = d['y']
    z = d['z']
elif t == -1:
    d = root['OUTPUTS']['distribution']
    dist_label = 'final distribution'
    it = round(float(t)/dt)
    x = d['x']
    y = d['y']
    z = d['z']
else:
    d = root['OUTPUTS']['distribution']['history']
    t0 = root['OUTPUTS']['distribution']['t0']
    it = int(round(float(t-t0)/dt))
    if it < 0:
        it = 0
    dist_label = 'distribution at t = {:}'.format(it*dt+t0)
    x = d['x'][it, :]
    y = d['y'][it, :]
    z = d['z'][it, :]

# Sanitize inputs
if nbins > N/10.:
    nbins = floor(N/10.)

# Get out data

# Plot
fig = gcf()
fig.suptitle('COVFEFE model {} w/ {} test particles'.format(dist_label, N))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222, projection='3d')
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224, sharey=ax3)

ax1.set_aspect('equal', adjustable='box')
ax1.plot(x, y, '.', alpha=0.5)
tc = linspace(0, 2*pi, 360)
ax1.plot(R*cos(tc), R*sin(tc), color='k')
ax1.set_xlabel('X (cm)')
ax1.set_ylabel('Y (cm)')
ax1.text(0.99, 0.99, 'R = {:} cm\nZ = {:} cm'.format(R, Z),
         ha='right', va='top', transform=ax1.transAxes,
         fontsize=8)

ax2.set_aspect('equal', adjustable='box')
ax2.plot(x, y, z, '.', alpha=0.5)
ax2.plot(R*cos(tc), R*sin(tc), 0*tc, color='k')
ax2.plot(R*cos(tc), R*sin(tc), 0*tc+Z, color='k')
ax2.set_xlabel('X (cm)')
ax2.set_ylabel('Y (cm)')
ax2.set_zlabel('Z (cm)')

# Histograms
r = sqrt(x**2 + y**2)
theta = arctan2(x, y)

ax3.hist(r**2, bins=nbins)
ax3.set_xlabel('$R^2$ (cm$^2$)')
ax3.set_ylabel('Occurrences')
ax3.axvline(R**2, color='k', linestyle='--')

ax4.hist(theta/pi, bins=nbins)
ax4.set_xlabel('$\\theta/\pi$')
ax4.get_yaxis().set_visible(False)

tight_layout()
