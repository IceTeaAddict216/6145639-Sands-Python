# Signals and Systems
This repository contains scripts to generate and visualise basic signals and to modify them. It is for the course Signals and Systems AESB2122-24 from the Applied Earth Sciences program at TU Delft.

## Table of Contents
- [Description](#description)
- [Structure](#structure)
- [Installation](#installation)
- [How to use](#how-to-use)
- [Example](#example)

## Description
Python functions are provided to create standard signals such as sine waves, sinc, unit step and unit pulse functions. These are then plotted and modified (time scaling/shifting, addition and multiplication).

## Structure
| File | Description |
|------|--------------|
| ```signals.py``` | Library with defined functions |
| ```run.py``` | Script that plots and modifies the signals |
| ```test_my_module.py``` | Unit tests to verify signal functions |
| ```hellooo.py``` | A very kind print statement C: |
| ```pyproject.toml``` | Project configuration file |
| ```README.md``` | Project documentation |

## Installation
1. Download the project:
    ```git clone https://github.com/IceTeaAddict216/6145639-sands-python.git```
2. Open the folder:
    ```cd 6145639-sands-python```
3. Install required dependencies:
    ```pip install```

## How to use
1. Run the program:
    ```python run.py```
    This will open plots for each generated signal and modifies them
2. Run the tests (optional):
    ```python -m pytest```
    This checks if the functions work properly. If they do, the terminal will show the following:
    ![Passed test](passed_test.png)
    
## Example
```python
import signals as s
import matplotlib.pyplot as plt
import numpy as np

t, y = s.generate_sine_wave(frequency=5, duration=2, sample_rate=100)

plt.figure()
plt.plot(t, y)
plt.title("Generated sine wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
```
 ![Example plot](Example_plot.png)