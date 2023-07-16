import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the system
L = 10     # Length of the domain
N = 1000   # Number of grid points
dx = L/N   # Grid spacing
x = np.linspace(0, L, N)   # Spatial grid
V0 = 10    # Height of the potential barrier
a = 4      # Width of the potential barrier

# Define the time-independent Schrödinger equation
def schrodinger_eqn(psi, x, V):
    d2psi = np.gradient(np.gradient(psi, dx), dx)
    return -0.5*d2psi + V*psi

# Define the potential energy function
def potential(x, V0, a):
    V = np.zeros_like(x)
    V[x > L/2-a/2] = V0
    V[x > L/2+a/2] = 0
    return V

# Set up the initial wave function
psi = np.zeros_like(x)
psi[x < L/4] = 1

# Set up the time step and number of iterations
dt = 0.001
nsteps = 1000

# Set up the plot
fig, ax = plt.subplots()

# Loop over time steps
for i in range(nsteps):
    
    # Calculate the potential energy
    V = potential(x, V0, a)
    
    # Calculate the next time step using the finite difference method
    psi_new = psi + dt*schrodinger_eqn(psi, x, V)
    
    # Normalize the wave function
    psi_new /= np.sqrt(np.trapz(abs(psi_new)**2, x))
    
    # Update the wave function
    psi = psi_new
    
    # Plot the wave function
    ax.plot(x, abs(psi)**2, color='black')
    
    # Set plot limits and labels
    ax.set_xlim(0, L)
    ax.set_ylim(0, 1)
    ax.set_xlabel('Position')
    ax.set_ylabel('Probability Density')
    
    # Show the plot
    plt.show(block=False)
    plt.pause(0.001)
    
