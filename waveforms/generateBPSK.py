import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':

    # Pulse Parameters
    chip_sequence = [1,-1,-1]
    pulse_width = 5
    amplitude = 1
    centre_frequency = 2
    phase_offset = 0
    sample_frequency =20*len(chip_sequence)*centre_frequency
    
    # Time Array and zero array to store pulse
    pulse_time = np.arange(0,pulse_width,1/sample_frequency)
    waveform = np.zeros((len(pulse_time)))
        
    # Calculating Instantaneous Phase and Generating the waveform
    instantaneous_phase = (2*np.pi*centre_frequency*pulse_time)+phase_offset
    for i in range(0,(len(pulse_time)-len(chip_sequence)),len(chip_sequence)):
        for j in range(0,len(chip_sequence)):
            waveform[i+j] = chip_sequence[j]*amplitude * np.exp(1j*instantaneous_phase[i+j])
            
    # Plotting the waveform
    plt.figure(1)
    plt.plot(pulse_time,waveform)
    plt.xlabel('time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'constant tone pulse at {centre_frequency}Hz, seeded with a {len(chip_sequence)} chip BPSK sequence')
    
    # Modelling a burst of pulses with varying PRIs
    PRIs = [20,23,18,17,21]
    
    burst = {}
    for iPulse in range(0,len(PRIs)):
        burst[f'{iPulse}'] = {}
        burst[f'{iPulse}']['time'] = np.arange(0,PRIs[iPulse],1/sample_frequency)
        burst[f'{iPulse}']['signal'] = np.zeros(((sample_frequency*PRIs[iPulse]),1))
        burst[f'{iPulse}']['signal'][0:len(waveform),0] = waveform
    
    # Plotting the burst of pulses
    plt.figure(2)
    plt.plot(burst['3']['time'],burst['3']['signal'])
    plt.xlabel('time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'A single PRI')

    # Fast Fourier Transforming the waveform to determine the Spectral content
    waveform_fft = np.fft.fft(waveform)
    waveform_fft_shifted = np.fft.fftshift(waveform_fft)
    frequency_axis = np.arange(-sample_frequency/2, sample_frequency/2, sample_frequency/len(waveform_fft_shifted))
    
    # Plotting the spectral content of the waveform
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('spectral content of the contant tone waveform')
    ax1.plot(frequency_axis, np.abs(waveform_fft_shifted))
    ax1.set_xlabel('frequency (Hz)')
    ax1.set_ylabel('FFT of signal (Magnitude)')
    ax2.plot(frequency_axis, np.angle(waveform_fft_shifted))
    ax2.set_xlabel('frequency (Hz)')
    ax2.set_ylabel('FFT of signal (Phase)')
 
    plt.show()