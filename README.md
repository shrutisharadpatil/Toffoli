# Hardware-Aware Toffoli Decomposition Catalogue

A catalogue of Toffoli (CCX) gate decompositions together with an automated benchmarking pipeline for IBM Heavy-Hex quantum processors.

The pipeline verifies each decomposition, generates all connected physical layouts on a Heavy-Hex coupling graph, transpiles every decomposition onto each valid layout using the Qiskit transpiler, and reports hardware-aware circuit metrics for comparison.

---

## Repository Structure

```
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
│   └── visualize.py
│
├── results.json
├── summary.json
├── plots
└── README.md
```

---

## Pipeline

The benchmarking pipeline consists of the following stages.

1. Verify the functional correctness of every decomposition.
2. Generate every connected physical layout on the target Heavy-Hex coupling graph.
3. Transpile every decomposition onto every valid physical layout using the Qiskit transpiler.
4. Convert each circuit into the IBM Heron native gate basis.
5. Record hardware-aware circuit metrics.
6. Aggregate summary statistics.
7. Generate comparison plots.

---

## Included Decompositions

| ID | Decomposition |
|----|---------------|
| D1 | Barenco et al. |
| D2 | Maslov |
| D3 | Amy et al. |
| D4 | Cruz Linear Nearest-Neighbour |
| D5 | Nielsen–Chuang |
| D6 | Selinger (Ancilla-Assisted) |
| D7 | Vale et al. |
| D8 | Jones Relative-Phase Toffoli |
| D9 | Zero-Ancilla Exact Toffoli |
| D10 | Alternative Exact Toffoli |

---

## Hardware Model

The benchmarking pipeline targets IBM Heavy-Hex architectures.

Each decomposition is transpiled onto every connected physical layout and converted into the native gate basis

- CZ
- SX
- RZ
- X

using the standard Qiskit transpiler.

---

## Recorded Metrics

For every decomposition and every physical layout, the pipeline records

- CZ gate count
- SX gate count
- Circuit depth
- Hardware compatibility

Summary statistics are produced over all valid layouts for each decomposition.

---

## Generated Outputs

### `results.json`

Contains benchmarking results for every decomposition on every connected physical layout.

### `summary.json`

Contains aggregate statistics for each decomposition.

### `plots/`

Contains visual comparisons of the recorded hardware metrics.

---

## Requirements

- Python 3.13
- Qiskit
- NumPy
- Matplotlib

Install the required packages with

```bash
pip install qiskit numpy matplotlib
```

---

## Running the Pipeline

Verify all decompositions

```bash
python code/verify.py
```

Generate transpilation results

```bash
python code/transpile_all.py
```

Generate summary statistics

```bash
python code/analyze.py
```

Generate comparison plots

```bash
python code/visualize.py
```
