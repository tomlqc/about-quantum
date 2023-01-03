
Adiabatic Quantum Computer
==========================

Quotes and formulae are taken from the *D-Wave Documentation* :cite:`DWave_2021`
unless specified otherwise.

.. contents:: In this section
    :local:

-----

.. ---------------------------------------------------------------------------

Principle
---------

- **Combinatorial optimization** problems can be reformulated as **binary optimization** problems.
  These binary optimization can in turn be mapped to the Hamiltonian of a physical quantum system.

- **Quantum annealing** is based on the controlled evolution :cite:`Farhi_2000` of the Hamiltonian describing the quantum computer's hardware.
  It starts with an initial Hamiltonian whose ground state is known and easy to prepare,
  and *slowly* evolves towards the final Hamiltonian that describes the optimization problem.

  .. math::
    {\cal H}_{ising} =
    \underbrace{- \frac{A({s})}{2} \left(\sum_i {\hat\sigma_{x}^{(i)}}\right)}_\text{Initial Hamiltonian} +
    \underbrace{\frac{B({s})}{2} \left(\sum_{i} h_i {\hat\sigma_{z}^{(i)}} + 
                \sum_{i>j} J_{i,j} {\hat\sigma_{z}^{(i)}} {\hat\sigma_{z}^{(j)}}\right)}_\text{Final Hamiltonian}

- "An annealing process that experiences no interference from outside energy sources and
  evolves the Hamiltonian slowly enough is called an **adiabatic process**,
  and this is where the name *adiabatic quantum computing* comes from."

