
Quantum Chemistry
=================

.. ---------------------------------------------------------------------------

.. rubric:: Simulation

- Quantum Chemistry, :cite:`IQCQH_2020`, Lectures 22-27

- *Simulating Chemistry* :cite:`Kassal_2011`
  
  - reaction rates
  - molecular structure

- "energy derivates for quantum chemistry" :cite:`OBrien_2019`

- **Digital Simulation**: *Hardware-efficient VQE for small molecules*: :cite:`Kandala_2017`
  "superconducting Josephson junction (JJ) based qubits [...]
  includes 6 fixed frequency transmon qubits and a central flux-tunable asymmetric transmon qubit "

- **Analog Simulation**: *Analog quantum chemistry simulation* :cite:`ArguelloLuengo_2019`,
  with ultracold atoms in optical lattices and cavity quantum electrodynamics

.. ---------------------------------------------------------------------------

.. rubric:: Variational Quantum Eigensolver

- Lecture 19 :cite:`LMUQH2021`:, *VQE for small molecules* :cite:`Kandala_2017`

  - VQE compute energy with quantum computer, optimize parameters classically
  - makes sense if "computation of energy of trial state cannot be done efficiently with a classical computer",
  - need to map the electronic structure of the molecule (fermionic problem, atomic orbitals)
    to the gate-based quantum (single and two-qubits gates)

- "a variational quantum eigensolver (VQE) simulation of two intermediate-scale chemistry problems:
  the binding energy of hydrogen chains (as large as H12) and the isomerization mechanism of diazene"
  :cite:`Arute_2020`

- go further: "faster quantum gradient computation" :cite:`Gilyen_2019`

.. ---------------------------------------------------------------------------
