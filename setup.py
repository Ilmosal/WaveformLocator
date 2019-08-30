# -*- coding: utf8 -*-
from setuptools import setup, find_packages

setup(
    name="WaveformLocator",
    author="Ilmo Salmenperä",
    author_email="ilmo.salmenpera@helsinki.fi",
    packages=find_packages(),
    include_package_data=True,
    url="http://github.com/MrCubanfrog/WaveformLocator",
    license="LICENSE",
    description="Python library for fetching waveform data from various sources",
    install_requires=[
        "obspy",
        "nordb",
        "lxml"
    ],
    long_description=open("README.md").read(),
)
