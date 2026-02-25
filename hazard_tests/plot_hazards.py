import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ─── Real GEM5 Results ───────────────────────────────────────────────────────
hazards   = ['Data Hazard\n(RAW Chain)', 'Control Hazard\n(Branch Loop)', 'Structural Hazard\n(Memory Conflict)']
cpi       = [12.488783, 8.641989, 2.653822]
ipc       = [0.080072,  0.115714, 0.376815]
colors    = ['#e74c3c', '#e67e22', '#2ecc71']
labels    = ['Data Hazard', 'Control Hazard', 'Structural Hazard']

x = np.arange(len(hazards))
width = 0.45


# ─── PLOT 1: CPI Bar Chart ────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(x, cpi, width, color=colors, edgecolor='white', linewidth=1.5)
ax.axhline(1.0, color='navy', linestyle='--', linewidth=1.2, label='Ideal CPI = 1.0')
ax.set_xticks(x)
ax.set_xticklabels(hazards, fontsize=11)
ax.set_ylabel('Cycles Per Instruction (CPI)', fontsize=12)
ax.set_title('CPI Comparison Across Hazard Types\n(X86MinorCPU In-Order Pipeline, GEM5 v23)', fontsize=13, fontweight='bold')
ax.set_ylim(0, 15)
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)
ax.set_axisbelow(True)
for bar, val in zip(bars, cpi):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.25,
            f'{val:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=12)
plt.tight_layout()
plt.savefig('plot1_cpi_comparison.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved: plot1_cpi_comparison.png")


# ─── PLOT 2: IPC Bar Chart ────────────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(x, ipc, width, color=colors, edgecolor='white', linewidth=1.5)
ax.axhline(1.0, color='navy', linestyle='--', linewidth=1.2, label='Ideal IPC = 1.0')
ax.set_xticks(x)
ax.set_xticklabels(hazards, fontsize=11)
ax.set_ylabel('Instructions Per Cycle (IPC)', fontsize=12)
ax.set_title('IPC Comparison Across Hazard Types\n(Higher is Better)', fontsize=13, fontweight='bold')
ax.set_ylim(0, 0.5)
ax.legend(fontsize=10)
ax.grid(axis='y', alpha=0.3)
ax.set_axisbelow(True)
for bar, val in zip(bars, ipc):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
            f'{val:.4f}', ha='center', va='bottom', fontweight='bold', fontsize=12)
plt.tight_layout()
plt.savefig('plot2_ipc_comparison.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved: plot2_ipc_comparison.png")


# ─── PLOT 3: Side-by-Side CPI and IPC ─────────────────────────────────────────
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
fig.suptitle('Pipeline Hazard Analysis — GEM5 Simulation Results\n(X86MinorCPU In-Order Pipeline with L1 Caches)',
             fontsize=13, fontweight='bold')

bars1 = ax1.bar(x, cpi, width, color=colors, edgecolor='white', linewidth=1.5)
ax1.axhline(1.0, color='navy', linestyle='--', linewidth=1.2, label='Ideal CPI = 1')
ax1.set_xticks(x); ax1.set_xticklabels(hazards, fontsize=10)
ax1.set_ylabel('CPI (Cycles Per Instruction)', fontsize=11)
ax1.set_title('CPI — Lower is Better', fontweight='bold')
ax1.set_ylim(0, 15); ax1.legend(fontsize=9); ax1.grid(axis='y', alpha=0.3); ax1.set_axisbelow(True)
for bar, val in zip(bars1, cpi):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.2,
             f'{val:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=11)

bars2 = ax2.bar(x, ipc, width, color=colors, edgecolor='white', linewidth=1.5)
ax2.axhline(1.0, color='navy', linestyle='--', linewidth=1.2, label='Ideal IPC = 1')
ax2.set_xticks(x); ax2.set_xticklabels(hazards, fontsize=10)
ax2.set_ylabel('IPC (Instructions Per Cycle)', fontsize=11)
ax2.set_title('IPC — Higher is Better', fontweight='bold')
ax2.set_ylim(0, 0.5); ax2.legend(fontsize=9); ax2.grid(axis='y', alpha=0.3); ax2.set_axisbelow(True)
for bar, val in zip(bars2, ipc):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
             f'{val:.4f}', ha='center', va='bottom', fontweight='bold', fontsize=11)

plt.tight_layout()
plt.savefig('plot3_combined.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved: plot3_combined.png")


# ─── PLOT 4: Performance Penalty vs Ideal ─────────────────────────────────────
ideal_cpi = 1.0
penalty   = [c - ideal_cpi for c in cpi]

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(x, penalty, width, color=colors, edgecolor='white', linewidth=1.5)
ax.set_xticks(x); ax.set_xticklabels(hazards, fontsize=11)
ax.set_ylabel('Extra Cycles Per Instruction (vs Ideal)', fontsize=12)
ax.set_title('Pipeline Penalty Overhead Compared to Ideal CPU\n(Extra CPI due to hazard stalls)', fontsize=13, fontweight='bold')
ax.set_ylim(0, 14)
ax.grid(axis='y', alpha=0.3); ax.set_axisbelow(True)
for bar, val in zip(bars, penalty):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
            f'+{val:.2f}', ha='center', va='bottom', fontweight='bold', fontsize=12, color='#c0392b')
plt.tight_layout()
plt.savefig('plot4_penalty.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved: plot4_penalty.png")


# ─── PLOT 5: Horizontal Severity Ranking ──────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 4))
h_labels = ['Structural Hazard\n(Memory Conflict)', 'Control Hazard\n(Branch Loop)', 'Data Hazard\n(RAW Chain)']
h_cpi    = [2.653822, 8.641989, 12.488783]
h_colors = ['#2ecc71', '#e67e22', '#e74c3c']

bars = ax.barh(h_labels, h_cpi, color=h_colors, edgecolor='white', linewidth=1.5, height=0.5)
ax.axvline(1.0, color='navy', linestyle='--', linewidth=1.2, label='Ideal CPI = 1.0')
ax.set_xlabel('CPI (Cycles Per Instruction)', fontsize=12)
ax.set_title('Hazard Severity Ranking — Worst to Best\n(GEM5 X86MinorCPU Real Results)', fontsize=13, fontweight='bold')
ax.legend(fontsize=10)
ax.grid(axis='x', alpha=0.3); ax.set_axisbelow(True)
for bar, val in zip(bars, h_cpi):
    ax.text(val + 0.15, bar.get_y() + bar.get_height()/2,
            f'CPI = {val:.2f}', va='center', fontweight='bold', fontsize=11)
ax.set_xlim(0, 15)
plt.tight_layout()
plt.savefig('plot5_severity_ranking.png', dpi=150, bbox_inches='tight', facecolor='white')
plt.close()
print("Saved: plot5_severity_ranking.png")


print("\nAll 5 plots saved successfully in hazard_tests/ folder!")
