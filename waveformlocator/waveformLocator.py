import json
import os

from obspy.core.stream import Stream

from waveformlocator.waveformLocation import WaveformLocation
from waveformlocator.seedlinkLocation import SeedLinkLocation
from waveformlocator.cssArchiveLocation import CSSArchiveLocation

class WaveformLocator(object):
    """
    Main class for the waveform accessing service WaveformLocator. WaveformLocator fetches data from various configured locations and appends them together.

    WaveformLocator will have a list of WaveformLocation objects, which will be sorted by priority. These objects will be implemented separately. This list will be then iterated through when an getWaveforms function is called to request waveform data from all the different WaveformLocations.

    location_config is a path to a json file with the location configuration for this WaveformLocator.

    EXAMPLE WAVEFORMLOCATOR CONFIG FILE
    ###############################################
    {
        "waveformLocations":[
        {
            "name":"Example Seedlink",
            "type":"SeedLinkLocation",
            "server_name":"123.123.123.1"
            "priority":2
        },
        {
            "name":"Dummy Location",
            "type":"WaveformLocation",
            "priority":9
        },
        {
            "name":"Local archive",
            "type":"LocalArchiveLocation",
            "priority":1
        }
        ]
    }
    ###############################################
    """
    def __init__(self, location_config):
        self.__waveform_locations = []
        self.__readConfig(location_config)

    def __readConfig(self, location_config):
        """
        Read location_config json file and initialize the waveform_locations
        """
        config_file = open(location_config, 'r')
        settings = json.loads(config_file.read())
        config_file.close()

        for loc in settings['waveformLocations']:
            if loc['type'] == 'WaveformLocation':
                self.__waveform_locations.append(WaveformLocation(loc['name'], loc['priority']))
            elif loc['type'] == "SeedLinkLocation":
                self.__waveform_locations.append(SeedLinkLocation(loc['name'], loc['priority'], loc["server_name"]))
            #elif loc['type'] == "LocalArchiveLocation":
            #   self.__waveform_locations.append(LocalArchiveLocation(loc["server_name"], loc['name'], loc['file_path']))
            elif loc['type'] == "CSSArchiveLocation":
               self.__waveform_locations.append(CSSArchiveLocation(loc["name"], loc['priority'], loc['file_path']))

        self.__waveform_locations.sort(key=lambda x: x.getPriority())

    def getStatus(self):
        """
        Get current status of WaveformLocator waveform locations
        """
        current_status = dict()

        for loc in self.__waveform_locations:
            current_status.update(loc.getWaveformLocationStatus())

        return current_status

    def getEventWaveforms(self, event):
        """
        Get requested waveforms for a NorDB event
        """
        streams = Stream()

        for loc in self.__waveform_locations:
            new_streams = loc.requestEventWaveformTraces(event)
            if new_streams:
                streams += new_streams

        return streams

    def getWaveforms(self, requests):
        """
        Get requested waveforms from WaveformLocator
        """
        streams = Stream()
        for loc in self.__waveform_locations:
            new_streams = loc.requestWaveformTraces(requests)
            if new_streams:
                streams += new_streams

        return streams

