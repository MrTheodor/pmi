from distutils.core import setup
setup(name='pmi',
      version='1.0',
      py_modules=['pmi'],
      description='Parallel Method Invocation',
      author='Olaf Lenz',
      author_email='olenz@icp.uni-stuttgart.de',
      url='http://github.com/olenz/pmi/',
      download_url='http://github.com/olenz/pmi/downloads',
      keywords = ["mpi", "parallel"],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Environment :: Other Environment',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development :: Libraries',
        ' Topic :: System :: Clustering',
        ],
      license='GPL',
      platforms='OS Independent',
      long_description="""
Parallel Method Invocation
--------------------------

PMI is a pure python module that allows libraries to provide functions
that are parallelized using MPI but that can nontheless be called from
serial Python scripts.

PMI requires Python 2.4+ and is compatible to Python 3, furthermore it
requires a working MPI module (e.g. mpi4py or boostmpi).
""",
      )
