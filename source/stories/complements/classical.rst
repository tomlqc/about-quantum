
Classical Physics
=================

Use quantum computers to solve linear systems of equations
or simulate nonlinear physical systems.

.. contents::
    :local:

-----

.. `arXiv: <https://arxiv.org/abs/>`_
.. `doi: <https://doi.org/>`_

.. ---------------------------------------------------------------------------

Arithmetic operations
---------------------

About the difficulty of performing simple arithmetic operations on a quantum computer.
While factoring a number is much easier on a quantum computer,
multiplying two real numbers is much more difficult! One algorithm involves the QFT.

- Ruiz-Perez, **Quantum arithmetic with the Quantum Fourier Transform**, 2014,
  `arXiv:1411.5949 <https://arxiv.org/abs/1411.5949>`_,
  `doi:10.1007/s11128-017-1603-1 <https://doi.org/10.1007/s11128-017-1603-1>`_.

- Draper, **Addition on a Quantum Computer**, 2000,
  `arXiv:quant-ph/0008033 <https://arxiv.org/abs/quant-ph/0008033>`_.

- Vedral, **Quantum Networks for Elementary Arithmetic Operations**, 1995,
  `arXiv:quant-ph/9511018 <https://arxiv.org/abs/quant-ph/9511018>`_,
  `doi:10.1103/PhysRevA.54.147 <https://doi.org/10.1103/PhysRevA.54.147>`_.

.. ---------------------------------------------------------------------------

Linear Systems of Equations
---------------------------

- | Harrow, Hassidim & Lloyd, **Quantum algorithm for linear systems of equations**, 2009,
    `arXiv:0811.3171 <https://arxiv.org/abs/0811.3171>`_,
    `doi:10.1103/PhysRevLett.103.150502 <https://doi.org/10.1103/PhysRevLett.103.150502>`_
  
  - The **HHL algorithm**, see also the section :ref:`HHL algorithm <intro/computing/algo:HHL>`.
  - "We consider the case where one doesn’t need to know the solution x itself,
    but rather an approximation of the expectation value of some operator associated with x."
  - See also the
    `qiskit textbook chapter (HHL) <https://qiskit.org/textbook/ch-applications/hhl_tutorial.html>`_.

- | Bravo-Prieto, **Variational Quantum Linear Solver**, 2019,
    `arXiv:1909.05820 <https://arxiv.org/abs/1909.05820>`_
  
  - See also the
    `qiskit textbook chapter (VQLS) <https://qiskit.org/textbook/ch-paper-implementations/vqls.html>`_.

- | Perelshtein, **Solving Large-Scale Linear Systems of Equations by a Quantum Hybrid Algorithm**, 2022,
    `arXiv:2003.12770 <https://arxiv.org/abs/2003.12770>`_,
    `doi:10.1002/andp.202200082 <https://doi.org/10.1002/andp.202200082>`_.

.. ---------------------------------------------------------------------------

Nonlinear Problems
------------------

* | Lubasch et al., **Variational quantum algorithms for nonlinear problems**, 2020 :cite:`Lubasch_2020`
    `arXiv:1907.09032 <https://arxiv.org/abs/1907.09032>`_,
    `doi:10.1103/physreva.101.010301 <https://doi.org/10.1103/physreva.101.010301>`_
  
  - "Nonlinear problems including nonlinear partial differential equations can be efficiently solved
    by variational quantum computing."


- Liu, **Efficient quantum algorithm for dissipative nonlinear differential equations**, 2021,
  `arXiv:2011.03185 <https://arxiv.org/abs/2011.03185>`_,
  `doi:10.1073/pnas.2026805118 <https://doi.org/10.1073/pnas.2026805118>`_.
  See also dissertation
  `doi:10.13016/jxl7-ldtm <https://doi.org/10.13016/jxl7-ldtm>`_.

- Lloyd, **Quantum algorithm for nonlinear differential equations**, 2020,
  `arXiv:2011.06571 <https://arxiv.org/abs/2011.06571>`_.

