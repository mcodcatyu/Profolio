# Project Overview
This project implements a computational simulation of the N-body problem, a fundamental challenge in physics describing particle motion under mutual forces.

# Key Objectives & Findings:
  - **Gravitational Modeling**: Simulated the dynamic orbits of the Sun, Earth, and Moon using Newton's law of universal gravitation.
  - **Orbital Analysis**: Successfully visualized Earth’s orbit around the Sun and the Moon’s complex path around the Earth, calculating critical metrics such as orbital eccentricity and orbital periods.
  - **Mass Sensitivity Studies**:  Demonstrated that fluctuations in Solar mass directly correlate with Earth's orbital eccentricity.Verified that the Moon's orbital period decreases as its mass increases.
  - **System Interaction**: Illustrated the intricate interdependence within an N-body system, highlighting how individual mass variations affect the stability of the entire gravitational web.

--------------------------------------------------------------------------------------------------
# Technical Implementation
- **High-Performance**: Implemented via Python & Numba to handle intensive numerical integration.
- **Numerical Method**: Utilized Runge-Kutta (or Euler-Cromer) methods for trajectory calculation.

## 🪐Simulations & Data
The following are the initial parameters, physical formulas, and dynamic demonstration results of the planetary motion simulation.

<div align="center">
  <img src="https://github.com/user-attachments/assets/13516103-5bf5-4903-88b3-128dbd6c76b9" width="458">
  <p><i>Initial values of position, velocity and mass for three planets</i></p>
</div>

<br/>

<div align="center">
  <img src="https://github.com/user-attachments/assets/8e1f5795-ccf0-4472-bfcd-4b8f7eaf859b" width="516">
  <p><i>Equations of Force, acceleration and velocity</i></p>
</div>

<br/>

<div align="center">
  <img src="https://github.com/user-attachments/assets/f9c08a96-630a-4103-a290-c133ea9f5e1c" width="539">
  <p><i>The Earth orbits around the Sun (left) and Orbits of the Earth and Moon (right)</i></p>
</div>

<br/>

<div align="center">
  <img src="https://github.com/user-attachments/assets/3c746115-34e2-4a60-abd5-90b70a2ce1e6" width="541">
  <p><i>The difference between the Moon-Sun and Earth-Sun distances over half a year</i></p>
</div>

<br/>

<div align="center">
  <video src="https://github.com/user-attachments/assets/c0c49a73-cf2d-47e3-a0f6-f3c60ea630fd" width="600" autoplay loop muted playsinline>
  </video>
  <p><b>Video Demo: The Earth’s orbit around Sun between 0.7 and 1.3 solar masses</b></p>
</div>

<br/>

<div align="center">
  <img src="https://github.com/user-attachments/assets/64897247-160a-4d0c-8942-15c5db4155d7" width="763">
  <p><i>Orbital period of the Moon around the Earth between 1 and 100 lunar masses</i></p>
</div>

<br/>

<div align="center">
  <img src="https://github.com/user-attachments/assets/9d82ab61-55ab-48dc-b63c-4e19cb239314" width="502">
  <p><i>Changes of angles between Sun-Earth-Moon during first year period</i></p>
</div>
