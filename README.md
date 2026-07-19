# Hardware-Aware Toffoli Decomposition Catalogue

A hardware-aware benchmarking framework for comparing multiple Toffoli (CCX) gate decompositions on IBM Heavy-Hex quantum processors.

The pipeline verifies the correctness of each decomposition, generates all connected physical qubit layouts on a Heavy-Hex coupling graph, transpiles every decomposition onto each valid layout using the Qiskit transpiler, converts circuits to the IBM Heron native gate basis, and reports hardware-aware circuit metrics for comparison.

---

# Repository Structure

```text
.
├── code
│   ├── circuits
│   │   ├── d1_barenco.py
│   │   ├── d2_maslov.py
│   │   ├── d3_amy.py
│   │   ├── d4_cruz_linear.py
│   │   ├── d5_nielsen_chuang.py
│   │   ├── d6_selinger.py
│   │   ├── d7_vale.py
│   │   ├── d8_jones.py
│   │   ├── d9_zero_ancilla.py
│   │   └── d10_alt.py
│   │
│   ├── catalogue.py
│   ├── layouts.py
│   ├── verify.py
│   ├── transpile_all.py
│   ├── analyze.py
│   ├── visual.py
│
├── results.json
├── summary.json
├── plots
└── README.md
```

---

# Pipeline

The benchmarking workflow consists of the following stages:

1. Verify the functional correctness of every decomposition.
2. Generate every connected physical qubit layout on the target Heavy-Hex coupling graph.
3. Transpile every decomposition onto every valid layout using the Qiskit transpiler.
4. Convert each circuit into the IBM Heron native gate basis.
5. Record hardware-aware circuit metrics.
6. Compute summary statistics.
7. Generate comparison plots.

---

# Included Decompositions

| ID | Decomposition |
|----|---------------|
| D1 | Barenco et al. |
| D2 | Maslov |
| D3 | Amy et al. |
| D4 | Cruz Linear Nearest-Neighbour |
| D5 | Nielsen–Chuang |
| D6 | Selinger (Ancilla-Assisted) |
| D7 | Vale et al. |
| D8 | Jones Relative-Phase Toffoli* |
| D9 | Zero-Ancilla Exact Toffoli |
| D10 | Alternative Exact Toffoli |

> **Note:** D8 is a relative-phase Toffoli implementation and is benchmarked separately from the exact decompositions.

---

# Hardware Model

The benchmarking pipeline targets IBM Heavy-Hex architectures.

Every decomposition is transpiled onto every connected physical layout and synthesized into the IBM Heron native gate basis consisting of

- CZ
- SX
- RZ
- X

using the standard Qiskit transpiler.

---

# Recorded Metrics

For every decomposition and every physical layout, the pipeline records

- CZ gate count
- SX gate count
- Circuit depth
- Successful transpilation onto the target layout

Aggregate statistics are computed over all valid layouts for each decomposition.

---

# Generated Outputs

### `results.json`

Contains the raw benchmarking results for every decomposition–layout pair, including the recorded hardware metrics.

### `summary.json`

Contains aggregate statistics for each decomposition, including minimum and average values across all valid layouts.

### `plots/`

Contains graphical comparisons of the recorded hardware metrics.

---

# Requirements

- Python 3.10+
- Qiskit
- NumPy
- Matplotlib

Install the required packages using

```bash
pip install qiskit numpy matplotlib
```

---

# Running the Pipeline

Verify all decompositions

```bash
python code/verify.py
```

Run the benchmarking pipeline

```bash
python code/transpile_all.py
```

Generate summary statistics

```bash
python code/analyze.py
```

Generate comparison plots

```bash
python code/visual.py
```

---

# Overview

This repository provides a reproducible framework for evaluating different Toffoli gate decompositions under realistic hardware constraints. By benchmarking each decomposition across every connected Heavy-Hex layout after transpilation to the IBM Heron native gate set, the framework enables hardware-aware comparison based on circuit depth and native gate counts.