- Kacewicz, **Almost optimal solution of initial-value problems by randomized and quantum algorithms**, 2006,
  `doi:10.1016/j.jco.2006.03.001 <https://doi.org/10.1016/j.jco.2006.03.001>`_.

Special applications:

* Givois, Kabel & Gauger, **QFT-based Homogenization**, 2022,
  `arXiv:2207.12949 <https://arxiv.org/abs/>`_.

.. ---------------------------------------------------------------------------

Fluid Dynamics
--------------

- | Ray et al., **Solving the Navier-Stokes Equation**, 2019 :cite:`Ray_2019` -
    Los Alamos

- | Gaitan, **Finding flows of a Navier-Stokes fluid**, 2020 :cite:`Gaitan_2020`

- | Gaitan, **Finding Solutions of the Navier-Stokes Equations through Quantum Computing—Recent Progress,
    a Generalization, and Next Steps Forward**, 2021,
    `pdf:wiley <https://onlinelibrary.wiley.com/doi/epdf/10.1002/qute.202100055>`_,
    `doi:10.1002/qute.202100055 <https://doi.org/10.1002/qute.202100055>`_.

- | Steijl, book chapters: *Quantum Algorithms for Fluid Simulations* :cite:`Steijl_2020`
    and *Quantum Algorithms for Nonlinear Equations in Fluid Mechanics* :cite:`Steijl_2020a`

- | Steijl, **Quantum Algorithms for Nonlinear Equations in Fluid Mechanics**, 2020,
    `html:intechopen <https://www.intechopen.com/chapters/74384>`_,
    `doi:10.5772/intechopen.95023 <https://doi.org/10.5772/intechopen.95023>`_.

  - A key contributing factor to the limited progress in algorithms for non-linear problems is the inherent linearity of quantum mechanics. For quantum algorithms encoding information as amplitudes of a quantum state vector, nonlinear (product) terms cannot be obtained by multiplying these amplitudes by themselves, as a result of the no-cloning theorem that prohibits the copying of an arbitrary quantum state.
  - Quantum circuits for squaring floating-point numbers
  - Quantum circuits for multiplication of floating-point numbers

- Griffin et al., **Quantum algorithms for direct numerical simulation**, 2020 :cite:`Griffin_2020`

.. ---------------------------------------------------------------------------

Turbulence
----------

Three papers supervised by Givi - Pittsburgh:

* Sammak et al., **Potential for Turbulence Simulations**, 2015 :cite:`Sammak_2015`

* Xu et al., **Turbulent Mixing Simulation via a Quantum Algorithm**, 2018 :cite:`Xu_2018`

* Xu et al., **Reactant conversion rate in homogeneous turbulence**, 2019 :cite:`Xu_2019`


.. ---------------------------------------------------------------------------

Miscellaneous
-------------

* Brassard et al., **Quantum algorithm to approximate the mean**, 2011
  :cite:`Brassard_2011` (Brassard is one of the authors of the BB84 protocol)

.. ---------------------------------------------------------------------------

Summary
-------

Using a quantum computer to solve problems of classical physics faces numerous and fundamental problems:

- Performing some of the basic arithmetic operations as the multiplication is much more complex and
  inefficient on a quantum hardware.
- Nonlinear product terms cannot be obtained easily, as a result of the no-cloning theorem.
- Most classical physics problems involves spatial and temporal discretization
  that results in a huge amount of (qu)bits to represent the problem with the required accuracy,
  posing a serious obstacle to the use of a quantum computer in a foreseeable future.
- Even using a QPU for subproblems that are "hard" to solve with classical algorithms may require
  a large number of error-corrected qubits. And these subproblems still have to be identified.


.. ---------------------------------------------------------------------------

-----

Complements:
:ref:`intro/intro:An Introduction` »
:ref:`intro/computing/computing:Quantum Computing` »
:ref:`intro/computing/apps:Applications`