- The **minimum gap** problem:
  During the annealing process, while the Hamiltonian slowly evolves,
  the ground state may become very close to the first excited state
  in terms of the energy gap between them.
  If the process occurs too fast this could lead the system to move to this excited state
  and therefore corrupt the solution of the optimization problem.
  This is the reason for the requirement of the evolution to be *slow*. 
  One major theoretical odd of quantum annealing is the lack of a general statement
  about how slow this process has to occur.
  Nevertheless strategies are proposed to increase the energy gap [#gap]_.

.. ---------------------------------------------------------------------------

Optimization Problems
---------------------

- The kind of optimization problems that can be easily mapped on Hamiltonians are **Binary Quadratic Models** [#problems]_.
  The common variants for describing the objective functions are
  the *Ising Model* and
  *QUBO (Quadratic Unconstrained Binary Optimization)*.
  
    "In summary, to solve a problem on quantum samplers, you formulate the problem as an objective function,
    usually in Ising or QUBO format.
    Low energy states of the objective function represent good solutions to the problem."

- The **Ising Model**, one of the two common variants used to formulate the optimization problems,
  is also an immediate representation of the hardware (!)

  .. math::
    \text{E}_{Ising}(\boldsymbol{s}) = \sum_{i=1}^N h_i s_i + \sum_{i=1}^N \sum_{j=i+1}^N J_{i,j} s_i s_j

- Problems need to be reformulated in terms of a binary quadratic model.
  See the section :ref:`stories/complements/opti:Reformulating Problems` [#reformulate]_.

.. ---------------------------------------------------------------------------

Hardware
--------

- | Adiabatic quantum computers are made of a lattice of interconnected qubits [#topology]_.
    The qubits are not fully connected, what represents a limitation for the hamiltonians
    that can be described. Thus the topology i.e. the connection pattern is of great importance.

- The original **D-Wave architecture** is described by Harris, 2010 :cite:`Harris_2010`.
  A reason for the **difference between quantum annealers and circuit-based quantum computers** and
  therefore why the D-Wave quantum annealer has significantly more qubits then the current
  gate-based quantum computers is the following:

  "[...] one can provide uniform [flux] :math:`\Phi_{ccjj}^x` to multiple qubits
  using a single global current bias line, as opposed to one bias line per qubit. [...]
  In doing so, one substantially reduces the number of external biases that must be applied
  to the processor, thus **significantly improving the scaling of this particular architecture**. 
  "

- | The problematic sensitivity to noise of the above described design is due to the
    "qubit physical layer not separated from classical control layer" :cite:`Lidar_2021`.
    This leads to a not fully coherent mode of operation of current quantum annealers, 
    as described together with **"more-coherent" architectures** in the next section :ref:`stories/complements/adiabatic:State of the art`.

- To map any *Binary Quadratic Model* the specificity of the hardware topology must be considered.
  To make the best use of it, a strategy called **minor embedding** [#embedding]_ optimizes this mapping.
  
    "The process of mapping variables in the problem formulation to qubits on the QPU is known as minor embedding."

- | See also an alternative yet prototype coherent realization with Rydberg atoms :cite:`Glaetzle_2017`.

- See also the "quantum annealing architecture with all-to-all connectivity from local interactions"
  (LHZ architecture) :cite:`Lechner_2015` implemented by `ParityQC <https://parityqc.com/parityqc-architecture>`_.

For more details about the architecture and control see the notes below [#implementation]_ [#hardware]_.

.. ---------------------------------------------------------------------------

Embedding
---------

The discrete optimization problems must be mapped on the QUBO formalism,
and then the QUBO itself must be mapped to the hardware,
what is referred to as "embedding":
the main obstacle is the limited connectivity of the hardware,
and the problem's connectivity graph has to be "embedded" on the hardware.
This makes it necessary to group several physical qubits together to form one logical qubits.

In the case of a fully connected QUBO, the number of logical qubits that 
can be mapped on a specific hardware may be significantly smaller than the 
number of physical qubits.

The required connectivity is nicely represented by the "QUBO matrix".

Let's take the example of the
:ref:`stories/complements/opti:Example: Traveling Salesman` as stated in the
:ref:`stories/complements/opti:Combinatorial Optimization` section.
We have seen that the QUBO formulation scales with :math:`N^2` where :math:`N` is the number of places to visit.
The natural index for the variable was given by the pair :math:`v,i`
but we may express it by a single index :math:`\xi` in the range of :math:`N^2`.
The QUBO matrix is the representation of the coefficients in the quadratic expression of the Hamiltonian:
the terms :math:`Q_{\xi, \eta}` of the matrix are the coefficients in front of the terms
:math:`x_{\xi} x_{\eta}`.

The qubits in the Quantum Annealer hardware form an Ising model.
The one-to-one correspondence between QUBO and Ising model formulation is nicely 
described in the `myQML documentation <https://myqlm.github.io/index.html>`_'s
section about `Formulating combinatorial problem
<https://myqlm.github.io/combinatorial_optimization_intro.html#formulating-combinatorial-problems>`_.
The strength of the coupling between two qubits :math:`\xi` and :math:`\eta` is directly proportional
to the term :math:`Q_{\xi, \eta}` of the QUBO.

We can see from the TSP Hamiltonian that the connectivity is not only due to the terms related to the edge weights,
but that the penalty terms introduce a full connectivity because of the square of the sum of all variables.
For that reason the TSP will scale much worse than :math:`N^2` on real quantum hardware as it will require
many physical qubits for just a few logical ones.

Lucas :cite:`Lucas_2014` tells us that only few classes can be easily embedded:

    Another simple class of mappings from NP problems to Ising models: **“covering” and “packing” problems**.
    These are, by far, the most popular class of problems discussed in the AQO literature. As we mentioned
    in the introduction, this is because this is the **only class of NP problems** (discussed in this paper)
    for which it is **easy to embed** the problem via a graph which is not complete (or close to complete)

The embedding procedure as required on D-Wave system's is referred to as
`minor-embedding <https://docs.ocean.dwavesys.com/en/stable/concepts/embedding.html>`_.
The limitation described above is also mentioned by Weinberg :cite:`Weinberg_2022`:

    One should recognize that the **5000-qubit processor** cannot handle a problem of 5000 binary variables. The embedding requires multiple hardware qubits to be programmed as a logical node to represent each logical variable. For a fully-connected logical problem, one in which every binary variable interacts with all the others, one can only embed such a fully-connected problem of approximately **180 logical binary variables**. Many problems of practical interest are not fully-connected logically, so larger problem sizes of hundreds of binary variables can often be embedded.

.. ---------------------------------------------------------------------------
  
State of the art
----------------

- **A review:** *Adiabatic Quantum Computation* :cite:`Albash_2018`

  - AQC equivalent to the circuit model (and of course requires full coherence)
  - "We finally devote considerable space to Stoquastic AQC, the setting of most AQC work to date, where we discuss obstructions to success and their possible resolutions." :draft:`(de facto D-Wave hardware (?))`
  
- `When can Quantum Annealing win? <https://ai.googleblog.com/2015/12/when-can-quantum-annealing-win.html>`_,
  2016 :cite:`Denchev_2016`
  
    "During the last two years, the Google Quantum AI team has made progress in understanding the physics governing quantum annealers. [...]
    We found that for problem instances involving nearly 1000 binary variables, quantum annealing significantly outperforms its classical counterpart, simulated annealing. It is more than 108 times faster than simulated annealing running on a single core. [...]
    While these results are intriguing and very encouraging, there is more work ahead to turn quantum enhanced optimization into a practical technology. The design of next generation annealers must facilitate the embedding of problems of practical relevance. For instance, we would like to increase the density and control precision of the connections between the qubits as well as their coherence."

- `IARPA Quantum Enhanced Optimization <https://www.iarpa.gov/index.php/research-programs/qeo>`_,
  2021 summary :cite:`Lidar_2021` :cite:`Crosson_2021`
  
  - "More-coherent quantum annealing" :cite:`Novikov_2018`, build at MIT Lincoln Laboratory,
    while D-Wave hardware lacks sufficient coherence
  
  - Project superseded by the `DARPA’s Quantum Annealing Feasibility Study <https://www.darpa.mil/news-events/2020-05-11a>`_.

- "Demonstration of a scaling advantage for a quantum annealer over simulated annealing", 2018 :cite:`Albash_2018b`:

    "[We] establish the first example of a scaling advantage for an experimental quantum annealer over classical simulated annealing. [...]
    However, we do not find evidence for a quantum speedup: SQA exhibits the best scaling for annealing algorithms by a significant margin. This is a finding of independent interest, since we associate SQA’s advantage with its ability to transverse energy barriers in the semiclassical energy landscape by mimicking tunneling.
    "

- :draft:`To investigate:` *Readiness* :cite:`PerdomoOrtiz_2019` (?)

- Applications: SAT-Problem :cite:`Farhi_2000`, Quantum Chemistry :cite:`Kassal_2011`

See also general section about :ref:`intro/outlook/state:State of the Art` of Quantum Computing.

.. ===========================================================================

-----

**Notes:**

.. [#gap]

    `Handbook > Energy Gap <https://docs.dwavesys.com/docs/latest/handbook_qpu.html#energy-gap>`_
    :cite:`DWave_2021`

.. [#problems]

    `Getting Started > Solving Problems with Quantum Samplers <https://docs.dwavesys.com/docs/latest/c_gs_3.html>`_
    :cite:`DWave_2021`

.. [#reformulate]

    | `Getting Started > Next Learning Steps <https://docs.dwavesys.com/docs/latest/c_gs_9.html#>`_
      and
    | `Handbook > Reformulating a Problem <https://docs.dwavesys.com/docs/latest/handbook_reformulating.html>`_
      :cite:`DWave_2021`.

.. [#topology]

    `Getting Started > QPU Architecture: Topologies <https://docs.dwavesys.com/docs/latest/c_gs_4.html>`_
    :cite:`DWave_2021`

.. [#embedding]

    | `Ocean > Concept: Minor-Embedding <https://docs.ocean.dwavesys.com/en/stable/concepts/embedding.html>`_
      :cite:`DWaveOcean_2021` and
    | `Handbook > QPU Solvers: Minor-Embedding <https://docs.dwavesys.com/docs/latest/handbook_embedding.html>`_
      :cite:`DWave_2021`

.. [#implementation]

    `QPU Solver Datasheet <https://docs.dwavesys.com/docs/latest/c_qpu_annealing.html>`_
    :cite:`DWave_2021`

.. [#hardware]

    General considerations about the coupling :cite:`Krantz_2019`:

    "**Longitudinal coupling** is an important type of interaction,
    because it can generate entanglement without energy exchange.
    Moreover, it is found a necessary ingredient in the application of
    quantum annealing, where certain hard combinatorial optimization
    problems can be modeled by the Ising Hamiltonian [...] and
    finding its ground state would solve this problem."

    "In some applications, such as for quantum annealing, both **longitudinal
    and transverse couplings** are desired (:math:`\sigma_z \sigma_z` coupling for mapping
    the problem and :math:`\sigma_x \sigma_x` coupling for enhancing the annealing
    performance) and require independent control."

.. ---------------------------------------------------------------------------
