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

A general plan of what I ultimately want this to be 

Ideally, this will tie together all my PhD chapters into one coherent application
I will start with the basic aspect, which is a UI that allows for the selection of CNNs to be trained on given data.
But I want to tie in utility that allows querying of selected LLMs (possibly as classifiers, but mostly as a means to generate synthetic data)
These will present options to default prompt or to try to automatically generate a selection of prompts based on input image(s)
Finally, I aim to expand to cover the first chapter with some Bayesian modelling to incorporate phylogenetic effects. This will need to therefore interface with R and do a bunch of taxonomic name matching behind the scenes