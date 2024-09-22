import numpy as np
import matplotlib.pyplot as plt
import warnings

def GenerateRandBPSK(sample_frequency,pulse_width,amplitude,frequency,phase_offset,num_chips):
    
    # Undersampling warning
    minimum_sample_frequency = 20*num_chips*frequency
    if sample_frequency < minimum_sample_frequency:
        warnings.warn(f'A minimum sample frequency of {minimum_sample_frequency}Hz is suggested to prevent under-sampling.',stacklevel=2)
    
    # Time Array and zero array to store pulse
    pulse_time = np.arange(0,pulse_width,1/sample_frequency)
    waveform = np.zeros((len(pulse_time)))
    phase_modulation = np.zeros((len(pulse_time)))
    
    chip_sequence = np.random.choice([1,-1],size=num_chips)
    
    # Calculating Instantaneous Phase and Generating the waveform
    instantaneous_phase = (2*np.pi*frequency*pulse_time)+phase_offset
    for i in range(0,(len(pulse_time)-len(chip_sequence)),len(chip_sequence)):
        for j in range(0,len(chip_sequence)):
            phase_modulation [i+j] = chip_sequence[j]
            waveform[i+j] = chip_sequence[j]*amplitude * np.exp(1j*instantaneous_phase[i+j])
    
    return pulse_time,waveform,phase_modulation

if __name__ == '__main__':

    # Pulse Parameters
    num_chips = 15
    pulse_width = 5
    amplitude = 1
    centre_frequency = 20
    phase_offset = 0
    sample_frequency = 121
    
    pulse_time,waveform,phase_modulation = GenerateRandBPSK(sample_frequency,pulse_width,amplitude,centre_frequency,phase_offset,num_chips)
            
    # Plotting the waveform
    plt.figure(1)
    plt.plot(pulse_time,waveform)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'constant tone pulse at {centre_frequency}Hz, seeded with a {num_chips} chip BPSK sequence')
    
    plt.figure()
    plt.plot(pulse_time,phase_modulation)
    plt.xlabel('Time (s)')
    plt.ylabel('Binary Phase Chip (1/-1)')
    plt.title(f'Waveform Phase Chip Sequence')

    # Fast Fourier Transforming the waveform to determine the Spectral content
    waveform_fft = np.fft.fft(waveform)
    waveform_fft_shifted = np.fft.fftshift(waveform_fft)
    frequency_axis = np.arange(-sample_frequency/2, sample_frequency/2, sample_frequency/len(waveform_fft_shifted))
    
    # Plotting the spectral content of the waveform
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Spectral Content of the Waveform')
    ax1.plot(frequency_axis, np.abs(waveform_fft_shifted))
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('FFT of signal (Magnitude)')
    ax2.plot(frequency_axis, np.angle(waveform_fft_shifted))
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('FFT of signal (Phase)')
 
    plt.show()