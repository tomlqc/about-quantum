
Breaking RSA
============

.. include:: ../../qutex.rst

Let's sketch the Shor algorithm!

.. contents::
    :local:

.. ---------------------------------------------------------------------------

Quantum Fourier transform
-------------------------

We start with the *quantum Fourier transform*,
which is a linear operator in an :math:`N`-dimensional Hilbert space.
Let :math:`\ket{0}, ..., \ket{N - 1}` be an orthonormal basis of this space,
the QFT is defined as

.. math::

  \ket{j} \mapsto \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2 \pi i j k / N} \ket{k}

i.e. it associates to an element of the basis a superposition of all the basis elements.

To any arbitrary state :math:`\sum_{j=0}^{N-1} x_j \ket{j}` the QFT assigns 
a state :math:`\sum_{k=0}^{N-1} y_k \ket{k}`
whose amplitudes are the DFT coefficients of the amplitudes :math:`x_j`.

It is very useful to note that a system of :math:`n` qubits evolve
in a :math:`N = 2^n`-dimensional space,
i.e. we can write the elements :math:`\ket{j}` above using a binary
representation :math:`j = j_1 j_2 ... j_n`.
This representation can be used to construct an efficient quantum circuit computing the QFT 
with a complexity of :math:`O(n^2)` in terms of gates [#QFT]_.

.. ---------------------------------------------------------------------------

Phase estimation
----------------

Let :math:`U` be an unitary operator and :math:`\ket{u}` one of its eigenvectors
with eigenvalue :math:`e^{2 \pi i \phi}`.
The purpose of the *phase estimation* algorithm is to estimate :math:`\phi`
by an approximation :math:`\widetilde{\phi}`.

It makes use of two registers, where the first one is initialized
in state :math:`\ket{0}` while the second one is in state :math:`\ket{u}`
i.e. we start from :math:`\ket{0} \ket{u}`.
By applying Hadamard gates on each qubit of the first register, we generate
a superposition of "all the possible" states,
apply :math:`U` a certain number of times on the second register (this is the real magic),
and apply the inverse Fourier transform,
to finally terminate in state :math:`\widetilde{\ket{\phi_u}} \ket{u}`.

This is a product state (no entangled superposition),
thus we just have to measure the first register to get :math:`\widetilde{\phi}`!
Well, we get this value only with some probability, but this can be managed to be 
arbitrary close to one.

.. ---------------------------------------------------------------------------

Order finding
-------------

Now a bit of arithmetics.

For positive integers :math:`x` and :math:`N` with :math:`x \lt N` and no common factors,
the *order* of :math:`x` modulo :math:`N` is defined to be the least positive integer,
:math:`r`, such that :math:`x^r = 1 \, (\mathrm{mod} \, N)`.
*Order finding* is the task of finding :math:`r` for given :math:`x, N`,
and is believed to be hard for a classical computer in terms of the
size :math:`L = \log(N)`.

One can show that order-finding is equivalent to the phase estimation algorithm applied 
to the unitary operator :math:`U \ket{y} = \ket{ x y \, (\mathrm{mod} \, N) }`.
Indeed the eigenvalues of :math:`U` are the numbers
:math:`\exp{ \frac{2 \pi i s}{r} }` with :math:`0 \le s \le r - 1`.
This means, if we could prepare the second register in the state of
an eigenvector :math:`\ket{u_s}` of :math:`U`,
and we could implement :math:`U` efficiently, we would have an estimation of
:math:`\frac{r}{s}`. But then we must still find a way to derive :math:`r`...

Lot's of obstacle...

First notice that

.. math:: \frac{1}{r} \sum_{s=0}^{r-1} \ket{u_s} = \ket{1}

i.e. we can perform the phase estimation procedure on :math:`\ket{1}` 
and will get an estimation of one of the :math:`\widetilde{\phi} = \frac{s}{r}`.

The implementation issue of :math:`U` can be solved using a procedure
known as *modular exponentation*, that we won't detail here.

But how can we recover :math:`s` and :math:`r` from :math:`\widetilde{\phi}`?
A remarkable algorithm called the *continued fractions algorithm* allows us
to find a continued fraction expansion of an arbitrary real number.
In our case, we are looking for the expansion of a rational number,
described by L digits. The algorithm scales as :math:`O(L^3)`.
Thus, we have a way to calculate :math:`r`, since :math:`s` and :math:`r` have
no common factor!

.. ---------------------------------------------------------------------------

Factoring
---------

Factoring can be reduced to order-finding by an algorithm scaling as
:math:`O((\log N)^3)` with probability :math:`O(1)`.
After a few preliminary steps for finding easy factors of :math:`N`,
one of the steps of the algorithm involves choosing randomly 
a number :math:`x` in the range :math:`1` to :math:`N - 1`,
using the *order-finding* subroutine to find the order :math:`r`
of :math:`x` modulo :math:`N`.
Then (omitting additionaly checks) the *gcd* of
:math:`(x^{r/2} - 1, N)` and of :math:`(x^{r/2} + 1, N)` are calculated:
If one of these is a non-trivial factor, then we have found the result!

.. ---------------------------------------------------------------------------

RSA problem
-----------

`Wikipedia <https://en.wikipedia.org/wiki/RSA_(cryptosystem)>`_ tells us:
"The RSA problem is defined as the task of [...]
recovering a value :math:`m` such that :math:`c = m \, e \, (\mathrm{mod} \, n)`,
where :math:`(n, e)` is an RSA public key
and :math:`c` is an RSA ciphertext.
Currently the most promising approach to solving the RSA problem
is to factor the modulus :math:`n`."

*Et voilà!*

.. ---------------------------------------------------------------------------

Quantum Circuit
---------------

How many qubits will we need for this task?

The `NIST recommends
<https://doi.org/10.6028/NIST.SP.800-57pt3r1>`_
RSA key sizes of 2048 bits.
Bytheway you may click on your browser's lock symbol close to the address bar
and check yourself the size of your current RSA encryption.

That means we will need 2048 qubits just to store the number to factorize.
Depending on the error correction algorithms
(just think of a repetition code that requires many physical qubits
to implement one logical qubit), many more qubits will be necessary.
But it was shown that about 20 million qubits, much less then previously thought,
could be enough to factorize the 2048 bit number in 8 hours :cite:`Gidney_2021`.

But how to achieve a quantum computer with so many qubits,
that would achieve such an incredibly long coherence time?
We still need some technological breakthrough...

.. ===========================================================================

-----

.. [#QFT]

    We can interpret the QFT as a mapping from and to a N-dimensional space.
    Because a set of :math:`n` qubits evolve in a space of dimension :math:`N = 2^n`,
    the QFT's complexity can be written in terms of :math:`n`.
    It can be shown that the QFT can be implemented by a quantum circuit
    using :math:`O(n^2)` elementary gates,
    i.e. :math:`O((\log{N})^2)`
    
    For comparison, the classical Discrete Fourier Transform (DFT) with N terms
    has a complexity of :math:`O(N^2)`,
    and the Fast Fourier Transform (FFT) scales with :math:`O(N \log{N})`.
    
    Thus the QFT could be seen as an exponential speedup compared to the FFT,
    as :math:`O(N \log{N}) = O(2^n n)`.
    But the FT and the QFT achieve two different goals:
    while the FT returns the :math:`N` coefficients as numbers,
    the QFT generates a superposition of states whose amplitudes are the Fourier coefficients.

-----

Complements:
:ref:`intro/intro:An Introduction` »
:ref:`intro/computing/computing:Quantum Computing` »
:ref:`intro/computing/apps:Applications`
