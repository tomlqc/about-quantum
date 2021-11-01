
Adiabatic Quantum Computer
==========================

Quotes and formulae are taken from the *D-Wave Documentation* :cite:`DWave_2021`.

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

- Adiabatic quantum computers are made of a lattice of interconnected qubits [#topology]_.
  The qubits are not fully connected, what represents a limitation for the hamiltonians
  that can be described. Thus the topology i.e. the connection pattern is of great importance.

- To map any *Binary Quadratic Model* the specificity of the hardware topology must be considered.
  To make the best use of it, a strategy called **minor embedding** [#embedding]_ optimizes this mapping.
  
    "The process of mapping variables in the problem formulation to qubits on the QPU is known as minor embedding."

- :draft:`More about the physical realization and the difference to the Gate Model implementation soon...`
  [#implementation]_

.. ---------------------------------------------------------------------------
  
Miscellaneous
-------------

- :ref:`intro/computing/state:State of the Art`
- A review: *Adiabatic Quantum Computation* :cite:`Albash_2018`
- *Readiness* :cite:`PerdomoOrtiz_2019` (?)
- Applications: SAT-Problem :cite:`Farhi_2000`, Quantum Chemistry :cite:`Kassal_2011`

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

.. ---------------------------------------------------------------------------
