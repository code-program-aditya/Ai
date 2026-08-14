import numpy as np
import matplotlib.pyplot as plt

# Enable interactive plotting
plt.ion()
fig, ax = plt.subplots(figsize=(10,5))

# Time axis (0 to 1 second, 500 points)
t = np.linspace(0, 1, 500)

# Run multiple frames to simulate "live" changes
for frame in range(50):
    # Original clean signal (5 Hz sine wave)
    original_signal = np.sin(2 * np.pi * 5 * t)

    # Spoofed signal: frequency shift + phase shift + random noise
    spoofed_signal = np.sin(2 * np.pi * 7 * t + np.pi/4) + 0.3 * np.random.randn(len(t))

    # Clear previous plot and redraw
    ax.clear()
    ax.plot(t, original_signal, label="Original Signal")
    ax.plot(t, spoofed_signal, label="Spoofed Signal", alpha=0.7)
    ax.set_title(f"Live Spoofing Simulation - Frame {frame+1}")
    ax.set_xlabel("Time")
    ax.set_ylabel("Amplitude")
    ax.legend()

    # Pause briefly to update the frame
    plt.pause(0.2)

# Turn off interactive mode and keep final plot open
plt.ioff()
plt.show()
