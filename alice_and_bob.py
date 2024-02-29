from qiskit import QuantumCircuit, Aer, execute
from numpy.random import choice

# Constants
n = 10  # Number of qubits / bits in the key
bases_alice = [choice(['+', 'x']) for _ in range(n)]  # Alice's random bases
bases_bob = [choice(['+', 'x']) for _ in range(n)]  # Bob's random bases

# Function to prepare qubits
def prepare_qubits(circuit, qubit_idx, state, basis):
    if state == '1':
        circuit.x(qubit_idx)
    if basis == 'x':
        circuit.h(qubit_idx)

# Function to measure qubits
def measure_qubits(circuit, qubit_idx, basis):
    if basis == 'x':
        circuit.h(qubit_idx)
    circuit.measure(qubit_idx, qubit_idx)

# Preparing quantum circuit
qc = QuantumCircuit(n, n)

# Alice prepares qubits
for i in range(n):
    state = choice(['0', '1'])  # Random bit
    prepare_qubits(qc, i, state, bases_alice[i])

# Bob measures qubits
for i in range(n):
    measure_qubits(qc, i, bases_bob[i])

# Execute the circuit
backend = Aer.get_backend('qasm_simulator')
results = execute(qc, backend, shots=1).result()
measurements = results.get_counts()

# Extracting the key
key = list(measurements.keys())[0]  # The measured key
key_alice_bob = ''.join([key[i] for i in range(n) if bases_alice[i] == bases_bob[i]])

print("Shared key (where bases matched):", key_alice_bob)