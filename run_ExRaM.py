# == Radar Simulation Test ==

# Author: Allen
# Date: 08/09/2024

# ** Currently in Development

# Radar Parameters - Positioning & Orientation
radar = {}
radar['geod_pos'] = [0,0,0]
radar['boresight'] = [45,90]

# Radar Parameters - Waveform
radar['waveform'] = 'LFM'
radar['sample_rate'] = 100e6
radar['carrier_frequency'] = 9.4e9
radar['bandwidth'] = 20e6
radar['PRF'] = 10e3
radar['pulse_width'] = 1e-6
radar['tx_power'] = 1e3
radar['tx_antenna_gain'] = 30

print(radar)
