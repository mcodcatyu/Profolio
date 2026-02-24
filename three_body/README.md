## Project : Three-Body Orbital Simulation- Sun, Earth & Moon

###  Abstract 
This simulation models the Sun-Earth-Moon system using numerical integration to investigate how celestial mass influences orbital eccentricity and lunar periods. Numba is implemented to accelerate running speed. The project highlights the complexity of N-body interactions.


<div align="center">
<img width="464" height="319" alt="image" src="https://github.com/user-attachments/assets/d1c33eb3-adfb-4e21-b8aa-da3755919a17" />

  <p><i><b>Figure 1:</b> Initial values of position, velocity, and mass for the three-body system.</i></p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/8e1f5795-ccf0-4472-bfcd-4b8f7eaf859b" width="516">
  <p><i><b>Figure 2:</b> Governing equations for Gravitational Force, Acceleration, and Velocity.</i></p>
</div>

<div align="center">
  <img width="1002" height="536" alt="image" src="https://github.com/user-attachments/assets/121a5b2e-0696-4b09-80f2-b1b01119790b" />

  <p><i><b>Figure 3:</b> Earth's orbit around the Sun (left) and Earth-Moon orbital system (right).</i></p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/3c746115-34e2-4a60-abd5-90b70a2ce1e6" width="541">
  <p><i><b>Figure 4:</b> Distance variation over 180 days used to calculate the lunar orbital period.</i></p>
</div>

### Scientific Logic

**1. Visual Indicators & Trajectory**
* The Sun is marked with an orange dot, while green and red lines depict the Earth and the Moon respectively (Fig 3). The changing range of x and y values reveals that the Earth's orbit is not a perfect circle.
* The distance between two peaks, which is marked in orange(Fig 4), describes the orbital period of the Moon

**2. Lunar Period & Three-Body Dynamics**
* Increasing the Moon's mass shortens this period from 29 to 9 days (Fig 5), proving that in a three-body problem, even a slight change in one body affects the entire system's operation. The Moon completes one rotation every 29.74 days (Fig 6). 



<div align="center">
  <img src="https://github.com/user-attachments/assets/64897247-160a-4d0c-8942-15c5db4155d7" width="541">
  <p><i><b>Figure 5:</b> Correlation between Lunar Mass and Orbital Period.</i></p>
</div>

<div align="center">
  <img src="https://github.com/user-attachments/assets/9d82ab61-55ab-48dc-b63c-4e19cb239314" width="502">
  <p><i><b>Figure 6:</b> Sun-Earth-Moon angle variation used to identify the 12 full moon cycles per year.</i></p>
</div>

###  Comparison Table 
| Parameter| Simulation Result  | Physical Meaning |
| :--- | :--- | :--- |
| **Orbital Eccentricity** | **0.001180** | Earth's deviation from a perfect circle. |
| **Lunar Period** | **29.74 Days** | Time for Moon to orbit Earth (29.73 for full moon). |
| **Full Moons/Year** | **12 Times** | Frequency of Sun-Earth-Moon alignment ($180^\circ$). |

### Conclusion 
The Sun-Earth-Moon simulation serves as a prime example of three-body movement. It demonstrates that each body is interacted with others, and a slightly shift of one body can have impact on entire system operation.
