#
# UFS-workflow
#
# setup.py - Python setuptools integration
#

import setuptools
import os


setuptools.setup(
    name='ufs-workflow',
    version='0.0.1',
    author='NOAA-EMC',
    description='Workflows for UFS Applications',
    url='https://github.com/noaa-emc/ufs-workflow',
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: GNU Lesser General Public License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Operating System :: MacOS'],
    python_requires='>=3.6',
    install_requires=[
        'pyyaml>=5.3.1',
        'solo@git+https://github.com/JCSDA-internal/solo.git',
        'r2d2@git+https://github.com/JCSDA-internal/r2d2.git',
        'ewok@git+https://github.com/JCSDA-internal/ewok.git',
    ],
    package_data={
        '': [
           'hosts/*.yaml',
           'workflows/ecflow/tasks/*.ecf',
           'workflows/ecflow/include/*.h',
           'tasks/*.sh'
        ]
    },
    include_package_data=True,
)
