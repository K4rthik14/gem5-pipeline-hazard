# GEM5 Pipeline Hazard Analysis

> A Computer Organization & Architecture mini project analyzing data, control, and structural pipeline hazards using the GEM5 architectural simulator.

![Simulator](https://img.shields.io/badge/Simulator-GEM5-orange)
![Language](https://img.shields.io/badge/Language-C-blue)

## Overview

This project investigates the impact of **pipeline hazards** on processor performance using **GEM5**, an industry-standard computer architecture simulator.

Modern processors use pipelining to improve instruction throughput. However, hazards introduce stalls, pipeline flushes, and resource conflicts that reduce overall performance. Through a series of targeted experiments, this project demonstrates how different hazard types affect **Cycles Per Instruction (CPI)** and how modern processors mitigate these issues.

This work was completed as part of the **Computer Organization and Architecture (PBCST404)** course.

---

## Objectives

* Study the three major pipeline hazards.
* Simulate hazards using GEM5's **MinorCPU** (in-order pipeline).
* Measure CPI, pipeline stalls, and branch behavior.
* Analyze the effectiveness of common hardware mitigation techniques.

---

## Pipeline Hazards Covered

### Data Hazards

Instruction dependencies where an instruction requires data that has not yet been written by a previous instruction.

Examples:

* Read After Write (RAW)
* Write After Read (WAR)
* Write After Write (WAW)

Mitigation techniques:

* Forwarding / Bypassing
* Pipeline Stalling

---

### Control Hazards

Hazards introduced by branch and jump instructions where the next instruction cannot be determined immediately.

Mitigation techniques:

* Static Branch Prediction
* Dynamic Branch Prediction
* Delayed Branching

---

### Structural Hazards

Resource conflicts that occur when multiple instructions require the same hardware resource simultaneously.

Mitigation techniques:

* Resource Duplication
* Multiple Functional Units
* Pipelined Resources

---

## Repository Structure

```text
gem5-pipeline-hazard/
├── hazard_tests/
│   ├── data_hazard.c
│   ├── control_hazard.c
│   └── structural_hazard.c
├── plots/
│   └── hazard_comparison.png
└── README.md
```

---

## Experimental Setup

### Simulator

* GEM5
* X86 ISA
* MinorCPU
* Cache-enabled simulation

### Build GEM5

```bash
git clone https://github.com/gem5/gem5
cd gem5

scons build/X86/gem5.opt -j4
```

---

## Running Experiments

Compile a benchmark:

```bash
gcc -static -o data_hazard data_hazard.c
```

Run with GEM5:

```bash
./build/X86/gem5.opt configs/example/se.py \
    --cmd=./data_hazard \
    --cpu-type=MinorCPU \
    --caches
```

Inspect simulation statistics:

```bash
cat m5out/stats.txt | grep -E "cpi|stall|branch|ipc"
```

---

## Results

The experiments compare the performance impact of each pipeline hazard using metrics collected from `stats.txt`.

| Hazard Type       | Metric Observed       | Typical Effect       |
| ----------------- | --------------------- | -------------------- |
| Data Hazard       | Pipeline stalls       | Highest CPI increase |
| Control Hazard    | Branch mispredictions | Pipeline flushes     |
| Structural Hazard | Resource conflicts    | Execution delays     |

> Replace the table with your measured CPI, IPC, stall counts, and branch statistics from GEM5.

---

## Visualization

Simulation results can be visualized using Python and Matplotlib.

Example comparison:

* CPI across hazard types
* Pipeline stall counts
* Branch misprediction statistics

Include the generated plots inside the `plots/` directory.

---

## Key Learnings

* Instruction dependencies significantly increase pipeline stalls.
* Branch-heavy programs introduce control hazards and prediction penalties.
* Resource conflicts reduce throughput when hardware resources are limited.
* Hardware techniques such as forwarding, branch prediction, and resource duplication greatly improve pipeline performance.
* GEM5 provides an effective platform for studying processor microarchitecture beyond theoretical concepts.

---

## Technologies Used

* C
* GEM5 Simulator
* Python
* Matplotlib
* Linux

---

## Academic Context

**Course:** Computer Organization and Architecture (PBCST404)

This repository documents the implementation, experimentation, and analysis performed as part of the Semester 4 mini project.

---
