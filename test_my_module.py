import numpy as np
import signals as s
import pytest

def test_generate_sine_wave():
    t, y = s.generate_sine_wave(5, 2, 100)
    assert y[0] == 0

    t, y = s.generate_sine_wave(5, 0, 100)
    assert len(t) == 0 and len(y) == 0

    t, y = s.generate_sine_wave(0, 1, 10)
    assert np.allclose(y, 0)

def test_generate_sinc_wave():
    t, y = s.generate_sinc_wave(0, 10)
    assert len(t) == 0
    assert len(y) == 0

    t, y = s.generate_sinc_wave(1, 10)
    assert np.allclose(y, y[::-1])
    

def test_unit_step():
    assert s.unit_step(-1) == 0
    assert s.unit_step(0) == 1
    assert s.unit_step(5) == 1

    t = np.array([-2, -0.1, 0, 0.1, 3])
    result = s.unit_step(t)
    expected = np.array([0, 0, 1, 1, 1])
    assert all(result == expected)
    
    t = np.array([])
    y = s.unit_step(t)
    assert len(y) == 0


def test_unit_step2():
    assert s.unit_step2(-1) == 0
    assert s.unit_step2(0) == 2
    assert s.unit_step2(5) == 2

    t = np.array([-2, -0.1, 0, 0.1, 3])
    result = s.unit_step2(t)
    expected = np.array([0, 0, 2, 2, 2])
    assert all(result == expected)

    t = np.array([])
    y = s.unit_step2(t)
    assert len(y) == 0


def test_unit_pulse():
    t = np.array([-3, -2, -1, 0, 1, 2, 3])
    y = s.unit_pulse(t)
    assert y[0] == 0     
    assert y[3] == 2     
    assert y[-1] == 0

    assert s.unit_pulse(0) == 2
    assert s.unit_pulse(3) == 0
    assert s.unit_pulse(-3) == 0

    assert s.unit_pulse(100) == 0
    assert s.unit_pulse(-100) == 0