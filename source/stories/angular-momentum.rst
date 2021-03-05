
Angular Momentum
================

.. include:: ../qutex.rst

The basic results about angular momentum [#fQM10]_.

.. ---------------------------------------------------------------------------

Fundamentals
------------

In classical mechanics, the angular momentum :math:`\bm L` of a particle
of position :math:`\bm r` and momentum :math:`\bm p` is given by

.. math:: \bm L = \bm r \times \bm p

According to the correspondance principle, the angular-momentum observable is

.. math:: \hatb L = \hatb r \times \hatb p

and hence has following commutation relations

.. math:: \hatb{L} \times \hatb{L} = i \hbar \hatb{L}

We use these relations as the fundamental **definition** of an **angular-momentum
observable** :math:`\hatb J`

.. math:: \hatb{J} \times \hatb{J} = i \hbar \hatb{J}

We observe that :math:`[ \hatsup{J}{2}, \hatb{J} ] = 0` and that we can construct
a CSCO made of :math:`\{ \hatsup{J}{2}, \hatsub{J}{z} \}` i.e. these two operators
has a common eigenbasis.
We can write their eigenvalues, without loss of generality, 
using two dimensionless numbers :math:`j` and :math:`m` such that

.. math::
    
    & \hatsup{J}{2} \ket{j, m} = j (j + 1) \, \hbar^2 \ket{j, m} \\
    & \hatsub{J}{z} \ket{j, m} = m \hbar \ket{j, m}

where the vectors :math:`\ket{j, m}` form the set of eigenvectors.

It can be shown that the numbers :math:`j` and :math:`m` are quantized following the rules:

* :math:`j` is a positive (or zero) integer or half integer
* the only possible values of *m* are the :math:`2j + 1` numbers
  :math:`-j, -j + 1, ..., j - 1, j`.


Orbital angular momentum
------------------------

We consider here a particle moving in space, described by a wave function,
and its orbital angular momentum :math:`\hatb L = \hatb r \times \hatb p`.
In spherical coordinates the operator :math:`{\hat L}_z` has a simple form

.. math:: {\hat L}_z = \frac{\hbar}{i} \frac{\partial}{\partial \phi}

The required periodicity in :math:`\phi` with period :math:`\pi` leads to the conclusion
that for an orbital angular momentum, :math:`m` must be an integer, and
as a consequence :math:`l` is also an integer.

The eigenfunctions common to the observables :math:`\hatsup{L}{2}` and :math:`{\hat L}_z`
are called the spherical harmonics and are denoted :math:`Y_{l,m}(\theta, \phi)`

.. math::
    
    \newcommand{Ylm}{Y_{l,m}(\theta, \phi)}
    
    & \hatsup{L}{2} \, \Ylm = l (l + 1) \hbar^2 \, \Ylm , \\
    & {\hat L}_z \, \Ylm = m \hbar \, \Ylm


Motion in a central potential
-----------------------------

In spherical coordinates, the Laplacian operator :math:`\Delta` can be expressed in
terms of the angular momentum :math:`\hatb{L}`

.. math::

    \Delta = \frac{1}{r} \frac{\partial^2}{\partial r^2} r -
             \frac{1}{r^2 \hbar^2 \hatsup{L}{2}}

Thus the operator associated to the kinetic energy of a particle, and hence its
Hamiltonian :math:`\hat H`, can be expressed using :math:`\hatb{L}` too.

Furthermore one can show that for a particle in a central potential, they commute

.. math:: [\hat H, \hatb L] = 0

The wave function can be written as

.. math:: \psi_{l,m}(\bm r) = R_l(r) \, \Ylm

where :math:`R(r)` depend only on :math:`l`.

The eigenvalues of the Hamiltonian can be labeled by the two quantum numbers :math:`l`
and :math:`n'`, the *radial quantum number*. They do not depend on :math:`m`,
as a consequence of the rotation invariance of the system (central potential).

In a Coulomb potential, the energy levels depend only on the quantity :math:`n' + l + 1`,
and we can alternatively label the energies using this *principal quantum number* :math:`n`.

In spectroscopic notation we associate the levels of :math:`l` to the letters
*s, p, d, f, g, h* etc. and :math:`n` is denoted by a number preceding this letter,
e.g. :math:`n = 1, \; l = 0: \mathrm{state} \, 1s`.

Magnetic Moment
---------------

We postulate that if the particle has a magnetic moment :math:`\bm{\mu}`,
the corresponding observable :math:`\hatb{\mu}` is proportional to :math:`\hatb{L}`,
and we call the factor gyromagnetic ratio :math:`\gamma`

.. math:: \hatb{\mu} = \gamma \hatb{L}


Spin
----


.. ---------------------------------------------------------------------------

.. rubric:: Notes and References

.. [#fQM10] This story is basically a summary of *Quantum Mechanics* :cite:`Basdevant2005`,
    chapter 10. Some of the phrases are reproduced literally.
