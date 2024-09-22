import numpy as np
import matplotlib.pyplot as plt

def GenerateTone(sample_frequency, pulse_width, amplitude, frequency, phase_offset):

    # Time Array
    pulse_time = np.arange(0,pulse_width,1/sample_frequency)
    
    # Calculating Instantaneous Phase and Generating the waveform
    instantaneous_phase = (2*np.pi*frequency*pulse_time)+phase_offset
    waveform = amplitude * np.exp(1j*instantaneous_phase)
    
    return pulse_time,waveform
    

if __name__ == '__main__':

    # Pulse Parameters
    sample_frequency = 200
    pulse_width = 5
    amplitude = 1
    tone_frequency = 20
    phase_offset = 0
    
    pulse_time,waveform = GenerateTone(sample_frequency, pulse_width, amplitude, tone_frequency, phase_offset)
    
    # Plotting the waveform
    plt.figure()
    plt.plot(pulse_time,waveform)
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title(f'Constant Tone Pulse - Frequency: {tone_frequency}Hz, Phase Offset: {phase_offset} rads')
    
    # Fast Fourier Transforming the waveform to determine the Spectral content
    waveform_fft = np.fft.fft(waveform)
    waveform_fft_shifted = np.fft.fftshift(waveform_fft)
    frequency_axis = np.arange(-sample_frequency/2, sample_frequency/2, sample_frequency/len(waveform_fft_shifted))
    
    # Plotting the spectral content of the waveform
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Spectral content of the Waveform')
    ax1.plot(frequency_axis, np.abs(waveform_fft_shifted))
    ax1.set_xlabel('Frequency (Hz)')
    ax1.set_ylabel('FFT of signal (Magnitude)')
    ax2.plot(frequency_axis, np.angle(waveform_fft_shifted))
    ax2.set_xlabel('Frequency (Hz)')
    ax2.set_ylabel('FFT of signal (Phase)')
 
    plt.show()