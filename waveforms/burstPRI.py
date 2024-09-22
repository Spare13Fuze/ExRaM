import numpy as np
import matplotlib.pyplot as plt
import warnings

def BurstSinglePRI(sample_frequency,num_pulses,PRI,waveform):
    
    burst = {}
    for iPulse in range(0,num_pulses):
        burst[f'{iPulse}'] = {}
        burst[f'{iPulse}']['time'] = np.arange(0,PRI,1/sample_frequency)
        burst[f'{iPulse}']['signal'] = np.zeros(((sample_frequency*PRI),1))
        burst[f'{iPulse}']['signal'][0:len(waveform),0] = waveform
        
    return burst
    
def BurstVariablePRI(sample_frequency,PRI,waveform):

    burst = {}
    for iPulse in range(0,len(PRI)):
        burst[f'{iPulse}'] = {}
        burst[f'{iPulse}']['time'] = np.arange(0,PRI[iPulse],1/sample_frequency)
        burst[f'{iPulse}']['signal'] = np.zeros(((sample_frequency*PRI[iPulse]),1))
        burst[f'{iPulse}']['signal'][0:len(waveform),0] = waveform

    return burst 

    
if __name__ == '__main__':

    from generateLFM import GenerateLFM
    
    single_or_variable = 'VARIABLE'
    PRI_to_plot = 0
    
    # Pulse Parameters
    sample_frequency = 1000
    pulse_width = 10
    amplitude = 1
    centre_frequency = 40
    bandwidth = 10
    phase_offset = 0
    up_or_down = 'UP'
    
    pulse_time,waveform = GenerateLFM(sample_frequency,pulse_width,amplitude,centre_frequency,bandwidth,phase_offset,up_or_down)
    
    if single_or_variable == 'SINGLE':
        num_pulses = 5
        PRI = 25
        burst = BurstSinglePRI(sample_frequency,num_pulses,PRI,waveform)
        
        # Plotting the burst of pulses
        plt.figure()
        plt.plot(burst[f'{PRI_to_plot}']['time'],burst[f'{PRI_to_plot}']['signal'])
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title(f'Pulse {PRI_to_plot+1}: PRI = {PRI} secs')
        
    elif single_or_variable == 'VARIABLE':
        PRI = [20,23,18,17,21]
        burst = BurstVariablePRI(sample_frequency,PRI,waveform)
        
        # Plotting the burst of pulses
        plt.figure()
        plt.plot(burst[f'{PRI_to_plot}']['time'],burst[f'{PRI_to_plot}']['signal'])
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.title(f'Pulse {PRI_to_plot+1}: PRI = {PRI[PRI_to_plot]} Secs')

    plt.show()