"""
Main script of the QuakeDaemon. Starts the waveform server
"""
import sys
import time

from obspy import UTCDateTime

from quakedaemon.waveformLocator import WaveformLocator
from quakedaemon.waveformRequest import WaveformRequest

from nordb import getNordic

if __name__ == "__main__":
    waveform_locator = WaveformLocator('example_config.json')
    start_date = UTCDateTime('2019/03/23 00:00:00.0000')

    while start_date < UTCDateTime()
        request = WaveformRequest('HE', 'OBF8', 'HNZ', start_date, 86400)
        print("Fetching waveforms: {0}".format(start_date))
        streams = waveform_locator.getWaveforms([request,])
        start_date += 86400

        for tr in streams:
            tr.write(tr.id + '.MSEED', format='MSEED')

