"""
Class for encapsulating waveform requests
"""
class WaveformRequest(object):
    def __init__(self, network, station, channels, start_time, length):
        self.__network = network
        self.__station = station
        self.__channels = channels
        self.__start_time = start_time
        self.__end_time = start_time + length
        self.__fulfilled = False

    def network(self):
        return self.__network

    def station(self):
        return self.__station

    def channels(self):
        return self.__channels

    def start_time(self):
        return self.__start_time

    def end_time(self):
        return self.__end_time

    def fulfilled(self):
        return self.__fulfilled

    def fulfilRequest(self):
        self.__fulfilled = True

