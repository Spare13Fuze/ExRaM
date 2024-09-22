import numpy as np
import matplotlib.pyplot as plt
import warnings

def GenerateLFM(sample_frequency,pulse_width,amplitude,centre_frequency,bandwidth,phase_offset,up_or_down):

    # Time Array
    pulse_time = np.arange(0,pulse_width,1/sample_frequency)
    
    # Calculating Instantaneous Phase and Generating the waveform
    frequency_gradient = bandwidth/pulse_width
    chirp_frequency = frequency_gradient*(2*pulse_time)
    
    # If LFM frequency increases over time...
    if up_or_down == 'UP':
        instantaneous_frequency = centre_frequency+chirp_frequency
        instantaneous_phase = (2*np.pi*instantaneous_frequency*pulse_time)+phase_offset
        
    # If LFM frequency decreases over time...
    elif up_or_down == 'DOWN':
        instantaneous_frequency = centre_frequency-chirp_frequency
        instantaneous_phase = (2*np.pi*instantaneous_frequency*pulse_time)+phase_offset
        phase_gradient = np.gradient(instantaneous_phase)
        
        # Frequency Wrapping Check
        if phase_gradient[-1] < 0:
            warnings.warn('The LFM down chirp at the set parameters will encounter frequency wrapping.', stacklevel=2)
            plt.figure()
            plt.plot(pulse_time,instantaneous_phase)
            
    else:
        raise ValueError("Invalid specifier. 'UP' = Up Chirp, 'DOWN' = Down Chirp.")
        
    waveform = amplitude * np.exp(1j*instantaneous_phase)
    
    return pulse_time,waveform



if __name__ == "__main__":
    
    # Pulse Parameters
    sample_frequency = 1000
    pulse_width = 10
    amplitude = 1
    centre_frequency = 40
    bandwidth = 10
    phase_offset = 0
    up_or_down = 'UP'
    
    pulse_time,waveform = GenerateLFM(sample_frequency,pulse_width,amplitude,centre_frequency,bandwidth,phase_offset,up_or_down)
    
    # Plotting the waveform
    plt.figure()
    plt.plot(pulse_time,waveform)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'Linear Frequency Modulated (LFM) pulse - Centre Frequency: {centre_frequency}Hz, Bandwidth: {bandwidth}Hz')
    
    # Fast Fourier Transforming the waveform to determine the Spectral content
    waveform_fft = np.fft.fft(waveform)
    waveform_fft_shifted = np.fft.fftshift(waveform_fft)
    frequency_axis = np.arange(-sample_frequency/2, sample_frequency/2, sample_frequency/len(waveform_fft_shifted))
    
    # Plotting the spectral content of the waveform
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('spectral content of the LFM waveform')
    ax1.plot(frequency_axis, np.abs(waveform_fft_shifted))
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('FFT of signal (Magnitude)')
    ax2.plot(frequency_axis, np.angle(waveform_fft_shifted))
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('FFT of signal (Phase)')
    
    plt.show()
