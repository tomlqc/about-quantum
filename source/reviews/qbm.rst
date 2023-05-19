
Quantum Boltzmann Machines
==========================

  - Ising models and associative memory,
  - Restricted Boltzmann Machines as the first working prototypes of deep networks,
  - What about Quantum Boltzmann Machines?
  -  ... - May 19, 2023

:draft:`Work in progress...`

.. implement on circ, qiskit, pennylane?

.. contents::
    :local:

-----

.. ---------------------------------------------------------------------------

Literature
----------

- | Hinton et al., **A fast learning algorithm for deep belief nets**, 2006,
    `pdf:fastnc <https://www.cs.toronto.edu/~hinton/absps/fastnc.pdf>`_,
    `doi:10.1162/neco.2006.18.7.1527 <https://doi.org/10.1162/neco.2006.18.7.1527>`_ -
    Univ. Toronto, Univ. Singapore.
  
  - "Using complementary priors, we derive a fast, greedy algorithm that can learn deep, directed belief networks one layer at a time, provided the top two layers form an undirected associative memory."

- | Adachi et Henderson, **Application of Quantum Annealing to Training of Deep Neural Networks**, 2015,
    `arXiv:1510.06356 <https://arxiv.org/abs/1510.06356>`_ -
    Lockheed Martin.
  
  - "We investigated an alternative approach that estimates model expectations of Restricted Boltzmann Machines using samples from a D-Wave quantum annealing machine. [alternative to Contrastive Divergence]".

- | Amin et al., **Quantum Boltzmann Machine**, 2016,
    `pdf:10.1103/PhysRevX.8.021050 <https://journals.aps.org/prx/pdf/10.1103/PhysRevX.8.021050>`_,
    `arXiv:1601.02036 <https://arxiv.org/abs/1601.02036>`_,
    `doi:10.1103/PhysRevX.8.021050 <https://doi.org/10.1103/PhysRevX.8.021050>`_ -
    D-Wave, Univ. Waterloo.
  
  - ...

- | Crawford et al., **Reinforcement learning using quantum boltzmann machines**, 2018,
    `arXiv:1612.05695 <https://arxiv.org/abs/1612.05695>`_,
    `doi:10.5555/3370185.3370188 <https://doi.org/10.5555/3370185.3370188>`_ -
    1QBit, Univ. BC. 
  
  - "We investigate whether quantum annealers with select chip layouts can outperform classical computers in reinforcement learning tasks."

- | Verdon et al., **A quantum algorithm to train neural networks using low-depth circuits**, 2019,
    `arXiv:1712.05304 <https://arxiv.org/abs/1712.05304>`_ -
    Univ. Waterloo.
  
  - Our algorithm, which we call the Quantum Approximate Boltzmann Machine (QABoM) algorithm, generates approximate samples of distributions for use in machine learning on a near-term circuit model device rather than a quantum annealer.

- | Zoufal et al., **Variational quantum Boltzmann machines**, 2021,
    `pdf:10.1007/s42484-020-00033-7 <https://link.springer.com/content/pdf/10.1007/s42484-020-00033-7.pdf>`_,
    `arXiv:2006.06004 <https://arxiv.org/abs/2006.06004>`_,
    `doi:10.1007/s42484-020-00033-7 <https://doi.org/10.1007/s42484-020-00033-7>`_ -
    IBM Quantum, ETH Zürich.
  
  - "Novel realization approach to quantum Boltzmann machines (QBMs). The preparation of the required Gibbs states, as well as the evaluation of the loss function’s analytic gradient, is based on variational quantum imaginary time evolution. [...]
    We illustrate the application of this variational QBM approach to generative and discriminative learning tasks using numerical simulation"
  
- | Perot, **Quantum Boltzmann Machines: Applications in Quantitative Finance**, 2022,
    `arXiv:2301.13295 <https://arxiv.org/abs/2301.13295>`_ -
    RWTH Aachen, Jülich SC.
  
  - Master thesis

- | Viszlai et al., **Training Quantum Boltzmann Machines with Coresets**, 2022,
    `arXiv: <https://arxiv.org/abs/>`_,
    `doi:10.1109/QCE53715.2022.00049 <https://doi.org/10.1109/QCE53715.2022.00049>`_ -
    Univ. Chicago, ColdQuanta.
  
  - "We apply these ideas to Quantum Boltzmann Machines (QBM) where gradient-based steps which require Gibbs state sampling are the main computational bottle-neck during training. By using a coreset in place of the full data set, we try to minimize the number of steps needed and accelerate the overall training time."

- | Huijgen et al., **Training Quantum Boltzmann Machines with the β-Variational Quantum Eigensolver**, 2023,
    `arXiv:2304.08631 <https://arxiv.org/abs/2304.08631>`_ -
    Radboud Univ. (NL), Quantinuum.
  
  - "The training of the QBM consists of minimizing the relative entropy from the model to the target state. This requires QBM expectation values which are computationally intractable for large models in general. It is therefore important to develop heuristic training methods that work well in practice."


Code
----

- | `github:cameronperot/qbm-quant-finance <https://github.com/cameronperot/qbm-quant-finance>`_

  - "In this thesis we explore using the D-Wave Advantage 4.1 quantum annealer to sample from quantum Boltzmann distributions and train quantum Boltzmann machines (QBMs). [...]
    Our findings indicate that QBMs trained using the Advantage 4.1 are much noisier than those trained using simulations and struggle to perform at the same level as classical RBMs. However, there is the potential for QBMs to outperform classical RBMs if future generation annealers can generate samples closer to the desired theoretical distributions."

- | `github:prabh27/Quantum-Boltzmann-Machines <https://github.com/prabh27/Quantum-Boltzmann-Machines>`_

  - "Quantum Restricted Boltzmann Machines based on the paper
    `arXiv:1712.05304 <https://arxiv.org/abs/1712.05304>`_ [Verdon et al., 2019]"
  - See also `jugit.fz-juelich:qip/qbm <https://jugit.fz-juelich.de/qip/qbm>`_

.. ---------------------------------------------------------------------------
