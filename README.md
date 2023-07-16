# Schrödinger Equation Solver

This script solves the time-independent Schrödinger equation numerically using the finite difference method. It calculates and visualizes the probability density of a quantum particle in a one-dimensional potential barrier.

## Getting Started

### Prerequisites

To run this script, you need to have the following libraries installed:

- `numpy`
- `matplotlib`

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/Aganow/Schrodinger-Equation.git
   ```

2. Navigate to the project directory:

   ```
   cd schrodinger-equation-solver
   ```

3. Run the script:

   ```
   python schrodinger_equation.py
   ```

## Usage

1. Modify the parameters of the system, such as the length of the domain, the number of grid points, the potential barrier height and width, the time step, and the number of iterations, as needed.

2. Execute the script:

   ```
   python schrodinger_equation.py
   ```

3. The script will calculate the probability density of the quantum particle at each time step and plot it using `matplotlib`.

4. The plot will be continuously updated as the simulation progresses. You can adjust the animation speed by changing the value of `plt.pause()`.

## Acknowledgments

- The finite difference method implementation is based on the principles of numerical analysis.
- This script was created as a learning exercise and demonstration of the Schrödinger equation solver.
