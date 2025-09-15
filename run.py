import signals as s
print(s.generate_sine_wave(5, 2, 100)[0:10])

import matplotlib.pyplot as plt

t,y=s.generate_sine_wave(5,2,100)

plt.plot(t, y)
plt.title("Generated sine wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()
