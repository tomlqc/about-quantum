
*****************
Quantum Computing
*****************

.. rubric:: Contents

- Feynman's original idea, Di Vincenzo "ingredients"

- Theory: universal set of gates
- Gates, Circuits
- alternative models to Gate-Based Computers: Quantum Annealing

- Noise
- Quantum Error Correction
- Fault-tolerant Algorithms


- Complexity: Problems solved more efficiently on quantum computers.
- Algorithms
  
  * QFT > Phase Estimation > Shor (RSA) etc.
  * Grover


- Overview of Implementations:

  * see references below: NMR, QED, Ion traps, Quantum dots, Superconducting Qubits

- Superconducting: Physical architecture
- NISQ era (Noisy Intermediate-Scale Quantum Computers)
- State of the Art: ASM/Machine Instructions

.. rubric:: References

- Quantum dots:

  - electron spin qubits
  - seminal paper :cite:`Loss_1998`
  - foundry-fabricated quantum dots :cite:`Ansaloni_2020` (Copenhagen/CEA), hot chips :cite:`Petit_2020` (TU-Delft)
  - see also lecture at Jülich :cite:`Meyer_2009`
  - technology favoured by Intel :cite:`Russell_2020`, :cite:`Clarke_2020`
  - QH lecture 19 :cite:`LMUQH2021`

    - charge sensing :cite:`Vandersypen_2004`
    - single-shot spin read-out :cite:`Elzerman_2004`

- Superconducting Qubits:
  
  - "anharmonic oscillators (AHOs) constructed from superconducting circuit element"
  - review paper: engineer's guide :cite:`Krantz_2019`, state of play :cite:`Kjaergaard_2020`
  - implemented by Google, IBM, Rigetti
