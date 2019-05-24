"""
This module contains the seedlink implementation for WaveformLocation
"""
import os

from obspy.core.stream import Stream
from obspy.core.stream import read

from waveformlocator.waveformLocation import WaveformLocation

class CSSArchiveLocation(WaveformLocation):
    def __init__(self, name, priority, file_path):
        WaveformLocation.__init__(self, name, priority)
        self.__file_path = file_path
        self.__station_info = []

    def requestEventWaveformTraces(self, event):
        """
        Method for requesting event data from waveformLocation. Implement this to fetch event waveform data
        """
        streams = Stream()
        if self.__checkStatus() and event.waveform_h:
            wfdisc_file = event.waveform_h[0].waveform_info.lower()[4:]
            year = wfdisc_file[:4]
            yearjul = wfdisc_file[:7]
            if os.path.exists('{0}/{1}/{2}/{3}'.format(self.__file_path, year, yearjul, wfdisc_file)):
                streams += read('{0}/{1}/{2}/{3}'.format(self.__file_path, year, yearjul, wfdisc_file))

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

