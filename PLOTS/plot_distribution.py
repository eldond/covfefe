#-*-Python-*-
# Created by eldond at 2017 Aug 04  07:29

"""
This script plots particle distributions in the COVFEFE model

defaultVars parameters
----------------------
:param dist: Select which distribution to plot. 0 plots initial distribution.

:param R: Radius of the cup (cm)

:param Z: Height of the cup (cm)
"""
defaultVars(
    dist=0,
    R=root['SETTINGS']['PHYSICS'].setdefault('R', 3.5),
    Z=root['SETTINGS']['PHYSICS'].setdefault('Z', 5.5),
)

if dist == 0:
    d = root['OUTPUTS']['initial_distribution']
    dist_label = 'initial distribution'
else:
    d = root['OUTPUTS']['final_distribution']
    dist_label = 'final distribution'

x = d['x']
y = d['y']
z = d['z']

# Plot
fig = gcf()
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
ax1.set_title('COVFEFE model ({})'.format(dist_label))

ax2.set_aspect('equal', adjustable='box')
ax2.set_title('COVFEFE model ({})'.format(dist_label))
ax2.plot(x, y, z, '.', alpha=0.5)
ax2.plot(R*cos(tc), R*sin(tc), 0*tc, color='k')
ax2.plot(R*cos(tc), R*sin(tc), 0*tc+Z, color='k')
ax2.set_xlabel('X (cm)')
ax2.set_ylabel('Y (cm)')
ax2.set_zlabel('Z (cm)')

# Histograms
r = sqrt(x**2 + y**2)
theta = arctan2(x, y)

ax3.hist(r**2)
ax3.set_xlabel('$R^2$ (cm$^2$)')
ax3.set_ylabel('Occurrences')

ax4.hist(theta/pi)
ax4.set_xlabel('$\\theta/\pi$')

tight_layout()
