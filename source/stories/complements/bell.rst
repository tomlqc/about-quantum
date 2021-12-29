
Bell Inequalities
=================

.. include:: ../../qutex.rst

The Bell inequalities describe a way to prove the validity of Quantum Mechanics and to rule out any kind of hidden variable theory that would preserve locality and realism, as described in :ref:`stories/background/EPR_experiments:EPR Experiments`.

The are several forms of these inequalities. Here we will illustrate the CHSH inequality.

CHSH inequality
---------------

The *Gedankenexperiment* requires a large number of identical quantum systems, each made of two entangled particles.
One particle goes to Alice, who can measure the particle's spin along two directions :math:`\bm{a}, \, \bm{a'}`, while the other particle goes to Bob, who measures the spin along two other directions :math:`\bm{b}, \, \bm{b'}`.
The outcome of each of the measurements can take the values :math:`+1` or :math:`-1` only.
All systems are prepared in the same state, let it be the Bell state :math:`\phi^+ = \frac{1}{\sqrt{2}} (\ket{00} + \ket{11})`, expressed in the basis defined by :math:`\bm{a}`.
For each system, Alice and Bob choose randomly between their two possible measurements.

The CHSH inequality is based on the evaluation of following quantity for each system that we we will call "samples" in the remainder of this section, and involves the outcomes :math:`\epsilon` of the four possible measurements:

.. math::

    \epsilon_a \epsilon_b - \epsilon_{a'} \epsilon_b +
    \epsilon_a \epsilon_{b'} + \epsilon_{a'} \epsilon_{b'}

By reordering the terms, we observe that this quantity will only take the values :math:`+2` or :math:`-2`:

.. math::

    (\epsilon_a - \epsilon_{a'}) \epsilon_b +
    (\epsilon_a + \epsilon_{a'}) \epsilon_{b'} = \pm 2

Thus the average :math:`\Sigma_{Bell}` of this quantity over all systems will be bounded by the values :math:`\pm 2`:

.. math::

    -2 \le \Sigma_{Bell} \le +2 


Contradiction
-------------

For each of the sample systems, Alice as well as Bob can only measure one of their spin components. Let us assume that the four terms are always well defined **real** quantities, even if they are not all measured.
We also assume that the values of these quantities are defined **locally**, i.e. there are defined *a priori*, i.e. they do not depend neither on the choice of the measurements, nor on the measurement outcome of the other particle.

This means that, even if we have no access to the four measurement outcomes for each of the samples, we can perform an estimation of :math:`\Sigma_{Bell}` with an arbitrary precision (the precision depends only on the number of samples).
This is why we can statistically estimate :math:`\Sigma_{Bell}` by using individual averages of each of its four terms:

.. math::

    \Sigma_{Bell} = 
    & + \left< \epsilon_{a} \epsilon_{b} \right>_{\mathrm{samples \, where} \, (a, b) \, \mathrm{measured}} \\
    & - \left< \epsilon_{a'} \epsilon_{b} \right>_{\mathrm{samples \, where}(a', b) \, \mathrm{measured}} \\
    & + \left< \epsilon_{a} \epsilon_{b'} \right>_{\mathrm{samples \, where}(a, b') \, \mathrm{measured}} \\
    & + \left< \epsilon_{a'} \epsilon_{b'} \right>_{\mathrm{samples \, where}(a', b') \, \mathrm{measured}} 
    

We can also write these averages as expectation values given by the rules of Quantum Mechanics:

.. math::

    \Sigma_{Bell} =
    \left< { \sigma_{a \vphantom{b}}^A } { \sigma_{b}^B } \right> -
    \left< \sigma_{a' \vphantom{b}}^A \sigma_{b}^B \right> +
    \left< \sigma_{a \vphantom{b'}}^A \sigma_{b'}^B \right> +
    \left< \sigma_{a' \vphantom{b'}}^A \sigma_{b'}^B \right>

Let us go through one of the possible four outcomes:

We first measure :math:`\bm{a}`.
If :math:`\epsilon_{a} = +1` i.e. the state of A is projected on :math:`\ket{0}_A`,
then B is projected on :math:`\ket{0}_B` (remind that the initial state is :math:`\phi^+`).
The probability of :math:`\epsilon_{a} = +1` is 0.5.
It is the same for :math:`\epsilon_{a} = -1`.

Then we measure :math:`\bm{b}`.
According to the rules of Quantum Mechanics, the conditional probabilities for the terms :math:`\epsilon_a \epsilon_b` are:

.. math:: 

    P( b = +1 | a = +1 ) = \cos^2 (\frac{\theta_{a, b}}{2}) \, , \quad \epsilon_a \epsilon_b = +1 \,; \\
    P( b = -1 | a = +1 ) = \sin^2 (\frac{\theta_{a, b}}{2}) \, , \quad \epsilon_a \epsilon_b = -1 \,; \\
    P( b = +1 | a = -1 ) = \sin^2 (\frac{\theta_{a, b}}{2}) \, , \quad \epsilon_a \epsilon_b = -1 \,; \\
    P( b = -1 | a = -1 ) = \cos^2 (\frac{\theta_{a, b}}{2}) \, , \quad \epsilon_a \epsilon_b = +1 \,;

And finally we get:

.. math:: 

    \left< { \sigma_{a \vphantom{b}}^A } { \sigma_{b}^B } \right> =
    0.5 * 2 (\cos^2 \left( \frac{\theta_{a, b}}{2} \right) -
             \sin^2 \left( \frac{\theta_{a, b}}{2} \right) ) =
    \cos \theta_{a, b}

The expectation values of the other terms follow the same procedure, and we get:

.. math::

    \Sigma_{Bell} =
    \cos \theta_{a, b} - \cos \theta_{a', b} + 
    \cos \theta_{a, b'} + \cos \theta_{a', b'} 
    

Now we introduce the particular experimental setup suggested for the CHSH inequality.
We define the directions of the components :math:`\bm{a}, \bm{a'}, \bm{b}, \bm{b'}` such that:

.. math::

    \theta_{a, b} = \theta_{b', a} = \theta_{a', b'} = \frac{\pi}{4} \, , \quad
    \theta_{a', b} = \frac{3 \pi}{4}

These values lead to a value of :math:`\Sigma_{Bell}` that violates the inequality above:

.. math::

    \Sigma_{Bell} = + 2 \sqrt{2} \gt +2


Interpretation
--------------

As presented in :ref:`stories/background/EPR_experiments:EPR Experiments`,
it has been experimentally confirmed that the world obeys the rules of Quantum Mechanics.
This means that at least one of the assumptions of locality and realism,
which are required by the hidden variable theory, does not hold. Such a theory cannot exist!

One of the key elements to understand how this contradiction occurs,
is to consider that we estimate the four terms contributing to :math:`\Sigma_{Bell}` *individually*.
For each of these terms, we only have access to the outcomes of two of the four possible measurements.
When considering the contributions to one of this terms,
we observe that an unforeseen (wrt. the hidden variable theory) correlation introduces a statistic deviation from the expected behavior.
By choosing the two measurements, something *indeed* happens, that alters the uniform distribution that would lead to preserving the inequality.
By measuring one of the particles, i.e. by choosing one of the directions and inducing the collapse of the wave function, we alter the statistical distribution of the measurement outcomes of the second particles. This happens instantaneously and nonlocally.
