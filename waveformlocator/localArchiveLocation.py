"""
This module contains the seedlink implementation for WaveformLocation
"""
import os

from obspy.core.stream import Stream

from quakedaemon.waveformLocation import WaveformLocation

class LocalArchiveLocation(WaveformLocation):
    def __init__(self, name, priority, file_path):
        WaveformLocation.__init__(self, name, priority)
        self.__file_path = file_path
        self.__station_info = []

    def requestWaveformTraces(self, requests):
        """
        Method for requesting data from WaveformLocation. Implement this to get waveform data.
        """
        streams = Stream()
        return streams

    def __checkStatus(self):
        """
        Function for checking the status of the local archive location and fetching all station related information from there  and saving it to station_info.
        """
        return os.path.isdir(self.__file_path)

    def getWaveformLocationStatus(self):
        """
        Ask if the seedlink location is listening and return the information to the user.
        """
        return {self.getName(): self.__checkStatus()}

