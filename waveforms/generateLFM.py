import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    
    # Pulse Parameters
    sample_frequency = 200
    pulse_width = 5
    amplitude = 1
    centre_frequency = 20
    bandwidth = 5
    phase_offset = 0
    
    # Time Array
    pulse_time = np.arange(0,pulse_width,1/sample_frequency)
    
    # Calculating Instantaneous Phase and Generating the waveform
    frequency_gradient = bandwidth/pulse_width
    chirp_rate = frequency_gradient*pulse_time
    instantaneous_phase = (2*np.pi*chirp_rate*pulse_time)+phase_offset
    waveform = amplitude * np.exp(1j*instantaneous_phase)
    
    # Fast Fourier Transforming the waveform to determine the Spectral content
    waveform_fft = np.fft.fft(waveform)
    waveform_fft_shifted = np.fft.fftshift(waveform_fft)
    frequency_axis = np.arange(-sample_frequency/2, sample_frequency/2, sample_frequency/len(waveform_fft_shifted))
    
    # Plotting the waveform
    plt.figure(1)
    plt.plot(pulse_time,waveform)
    plt.xlabel('time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'Linear Frequency Modulated (LFM) pulse - Centre Frequency: {centre_frequency}Hz, Bandwidth: {bandwidth}Hz')
    
    # Plotting the spectral content of the waveform
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('spectral content of the LFM waveform')
    ax1.plot(frequency_axis, np.abs(waveform_fft_shifted))
    ax1.set_xlabel('frequency (Hz)')
    ax1.set_ylabel('FFT of signal (Magnitude)')
    ax2.plot(frequency_axis, np.angle(waveform_fft_shifted))
    ax2.set_xlabel('frequency (Hz)')
    ax2.set_ylabel('FFT of signal (Phase)')
    
    plt.show()
