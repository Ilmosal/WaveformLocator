"""
This module contains the seedlink implementation for WaveformLocation
"""

import xml.etree.ElementTree as ET

from obspy import UTCDateTime
from obspy.clients.seedlink.easyseedlink import create_client
from obspy.clients.seedlink.basic_client import Client
from obspy.core.stream import Stream

from quakedaemon.waveformLocation import WaveformLocation

class SeedLinkLocation(WaveformLocation):
    def __init__(self, name, priority, server_name):
        WaveformLocation.__init__(self, name, priority)

        self.__server_name = server_name
        self.client = Client(self.__server_name)
        self.__station_info = []

    def requestWaveformTraces(self, requests):
        """
        Method for requesting data from WaveformLocation. Implement this to get waveform data.
        """
        streams = Stream()
        if self.__checkStatus():
            for request in requests:
                if not request.fulfilled():
                    #check if station_info contains a station the request is trying to access and its data starts soon enough to contain the stream
                    if [e for e in self.__station_info.findall('station') if e.attrib['name'] == request.station() and UTCDateTime(e.find("stream").attrib['begin_time']) < request.start_time()]:
                        for channel in request.channels():
                            new_stream = self.client.get_waveforms(request.network(), request.station(), '??', 'HH' + channel, request.start_time(), request.end_time())
                            streams += new_stream
                            request.fulfilRequest()

        return streams

    def __checkStatus(self):
        """
        Function for checking the status of the seedlink location and fetching all station related information from the seedlink server and saving it to station_info.
        """
        try:
            cl = create_client(self.__server_name)
        except:
            return False
        self.__station_info = ET.fromstring(cl.get_info('STREAMS'))
        cl.close()
        return True

    def getWaveformLocationStatus(self):
        """
        Ask if the seedlink location is listening and return the information to the user.
        """
        return {self.getName(): self.__checkStatus()}

