import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    t=np.linspace(0, duration, int(sample_rate*duration))
    y= np.sin(2*np.pi*frequency*t)
    return t, y

def unit_step(n):
    return np.heaviside(n,1)

def unit_step2(n2):
    return np.where(n2 < 0, 0, 2)

def unit_pulse(x):
    return np.where(np.abs(x) <= 0.5, 5, 0)