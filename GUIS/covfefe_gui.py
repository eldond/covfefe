#-*-Python-*-
# Created by eldond at 2017 Aug 04  15:14

"""
This script provides the main COVFEFE module GUI
"""

OMFITx.TitleGUI('COVFEFE')

if 'initial_distribution' not in root['OUTPUTS']:
    OMFITx.Entry(
        "root['SETTINGS']['PHYSICS']['N']",
        'Number of test particles',
        default=1000,
    )
    OMFITx.Entry(
        "root['SETTINGS']['PHYSICS']['R']",
        'Radius of coffee mug (cm)',
        default=3.3,
    )
    OMFITx.Entry(
        "root['SETTINGS']['PHYSICS']['Z']",
        'Height of coffee mug (cm)',
        default=5.5,
    )
    OMFITx.Button(
        'Set up initial distribution',
        root['SCRIPTS']['set_initial_distribution'].run,
    )
else:
    OMFITx.Entry(
        "root['SETTINGS']['PHYSICS']['nt']",
        'Number of time steps',
        default=1000,
    )
    OMFITx.Entry(
        "root['SETTINGS']['PHYSICS']['dt']",
        'Time step size (s)',
        default=5,
    )
    OMFITx.Entry(
        "root['SETTINGS']['PHYSICS']['temp']",
        'Coffee temperature (K)',
        default=396.15,
    )
    OMFITx.Entry(
        "root['SETTINGS']['PHYSICS']['mass']",
        'Milk particle mass (g)',
        default=3e-9,
    )
    OMFITx.Button(
        'Evolve model in time',
        root['SCRIPTS']['evolve'].run,
    )

    OMFITx.Separator()

    OMFITx.Entry(
        "root['SETTINGS']['EXPERIMENT']['time']",
        'Time to plot (s) (-1 does end of simulation, 0 does initial condition)',
        default=-1,
    )

    OMFITx.Button(
        'Plot distribution',
        root['PLOTS']['plot_distribution'].plot,
    )

OMFITx.CheckBox(
    "root['SETTINGS']['EXPERIMENT']['plot_after']",
    'Plot after doing important stuff',
)