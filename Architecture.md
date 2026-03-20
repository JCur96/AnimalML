Architecture

GUI layer responsible for:

    buttons

    forms

    file selection

    showing logs/progress

    displaying outputs


Python application layer responsible for:

    config handling

    workflow control

    input validation

    calling backend

    marshaling data

    error handling

C++/CUDA backend responsible for:

    expensive numeric operations

    GPU kernels

    memory-sensitive work

    performance-critical inference/pre/post-processing