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
t,y=s.generate_sinc_wave(4,250)

plt.figure()
plt.plot(t, y)
plt.title("Generated sinc wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)

plt.show()

#unit step
t=np.linspace(-2,2,1000)

plt.figure()
plt.plot(t, s.unit_step(t))
plt.title("Generated unit step 1")
plt.xlabel("Time (s)")
plt.ylabel("u(t)")
plt.grid(True)

plt.show()

#unit step2
t=np.linspace(-2,2,1000)

plt.figure()
plt.plot(t, s.unit_step2(t))
plt.title("Generated unit step 2")
plt.xlabel("Time (s)")
plt.ylabel("u(t)")
plt.grid(True)

plt.show()

#unit pulse
t=np.linspace(-2,2,1000)

plt.figure()
plt.plot(t, s.unit_pulse(t))
plt.title("Generated unit pulse")
plt.xlabel("Time (s)")
plt.ylabel("$\Pi(t)$")
plt.grid(True)

plt.show()

#unit step shifted + scaled
t=np.linspace(2,6,1000)

plt.figure()
plt.plot(t, s.unit_step((t-4)*(-3)))
plt.title("$-3 \cdot u(t-4)$")
plt.xlabel("Time (s)")
plt.ylabel("u(t)")
plt.grid(True)

plt.show()

#unit step + unit pulse
t=np.linspace(-2,6,1000)

plt.figure()
plt.plot(t, s.unit_step((t-4)*(-3)) + s.unit_pulse(t-1))
plt.title("$-3 \cdot u(t-4)$ + $\Pi(t-1)$")
plt.xlabel("Time (s)")
plt.ylabel("x(t)")
plt.grid(True)

plt.show()