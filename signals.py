import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    t=np.linspace(0, duration, int(sample_rate*duration))
    y= np.sin(2*np.pi*frequency*t)
    """
    Generates sine wave function.

    Parameters:
        frequency: integer/float, frequency of the sine wave in Hz
        duration: integer/float, duration of the signal in s
        sample_rate: integer/float, amount of samples (points) per second in n/s
    
    Returns:
        t: integer/float, time array in s
        y: integer/float, sine wave function
    """
    return t, y

def generate_sinc_wave(duration1, sample_rate1):
    t= np.linspace((-1)*duration1, duration1, int(sample_rate1*duration1))
    y= np.sinc(t)
    """
    Generates sinc wave function.

    Parameters:
        duration1: integer/float, duration of the signal in s
        sample_rate1: integer/float, amount of samples (points) per second in n/s
    
    Returns:
        t: integer/float, time array in s with [-duration1, duration1]
        y: integer/float, sinc wave function
    """
    return t, y

def unit_step(t):
    """
    Generates unit step function using np.heaviside.

    Parameters:
       t: integer/float, time array in s

    Returns:
        unit step function
    """
    return np.heaviside(t,1)


def unit_step2(t):
    """
    Generates unit step function using np.where.

    Parameters:
       t: integer/float, time array in s

    Returns:
        unit step function
    """
    return np.where(t < 0, 0, 2)

def unit_pulse(t):
    """
    Generates unit pulse function using np.where.

    Parameters:
       t: integer/float, time array in s

    Returns:
        unit pulse function
    """
    return np.where(np.abs(0.5*t) <= 0.5, 2, 0)