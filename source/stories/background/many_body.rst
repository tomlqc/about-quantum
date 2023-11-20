
Quantum Many-Body Physics
=========================

:draft:`My knowledge of quantum many-body physics is still very sparse. Nevertheless...`

This chapter gives a brief overview of tensor networks and how they are used to simulate quantum circuits.

.. ---------------------------------------------------------------------------

Tensor Networks
---------------

- | Orus, **A practical introduction to tensor networks:
    Matrix product states and projected entangled pair states**, 2014
    :cite:`Orus_2014` - :draft:`chapter 2-4`

  - "a partly non-technical introduction to selected topics on tensor network method"

  - Examples of TN methods: Density Matrix Renormalization Group (DMRG), Matrix product states (MPS),
    Projected Entangled Pair States (PEPS)
    
  - Wide variety of numerical methods for strongly correlated systems, each with their own limitations,
    e.g. Density Functional Theory (DFT) depends strongly on the modeling of the exchange and correlation interactions 

  - We can think of TN states as quantum states given in some entanglement representation.

  - The Hilbert space of a quantum many-body system is a really big place
    with an incredibly large number of quantum states,
    but low-energy states of realistic Hamiltonians are not just “any” state in the Hilbert space:
    they are heavily constrained by locality so that they must obey the *entanglement area-law*.
    
  - The manifold containing [the candidate low-energy] states is just a tiny, exponentially small,
    corner of the gigantic Hilbert space. 
    The vast majority of the Hilbert space is reachable only after a time evolution that would take O(exp(N )) time,
    given some initial quantum state, most of the Hilbert space is unreachable in practice.

  - A tensor network is the re-formulation of a rank-k tensor in terms of tensors of rank < k,
    using *index contraction* i.e.
    "sum over all the possible values of the repeated indices of a set of tensors"
    
  - Tensor networks can nicely by visualized as diagrams, such as to easily handle calculations with TN.
  
  - The total number of operations that must be done in order to obtain the final result of a TN contraction
    depends heavily on the order in which indices in the TN are contracted. 

- | Markov et al., **Simulating quantum computation by contracting tensor networks**, 2008 :cite:`Markov_2008` -
    :draft:`chapter 3-`

  - A quantum circuit C can be naturally regarded as a tensor network N(C):
    each gate is regarded as the corresponding tensor.

Implementation and algorithms:

- | NVIDIA's
    `cuTensorNet <https://docs.nvidia.com/cuda/cuquantum/latest/cutensornet/overview.html>`_

- | Tensor Network algorithms on `tensornetwork.org <https://tensornetwork.org>`_


:draft:`To investigate:`

- | Bridgeman, **Hand-waving and interpretive dance: an introductory course on tensor networks**, 2017
    :cite:`Bridgeman_2017` - :draft:`to read...`
  
  - "forms the basis for a seven lecture course,
    introducing the basics of a range of common tensor networks and algorithms"

- | from qiskit's `Matrix product state simulation method <https://qiskit.org/ecosystem/aer/tutorials/7_matrix_product_state_method.html>`_:

  - Vidal, **Efficient classical simulation of slightly entangled quantum computations**, 2003,
    `arXiv:quant-ph/0301063 <https://arxiv.org/abs/quant-ph/0301063>`_ - :draft:`seminal paper for MPS`

  - Schollwoeck, **The density-matrix renormalization group in the age of matrix product states**,
    `arXiv:1008.3477 <https://arxiv.org/abs/1008.3477>`_

- | Wood et al., **Tensor networks and graphical calculus for open quantum systems**, 2015 :cite:`Wood_2015`
    cited in :ref:`stories/background/environment:Quantum channels`.

- | Huang et al., **Efficient parallelization of tensor network contraction for simulating quantum computation**,
    2021 :cite:`HuangC_2021`
  
- | Seitz et al., **Simulating quantum circuits using tree tensor networks**, 2023 :cite:`Seitz_2023`

.. ---------------------------------------------------------------------------
