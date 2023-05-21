
State of the Art
================

.. contents::
    :local:

-----

Hardware
--------

- NISQ era (Noisy Intermediate-Scale Quantum Computers) :cite:`Preskill_2018`

- | *Superconducting qubits: current state of play* :cite:`Kjaergaard_2020`

- Challenges (*scale, quality, speed*):

  - number of qubits:
    more qubits on a chip, or "extend quantum systems with quantum optical channels" :cite:`QCE21_Gambetta`,
    see also *Entanglement across separate silicon dies* :cite:`Gold_2021` 
  - quality of qubits:
    error-rate, coherence time
  - manufacturing:
    e.g. avoid defects introducting splitting of levels :cite:`QCE21_Reagor`
  - connectivity of qubits:
    strong impact on performance,
    (but simple ladder connectivity may be good enough for current hardware :cite:`Holmes_2020`
    :cite:`QCE21_Matsuura`)
  - data I/O: performance of loading classical data, faster read out (measurements) :cite:`QCE21_Matsuura`
  - control electronics:
    "Reduce the wiring: move the controller to cryogenic temperature (4K) - cryogenic CMOS"
    :cite:`QCE21_Clarke`


Software
--------

- | ASM / Machine Instructions

- | currently *Variational Quantum Algorithms* or *Quantum Annealing*:
  
  - see :ref:`intro/computing/algo:Algorithms`,
    also :ref:`reviews/ieee_qce21:Quantum Approximate Optimization` in QAOA.
  
- Challenges:
  
  - *quantum compiler* (LLVM): optimization of qubit usage,
    "mapping & scheduling" :cite:`QCE21_Clarke`,
    "randomized compiling" :cite:`QCE21_Emerson`
  - **Error correction**


Quantum Advantage
-----------------

Also refered to as **Quantum Supremacy** e.g. by Google.
The term **Quantum Advantage** was preferred by IBM.

- | Google's 2019 *Quantum Supremacy* claim with 53 qubits :cite:`Arute_2019` for an academic problem.

- | More from Google AI Quantum Research in the dedicated section:
    :ref:`reviews/google:Quantum Advantage`

- Estimate of the number of qubits to achieve *Quantum Supremacy* (2020) :cite:`Dalzell_2020`

    "An IQP circuit with 208 qubits, a QAOA circuit with 420 qubits,
    and a boson sampling circuit with 98 photons
    each would require at least one century to be simulated using a classical simulation algorithm"

- | Focus beyond Quadratic Speedups for Error-Corrected Quantum Advantage (2021) :cite:`Babbush_2021`

    "We discuss conditions under which it would be possible for a modest fault-tolerant quantum computer
    to realize a runtime advantage by executing a quantum algorithm with only a small polynomial speedup
    over the best classical alternative. [...]
    We conclude that quadratic speedups will not enable quantum advantage on early generations
    of such fault-tolerant devices unless there is a significant improvement in how we realize quantum error correction."

- | About **quantum chemistry**:
    *Gate-count estimates for performing quantum chemistry on small quantum computers?* (2014)
    :cite:`Wecker_2014`

- | About **quantum machine learning**:
    *Quantum advantage in learning from experiments* (2022) :cite:`Huang_2022`

- | About **optimization problems**:
    `Where is the quantum advantage? <https://blog.xa0.de/post/Where-is-the-quantum-advantage%3F/>`_ (2021)
    :cite:`Ratke_2021`
    
- | About **quantum annealing**:
    `When can Quantum Annealing win? <https://ai.googleblog.com/2015/12/when-can-quantum-annealing-win.html>`_
    :cite:`Denchev_2016` (2016), see also :ref:`stories/complements/adiabatic:State of the art` of AQC.

- | About **boson sampling**:
    *Quantum computational advantage with a programmable photonic processor* (2022) :cite:`Madsen_2022`
    (`YouTube <https://www.youtube.com/watch?v=bnX57EjvFVQ>`_)


:draft:`The important questions to investigate:`

- :draft:`A list of problems solved more efficiently on quantum computers.`
- :draft:`For what problems can we expect an exponential speedup?`


Roadmaps
--------

- `IBM’s Roadmap For Scaling Quantum Technology
  <https://www.ibm.com/blogs/research/2020/09/ibm-quantum-roadmap/>`_, Sep-15-2020
- `IBM’s roadmap for building an open quantum software ecosystem
  <https://www.ibm.com/blogs/research/2021/02/quantum-development-roadmap/>`_, Feb-4-2021


Balanced Opinions
-----------------

- "Quantum Computing: A bubble ready to burst?", Nov-11-2020 :cite:`Brant_2020`,
- "Will Quantum Computing ever live up to its hype?", Apr-20-2021 :cite:`Horgan_2021`
- "Quantum computing has a hype problem", Mar-28-2022 :cite:`DasSarma_2022`
- "Quantum Computing will change our lives. But be patient, please", Dec-14-2022, :cite:`Shankland_2022`

-----

**Further readings**

- "Status of quantum computer development"
  by the German Federal Office for Information Security :cite:`BSI_2020`
