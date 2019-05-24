"""
This module contains WaveformLocation object definition
"""

from obspy.core.stream import Stream

class WaveformLocation(object):
    """
    Implementation of WaveformLocation class. Inherit this class when creating a new waveform location class.
    """
    def __init__(self, name, priority):
        self.__name = name
        self.__priority = priority

    def requestWaveformTraces(self, requests):
        """
        Method for requesting data from WaveformLocation. Implement this to get waveform data.
        """
        stream = Stream()
        return stream

    def requestEventWaveformTraces(self, event):
        """
        Method for requesting event data from waveformLocation. Implement this to fetch event waveform data
        """
        stream = Stream()
        return stream

    def getWaveformLocationStatus(self):
        """
        Ask if waveform location is listening.
        """
        return {self.__name: False}

    def getPriority(self):
        """
        Get the priority of the WaveformLocation object
        """
        return self.__priority

    def getName(self):
        return self.__name
