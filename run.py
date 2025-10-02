import signals as s
import matplotlib.pyplot as plt
import numpy as np

#sine wave
t,y=s.generate_sine_wave(5,2,100)

plt.figure()
plt.plot(t, y)
plt.title("Generated sine wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()

#sinc wave
t2,y2=s.generate_sinc_wave(4,250)

plt.figure()
plt.plot(t2, y2)
plt.title("Generated sinc wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()

#unit step
n=np.linspace(-5,5,1000)

plt.figure()
plt.plot(n, s.unit_step(n))
plt.title("Generated unit step 1")
plt.xlabel("Time (s)")
plt.ylabel("u(t)")
plt.grid(True)

plt.show()

#unit step2
n2=np.linspace(-2,2,1000)

plt.figure()
plt.plot(n2, s.unit_step2(n2))
plt.title("Generated unit step 2")
plt.xlabel("Time (s)")
plt.ylabel("u(t)")
plt.grid(True)

plt.show()

#unit pulse
x=np.linspace(-2,2,1000)

plt.figure()
plt.plot(x, s.unit_pulse(x))
plt.title("Generated unit pulse")
plt.xlabel("Time (s)")
plt.ylabel("$\Pi(t)$")
plt.grid(True)

plt.show()


