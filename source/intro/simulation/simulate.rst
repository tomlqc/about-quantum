
Simulate Quantum Systems
========================

.. ---------------------------------------------------------------------------

Simulating quantum systems is a very challenging task, because of the huge
requirements in computational power and in memory, that scales exponentially
with the system size.
The "standard" threshold is considered to be at about :math:`N = 40` :
storing :math:`2^{40} \approx 10^{12}` numbers as 32-bit floats takes about 4 TB of memory
[#50qubits]_.
Approximate statistical methods, namely Monte Carlo algorithms, can be used for many
problems, but not for all quantum systems, especially for fermionic systems,
as for example the electronic structure of a molecule.

In 1982, Richard Feynman explained his vision of a quantum computer that would
be able to simulate quantum systems in a far more efficient way that classical
computers, because it would be of the same nature that the system to simulate:
"Let the computer it-self be built of quantum mechanical elements
which obey quantum mechanical laws." :cite:`Feynman_1982`

The kind of computer that Feynman envisaged was a universal quantum simulator,
made of a circuit of universal quantum gates,
and is currently refered to as a **digital quantum simulator**.
The Hamiltonian of the system to be simulated is approximated by a circuit,
with the essential condition that for the simulation to be efficient,
this approximation, including the preparation of the initial state,
must be done with polynomial resources.

The second kind of simulators relies on the mapping of the simulated quantum system
onto a simulator system, and is called an **analog quantum simulator**.
The simulator is able to partly reproduce the dynamics of the simulated system,
forms a many-body model of it, and can be controlled to some extend.

.. ---------------------------------------------------------------------------

-----

**References:**
*Quantum Simulation* :cite:`Georgescu_2014`,
complemented by *Quantum Simulators* :cite:`Altman_2021`.

.. [#50qubits]
    
    Preskill mentions a "milestone" of 50 qubits :cite:`Preskill_2018`, that is
    "beyond what can be simulated by brute force using the most powerful existing digital supercomputers".
    This estimation relies on classical simulations of typically a lattice of 7 x 7 qubits
    :cite:`Boixo_2018`.
    It is practically the same then the 40 qubits named above.
    
.. ---------------------------------------------------------------------------
