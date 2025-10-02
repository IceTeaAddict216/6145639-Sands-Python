import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    t=np.linspace(0, duration, int(sample_rate*duration))
    y= np.sin(2*np.pi*frequency*t)
    return t, y

def generate_sinc_wave(duration1, sample_rate1):
    t= np.linspace((-1)*duration1, duration1, int(sample_rate1*duration1))
    y= np.sinc(t)
    return t, y

def unit_step(t):
    return np.heaviside(t,1)

def unit_step2(t):
    return np.where(t < 0, 0, 2)

def unit_pulse(t):
    return np.where(np.abs(0.5*t) <= 0.5, 2, 0)