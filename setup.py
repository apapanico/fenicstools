#!/usr/bin/env python

from distutils.core import setup

# Version number
major = 2017
minor = 1

try:
    import dolfin
    import ufl
except ImportError as e:
    raise ImportError("fenicstools requires fenics/dolfin/ufl®")

setup(
    name="fenicstools",
    version="%d.%d" % (major, minor),
    description="fenicstools -- tools for postprocessing in FEniCS programs",
    author="Mikael Mortensen",
    author_email="mikaem@math.uio.no",
    url='https://github.com/mikaem/fenicstools.git',
    install_requires=[
        "mpi4py",
        "numpy",
        "matplotlib",
        "h5py",
        "pyvtk"
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.6',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=["fenicstools"],
    package_dir={"fenicstools": "fenicstools"},
    package_data={"fenicstools": ["Probe/*.h",
                                  "Probe/*.cpp",
                                  "fem/*.cpp",
                                  "dofmapplotter/*.py",
                                  "dofmapplotter/cpp/*.cpp"]},
)
