
# Risk-Informed Model-Free Safe Control of LPV Systems

This repository contains code and documentation for the paper:

**Title**: Risk-Informed Model-Free Safe Control of Linear Parameter-Varying Systems  
**Authors**: Babak Esmaeili and Hamidreza Modares  
**Published in**: IEEE/CAA Journal of Automatica Sinica, Vol. 11, No. 9, Sept. 2024  
**DOI**: [10.1109/JAS.2024.124479](https://doi.org/10.1109/JAS.2024.124479)

---

## 🧠 Abstract

This paper presents a risk-informed data-driven safe control design approach for stochastic uncertain nonlinear systems modeled as LPV systems. A model-based probabilistic safe controller is first designed to guarantee probabilistic λ-contractivity of a given safe set. A direct data-driven representation of the closed-loop LPV system is then used to design a minimum-variance risk-averse safe controller that minimizes the variance of safety violations. Two practical examples are provided: (1) a magnetic suspension system computing safe-control gains to satisfy position/velocity constraints, and (2) a robotic vehicle path-tracking scenario where MATLAB-computed gains are deployed in a Python ROS 2 node for real-time safety-critical control, demonstrated in Gazebo simulation and real-world tests.

---

## 🎯 Overview

This work develops a robust, risk-informed, model-free safe control framework for LPV systems using only I/O data:
- **Data-driven closed-loop representation**: Bypass open-loop model identification by directly using collected state-input-scheduling data under gain-scheduling feedback.
- **Probabilistic safety**: Guarantee λ-contractivity of polyhedral safe sets in probability under Gaussian disturbances.
- **Risk-averse design**: Formulate and solve optimization (LP/SDP) to minimize variance of closed-loop behavior w.r.t. safe set, improving safety confidence.
- **Data efficiency**: Requires weaker data-richness conditions compared to model-based identification.
- **Practical validation**: Two examples demonstrate effectiveness:
  1. **Magnetic suspension system**: MATLAB scripts compute safe-control gains ensuring constraints on position and velocity.
  2. **Robotic vehicle path tracking**: MATLAB-computed gains are used in a Python ROS 2 node for real-time deployment on a mobile robot; includes Gazebo simulation and real-world experiments.

---



---

## 🛠 Requirements

- **MATLAB R2018a or newer**: for running MATLAB example scripts.
- **Python 3.8+**, **ROS 2** (e.g., Foxy/Galactic/Humble) and related packages: for deploying the ROS 2 node.
- **Gazebo**: for simulation of the robotic vehicle.
- **NumPy**, **rclpy**, **sensor_msgs**, **geometry_msgs**, etc.: Python dependencies for ROS 2 node.
- **YALMIP/MOSEK** or **CVX/MOSEK** in MATLAB: for solving LP in safe gain computation.
- A mobile robot platform compatible with ROS 2 for real-world validation.

---

## ▶️ Usage

### Example 1: Magnetic Suspension (MATLAB only)
1. Open MATLAB and navigate to `matlab/example1_magnetic_suspension/`.
2. Run `generate_data.m` to collect or simulate input-output data under perturbations.
3. Run `compute_safe_gains.m` to compute risk-informed safe-control gains ensuring constraints on position and velocity.
4. Run `simulate_suspension.m` to simulate closed-loop response and verify constraint satisfaction.
5. Inspect plots of trajectories and safe-set adherence.

---

## 📜 License and Contact

This project is licensed under the MIT License – see [LICENSE](LICENSE) for details.

For questions or collaboration, contact:
- **Babak Esmaeili** – esmaeil1@msu.edu

---

## 📚 Citation

If you use this repository, please cite:
```bibtex
@article{esmaeili2024riskinformed,
  title={Risk-Informed Model-Free Safe Control of Linear Parameter-Varying Systems},
  author={Esmaeili, Babak and Modares, Hamidreza},
  journal={IEEE/CAA Journal of Automatica Sinica},
  volume={11},
  number={9},
  pages={1918--1932},
  year={2024},
  doi={10.1109/JAS.2024.124479}
}
```

---

**Visuals**

![Gazebo Simulation](images/gazebo_simulation.png)  
*Gazebo environment for robotic vehicle path tracking.*

![Real-World Setup](images/real_world_setup.jpg)  
*Physical robot in its operating environment.*

Enjoy exploring risk-informed safe control for LPV systems with practical MATLAB and ROS 2 examples!
