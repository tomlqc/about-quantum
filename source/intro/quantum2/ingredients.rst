
More Ingredients
================

.. ---------------------------------------------------------------------------

Additionally to the fundamental description of *superposition* and *entanglement*,
a few more tools are necessary for properly describing the quantum phenomena
whose control is mandatory for running a quantum computer.

The so-called **qubits** are based on :ref:`stories/background/twolevel:Two-Level Systems` (TLS)
that are quantum systems that inherently possess two energy levels.
These systems may have additional levels, but these must not be attained by the system
else it would spoil the function of the quantum computer.
Hence the energy gap between these two levels has to be sensibly different from the other levels.
An isolated single qubit will evolve in the two-dimensional Hilbert space of this TLS.

Qubits must be allowed to interact with each other and form a single quantum system
grouping all of them.
This **interaction** involves a medium between the qubits that passes quantas of energy:
this medium is itself a part of the quantum system, and
is basically a quantized field such as light (e.g. photons in cavity QED)
or vibrational modes (e.g. phonons in ion traps).
These fields can be nicely described with the :ref:`stories/background/harmonic:Harmonic Oscillator` model.

To fit the qubits and their interaction all together,
the **quantization** of the TLS and the field can be united into own powerful framework,
that describes the state and the evolution of the system in terms of its energy:
the :ref:`Hamiltonian <stories/background/hamiltonian:Hamiltonians>`.
The :ref:`stories/background/2ndquant:Quantization of the electromagnetic field`
is a prerequisite to formulating the atom-light interaction and
is a fascinating description of light in terms of the harmonic oscillator.
The :ref:`stories/background/2ndquant:Second Quantization`
is a way to formulate the atomic Hamiltonian in analog terms to the quantized electromagnetic field.
It involves *ladder* operators such as the *creation* and *annihilation* operators,
and describes a matter particle in the same terms then a field.

In his pioneering experiments in cavity QED, Serge Haroche called the qubits and 
the mediating entities between them the "spins and springs",
as its TLS under consideration were described in terms of 1/2 spins,
while springs are illustrative for the harmonic oscillator.

Finally, the concept of quantum computing is based on an ideally isolated quantum system,
but paradoxically this quantum system must be feed and controlled from the outside world:
the **environment**.
Beside this desirable interaction, the quantum system can and will sporadically interact
with the environment in an uncontrolled way: the **noise**.
There is a sound framework for describing the action of the 
:ref:`stories/background/environment:Environment` on a quantum system.
It is well modelled, and a mandatory tool to describe the
:ref:`intro/computing/noise:Noise` in a Quantum Computer.

.. ---------------------------------------------------------------------------
