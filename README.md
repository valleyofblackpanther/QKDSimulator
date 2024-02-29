# Quantum Key Distribution Simulator

This project is a simple simulation of a quantum key distribution (QKD) system using Qiskit, a quantum computing framework. The simulation demonstrates the generation of a shared secret key between two parties, Alice and Bob, using quantum principles. It leverages the no-cloning theorem and the uncertainty principle to ensure the security of the key distribution process.

## Features

- Simulation of quantum key distribution using random bases.
- Generation of a shared secret key between two parties.
- Use of Qiskit for quantum circuit simulation.

## Prerequisites

Before running this simulation, you will need to have Python installed on your system. Additionally, the Qiskit library and NumPy must be installed. These can be installed using pip:

```bash
pip install qiskit numpy
```

## Usage

The script performs the following steps to simulate quantum key distribution:

1. **Initialization**: Sets up the number of qubits/bits for the key and randomly selects bases for Alice and Bob.
2. **Qubit Preparation**: Alice prepares qubits in random states ('0' or '1') according to her bases.
3. **Measurement**: Bob measures the qubits according to his bases.
4. **Key Extraction**: A shared key is extracted where Alice's and Bob's bases match.

To run the simulation, simply execute the script:

```bash
python alice_and_bob.py
```

Output will display the shared key where Alice's and Bob's measurement bases matched.

## Code Structure

- `prepare_qubits(circuit, qubit_idx, state, basis)`: Function to prepare qubits in a specified state and basis.
- `measure_qubits(circuit, qubit_idx, basis)`: Function to measure qubits in a specified basis.
- The main script initializes the quantum circuit, prepares and measures qubits, executes the circuit, and extracts the shared key.
