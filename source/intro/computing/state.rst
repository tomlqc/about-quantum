
State of the Art
================

- Hardware:

  - NISQ era (Noisy Intermediate-Scale Quantum Computers) :cite:`Preskill_2018`
  - | *Superconducting qubits: current state of play* :cite:`Kjaergaard_2020`

  - Challenges (*scale, quality, speed*):

    - number of qubits:
      more qubits on a chip, or "extend quantum systems with quantum optical channels" :cite:`QCE21_Gambetta`
    - quality of qubits:
      error-rate, coherence time
    - connectivity of qubits
    - data I/O: performance of loading classical data, faster read out (measurements)
    - control electronics:
      "Reduce the wiring: move the controller to cryogenic temperature (4K) - cryogenic CMOS"
      :cite:`QCE21_Clarke`

- Software:

  - ASM / Machine Instructions

  - | currently:
      *Variational Quantum Algorithms* or *Quantum Annealing*
      (see :ref:`intro/computing/algo:Quantum algorithms`)
    
  - Challenges:
    
    - *quantum compiler* (LLVM): optimization of qubit usage, "mapping & scheduling" :cite:`QCE21_Clarke`
    - error correction

- :ref:`intro/computing/algo:Quantum Supremacy`:

  - | Google's 2019 *Quantum Supremacy* claim with 53 qubits :cite:`Arute_2019` for an academic problem.

  - Estimate of the number of qubits to achieve *Quantum Supremacy* :cite:`Dalzell_2020`

      "An IQP circuit with 208 qubits, a QAOA circuit with 420 qubits,
      and a boson sampling circuit with 98 photons
      each would require at least one century to be simulated using a classical simulation algorithm"

  - | About quantum chemistry:
      *Gate-count estimates for performing quantum chemistry on small quantum computers?*
      :cite:`Wecker_2014`

  - | About optimization problems:
      `Where is the quantum advantage? <https://blog.xa0.de/post/Where-is-the-quantum-advantage%3F/>`_
      :cite:`Ratke_2021`

- Roadmaps:
  
  - `IBM’s Roadmap For Scaling Quantum Technology
    <https://www.ibm.com/blogs/research/2020/09/ibm-quantum-roadmap/>`_, Sep-15-2020
  - `IBM’s roadmap for building an open quantum software ecosystem
    <https://www.ibm.com/blogs/research/2021/02/quantum-development-roadmap/>`_, Feb-4-2021
  
- Balanced Opinions:
  
  - "Quantum Computing: A Bubble Ready to Burst?" :cite:`Brant_2020`,
  - "Will Quantum Computing Ever Live Up to Its Hype?" :cite:`Horgan_2021`

-----

**Further readings**

- "Status of quantum computer development"
  by the German Federal Office for Information Security :cite:`BSI_2020`
