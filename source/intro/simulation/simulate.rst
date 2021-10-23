
Simulate Quantum Systems
========================

.. ---------------------------------------------------------------------------

As described previously, the original :ref:`idea <intro/computing/idea:Idea>`
of quantum computing rose as a solution to simulating quantum systems.
Feynman's idea relied on the **digital quantum simulator**.

A second kind of simulators relies on the mapping of the simulated quantum system
onto a simulator system, and is called an **analog quantum simulator**.
The simulator is able to partly reproduce the dynamics of the simulated system,
forms a many-body model of it, and can be controlled to some extend. |citation|

.. ---------------------------------------------------------------------------

Two major problems can be addressed:

- | **Computing the energy levels** of a quantum system's:
    this requires an eigensolver for the Hamiltonian.
    This topic is covered in :ref:`stories/complements/chemistry:Quantum Chemistry`.

- | **Simulating Hamiltonian dynamics**:
    this requires the discretization of the Hamiltonian.

The former problem is essential to Quantum Chemistry:

- "Perhaps the **most important quantity** in quantum chemistry simulation is the **ground state**,
  which is the minimum energy eigenvector of the Hamiltonian matrix.
  This is because for most molecules at room temperature quantities such as **reaction rates**
  are dominated by free energy differences between quantum states
  that describe the beginning and end of a step in a reaction pathway and
  at room temperature such intermediate state are usually ground states." [#Groundstate]_


For the latter problem, two discretization methods may be applied [#Dynamics]_:

- Trotterization :cite:`Whitfield_2011`, :cite:`Hastings_2014`
- Qubitization :cite:`Low_2019`, :cite:`Babbush_2018`

...

.. ---------------------------------------------------------------------------

-----

**Notes:**

.. [#Groundstate]
    
    `Hartree–Fock Theory <https://docs.microsoft.com/en-us/azure/quantum/user-guide/libraries/chemistry/concepts/hartree-fock>`_
    in the Azure Quantum Documentation :cite:`AQCL_2021`.
    
.. [#Dynamics]
    
    `Simulating Hamiltonian Dynamics <https://docs.microsoft.com/en-us/azure/quantum/user-guide/libraries/chemistry/concepts/algorithms>`_
    in the Azure Quantum Documentation :cite:`AQCL_2021`.

**Further readings:**

- *Quantum Simulation* :cite:`Georgescu_2014`,
  complemented by *Quantum Simulators* :cite:`Altman_2021`.

- `Nature Physics Insight – Quantum Simulation
  <https://www.nature.com/collections/tmqjjbrhcb#editorial>`_,
  Nature 2012 (incl. :cite:`Bloch_2012`, :cite:`Blatt_2012`).

.. ---------------------------------------------------------------------------
