"""
"""
import sys
import time

from obspy import UTCDateTime

from waveform_locator.waveformLocator import WaveformLocator
from waveform_locator.waveformRequest import WaveformRequest

from nordb import getNordic

if __name__ == "__main__":
    waveform_locator = WaveformLocator('example_config.json')
    start_date = UTCDateTime('2018/10/01 00:00:00.0000')

    while start_date < UTCDateTime():
        try:
            request = WaveformRequest('HE', 'OBF8', 'ENZ', start_date, 86400)
            print("Fetching waveforms: {0}".format(start_date))
            streams = waveform_locator.getWaveforms([request,])
            start_date += 86400

            for tr in streams:
                tr.write('/levy/ilmosalm/tietokantajutut/obf8_waves/{0}.{1}{2:03d}'.format(tr.id, start_date.year, start_date.julday), format='MSEED')
        except Exception as e:
            print("Exception occurred: {0}. Waiting for 10 seconds and trying again".format(e))
            time.sleep(10)
