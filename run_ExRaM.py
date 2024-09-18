#=====================================================
# == Experimental Radar Model (ExRaM) - Run Model ==
#
# Author: Allen
# Date: 08/09/2024
#
# ** Currently in Development
#=====================================================

# Import Required Packages
import numpy as np
import matplotlib.pyplot as plt
from coordinateTransforms.functions import LLA2ECEF, ECEF2LLA


# Radar Parameters - Positioning & Orientation
radar = {}

radar['pos_ori'] = {}
radar['pos_ori']['geod_pos'] = [0,0,0]
radar['pos_ori']['ECEF_pos'] = LLA2ECEF(radar['posit_and_orient']['geod_pos'],'SPHERICAL')
radar['pos_ori']['boresight'] = [45,90]

# Radar Parameters - Transmit
radar['transmit'] = {}
radar['transmit']['peak_power'] = 1e3
radar['transmit']['peak_gain'] = 30
radar['transmit']['tx_loss'] = 7

# Radar Parameters - Waveform
radar['waveform'] = {}
radar['waveform']['sample_rate'] = 100e6
radar['waveform']['carrier_frequency'] = 9.4e9
radar['waveform']['bandwidth'] = 20e6
radar['waveform']['PRF'] = 10e3
radar['waveform']['pulse_width'] = 1e-6
radar['waveform']['modulation_type'] = 'LFM'

# Radar Parameters - Signal Processing
radar['sig_proc'] = {}
radar['sig_proc']['pulse_compression'] = {}
radar['sig_proc']['pulse_compression']['toggle'] = True
radar['sig_proc']['pulse_compression']['type'] = 'MF'

radar['sig_proc']['CFAR'] = {}
radar['sig_proc']['CFAR']['toggle'] = True
radar['sig_proc']['CFAR']['type'] = 'CA'

radar['sig_proc']['pulse_integration'] = {}
radar['sig_proc']['pulse_integration']['toggle'] = True
radar['sig_proc']['pulse_integration']['type'] = 'COHERENT'

# Scene Parameters
scene = {}
scene['noise_figure'] = 5
scene['atmos_atten'] = True

# Target Parameters
target = {}
target['range'] = 10e3
target['velocity'] = 100
target['RCS'] = 1
target['angle_offset_azi'] = 0
target['angle_offset_elev'] = 0


print(radar)
