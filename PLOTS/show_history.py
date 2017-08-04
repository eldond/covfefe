#-*-Python-*-
# Created by eldond at 2017 Aug 04  15:29

"""
This script plots time histories of test particles in the COVFEFE model.

defaultVars parameters
----------------------
:param ip: Indices of test Particles to plot
"""
defaultVars(
    ip=[0, 1, 2, 3, 4, 5],
)

h = root['OUTPUTS']['distribution']['history']

fig = gcf()
ax1 = fig.add_subplot(311)
ax2 = fig.add_subplot(312)
ax3 = fig.add_subplot(313)
fig.suptitle('History of position of test particle #{:}'.format(ip))

aa = ['x', 'y', 'z']
axs = [ax1, ax2, ax3]

for a, ax in zip(aa, axs):
    for i in ip:
        ax.plot(h['t'], h[a][:, i])
        ax.set_ylabel('{} (cm)'.format(a))

axs[-1].set_xlabel('t (s)')
