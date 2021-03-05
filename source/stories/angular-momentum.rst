
Angular Momentum
================

.. include:: ../qutex.rst

.. ---------------------------------------------------------------------------

Fundamentals
------------

[#fQM10]_ In classical mechanics, the angular momentum :math:`\bm L` of a particle
of position :math:`\bm r` and momentum :math:`\bm p` is given by

.. math:: \bm L = \bm r \times \bm p

According to the correspondance principle, the angular-momentum observable is

.. math:: \hatb L = \hatb r \times \hatb p

and hence has following commutation relations

.. math:: \hatb{L} \times \hatb{L} = i \hbar \hatb{L}

We use this relation as the fundamental **definition** of an **angular-momentum
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


Orbital angular momentum
------------------------


Spin
----


.. ---------------------------------------------------------------------------

.. rubric:: Notes and References

.. [#fQM10] This story follows *Quantum Mechanics* :cite:`Basdevant2005`, chapter 10.
