# Hardware-Aware Toffoli Decomposition Catalogue

This repository contains a catalogue of Toffoli (CCX) gate decompositions
together with a pipeline for verification, transpilation, and benchmarking
on IBM Heavy-Hex architectures.

## Repository structure

Catalog/
    circuits/
        ...
    catalogue.py
    layouts.py
    verify.py
    transpile_all.py
    analyze.py
    visualize.py

results.json
summary.json

plots/

## Pipeline

1. Verify every decomposition.
2. Generate connected Heavy-Hex layouts.
3. Transpile every decomposition on every layout.
4. Collect CZ count, SX count and circuit depth.
5. Generate summary statistics.
6. Produce comparison plots.

## Included decompositions

- D1 Barenco
- D2 Maslov
- D3 Amy
...
- D10 Alternative

## Metrics

Each decomposition is benchmarked using

- CZ count
- SX count
- Circuit depth

across every connected Heavy-Hex layout.

## Requirements

Python 3.13

Qiskit

Matplotlib

NumPy

...
