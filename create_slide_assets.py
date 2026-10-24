import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

BASE_DIR = Path(__file__).resolve().parent
slides_dir = BASE_DIR / 'slides'
slides_dir.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------------------
# 1. SLIDE 3: GROWTH TREE & CHANNEL SHIFT
# -------------------------------------------------------------------------
plt.style.use('default')
fig, ax = plt.subplots(figsize=(13, 6.8), dpi=300)
fig.patch.set_facecolor('#FFFFFF')
ax.set_facecolor('#FFFFFF')

ax.axis('off')
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

navy = '#0F294A'
teal = '#0E7490'
gold = '#D97706'
slate = '#334155'
green = '#15803D'
red = '#B91C1C'

ax.text(50, 96, "The Multiplicative Growth Tree & Channel Shift (H1 2025 vs H1 2026)", 
        fontsize=16, fontweight='bold', color=navy, ha='center', fontfamily='sans-serif')

root_box = patches.FancyBboxPatch((32, 77), 36, 14, boxstyle="round,pad=0.8,rounding_size=1.5", 
                                  fc='#E0F2FE', ec='#0284C7', lw=2)
ax.add_patch(root_box)
ax.text(50, 86.5, "Total Test Results Volume", fontsize=13, fontweight='bold', color=navy, ha='center')
ax.text(50, 82.5, "H1 2025: 357,769   ->   H1 2026: 378,358", fontsize=11, color=slate, ha='center')
ax.text(50, 78.5, "Actual Growth: +5.75% (+20,589 results)", fontsize=11.5, fontweight='bold', color='#0369A1', ha='center')

branches = [
    {"name": "1. Unique Patients", "val25": "204,444", "val26": "212,126", "growth": "+3.76%", "color": green, "x": 12.5},
    {"name": "2. Visits / Patient", "val25": "1.488", "val26": "1.474", "growth": "-0.98%", "color": red, "x": 37.5},
    {"name": "3. Tests / Visit", "val25": "1.411", "val26": "1.442", "growth": "+2.19%", "color": green, "x": 62.5},
    {"name": "4. Results / Test", "val25": "0.832", "val26": "0.838", "growth": "+0.72%", "color": green, "x": 87.5},
]

for b in branches:
    ax.annotate('', xy=(b['x'], 65), xytext=(50, 77),
                arrowprops=dict(arrowstyle='->', color='#94A3B8', lw=1.8, shrinkA=0, shrinkB=0))
    
    box = patches.FancyBboxPatch((b['x'] - 11, 46), 22, 18, boxstyle="round,pad=0.6,rounding_size=1.2",
                                fc='#F8FAFC', ec='#CBD5E1', lw=1.5)
    ax.add_patch(box)
    
    ax.text(b['x'], 60, b['name'], fontsize=11, fontweight='bold', color=navy, ha='center')
    ax.text(b['x'], 55.5, f"2025: {b['val25']}", fontsize=10, color=slate, ha='center')
    ax.text(b['x'], 51.5, f"2026: {b['val26']}", fontsize=10, color=slate, ha='center')
    ax.text(b['x'], 47.5, f"Growth: {b['growth']}", fontsize=11, fontweight='bold', color=b['color'], ha='center')

ax.text(50, 41, "(1 + 3.76%)  x  (1 - 0.98%)  x  (1 + 2.19%)  x  (1 + 0.72%)  =  1 + 5.75%  (Exact Product, Gap = 0.0%)",
        fontsize=10.5, fontstyle='italic', color='#475569', ha='center', bbox=dict(boxstyle='square,pad=0.3', fc='#F1F5F9', ec='none'))

ch_title_box = patches.Rectangle((4, 28), 92, 0.4, fc='#CBD5E1', ec='none')
ax.add_patch(ch_title_box)
ax.text(50, 31, "CHANNEL BREAKDOWN & CONTRIBUTION TO TOTAL GROWTH", fontsize=12, fontweight='bold', color=navy, ha='center')

# Home
home_box = patches.FancyBboxPatch((6, 6), 41, 20, boxstyle="round,pad=0.6,rounding_size=1.2",
                                 fc='#F0FDF4', ec='#86EFAC', lw=1.5)
ax.add_patch(home_box)
ax.text(26.5, 22, "HOME COLLECTION (High Growth Engine)", fontsize=11, fontweight='bold', color=green, ha='center')
ax.text(26.5, 17.5, "Results: 110,929  ->  152,709 (+37.66%)", fontsize=10.5, color=slate, ha='center')
ax.text(26.5, 13.5, "Patients: +26.25%  |  Visits/Pt: +6.83%  |  Tests/V: +1.89%", fontsize=9.5, color=slate, ha='center')
ax.text(26.5, 9, "Growth Contribution: +13.46 percentage points", fontsize=10.5, fontweight='bold', color=green, ha='center')

# Clinic
clinic_box = patches.FancyBboxPatch((53, 6), 41, 20, boxstyle="round,pad=0.6,rounding_size=1.2",
                                   fc='#FEF2F2', ec='#FECACA', lw=1.5)
ax.add_patch(clinic_box)
ax.text(73.5, 22, "CLINIC VISITS (Erosion Across All Cities)", fontsize=11, fontweight='bold', color=red, ha='center')
ax.text(73.5, 17.5, "Results: 245,042  ->  223,727 (-12.14%)", fontsize=10.5, color=slate, ha='center')
ax.text(73.5, 13.5, "Patients: -8.28%  |  Visits/Pt: -6.08%  |  Tests/V: +2.35%", fontsize=9.5, color=slate, ha='center')
ax.text(73.5, 9, "Growth Drag: -7.74 percentage points", fontsize=10.5, fontweight='bold', color=red, ha='center')

plt.tight_layout()
plt.savefig(str(slides_dir / 'slide3_growth_tree.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Generated slides/slide3_growth_tree.png")

# -------------------------------------------------------------------------
# 2. SLIDE 5: MULTI-PANEL EVIDENCE CHART
# -------------------------------------------------------------------------
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5.2), dpi=300)
fig.patch.set_facecolor('#FFFFFF')

channels = ['Clinic', 'Home']
y2025 = [245042, 110929]
y2026 = [223727, 152709]
x = np.arange(len(channels))
width = 0.35

ax1.set_facecolor('#FAFAFA')
r1 = ax1.bar(x - width/2, y2025, width, label='H1 2025', color='#94A3B8')
r2 = ax1.bar(x + width/2, y2026, width, label='H1 2026', color=['#EF4444', '#10B981'])

ax1.set_title("A. Channel Volume Shift (Results)", fontsize=12, fontweight='bold', color=navy, pad=12)
ax1.set_xticks(x)
ax1.set_xticklabels(channels, fontsize=11, fontweight='bold')
ax1.set_ylabel("Result Rows", fontsize=10, color=slate)
ax1.legend(frameon=True, facecolor='#FFFFFF')
ax1.grid(axis='y', linestyle='--', alpha=0.5)

ax1.text(0 - width/2, y2025[0] + 4000, f"{y2025[0]:,}", ha='center', fontsize=9, color=slate)
ax1.text(0 + width/2, y2026[0] + 4000, f"{y2026[0]:,}\n(-12.1%)", ha='center', fontsize=9, fontweight='bold', color='#DC2626')
ax1.text(1 - width/2, y2025[1] + 4000, f"{y2025[1]:,}", ha='center', fontsize=9, color=slate)
ax1.text(1 + width/2, y2026[1] + 4000, f"{y2026[1]:,}\n(+37.7%)", ha='center', fontsize=9, fontweight='bold', color='#059669')
ax1.set_ylim(0, 300000)

cities = ['Ahmedabad', 'Bengaluru', 'Chennai', 'Hyderabad', 'Jaipur', 'Pune']
attainment = [76.8, 73.9, 70.4, 74.9, 63.6, 74.7]
colors = ['#0EA5E9', '#0EA5E9', '#F97316', '#0EA5E9', '#EF4444', '#0EA5E9']

ax2.set_facecolor('#FAFAFA')
bars = ax2.barh(cities, attainment, color=colors, height=0.6)
ax2.axvline(73.0, color='#64748B', linestyle='--', linewidth=1.5, label='Total Attain: 73.0%')
ax2.axvline(100.0, color='#22C55E', linestyle=':', linewidth=1.5, label='Plan Target (100%)')
ax2.set_title("B. Plan Attainment % by City (Results)", fontsize=12, fontweight='bold', color=navy, pad=12)
ax2.set_xlabel("% of H1 2026 Plan Target Achieved", fontsize=10, color=slate)
ax2.grid(axis='x', linestyle='--', alpha=0.5)
ax2.set_xlim(0, 115)
ax2.legend(loc='lower right', fontsize=8.5, frameon=True)

for bar in bars:
    w = bar.get_width()
    ax2.text(w + 1.5, bar.get_y() + bar.get_height()/2, f"{w:.1f}%", va='center', fontsize=9, fontweight='bold', color=slate)

pkg_cats = ['Packages\n(PK01-04)', 'Routine Tests\n(Non-Package)']
pkg_25 = [44467, 313302]
pkg_26 = [60110, 318248]
x_pkg = np.arange(len(pkg_cats))

ax3.set_facecolor('#FAFAFA')
r3 = ax3.bar(x_pkg - width/2, pkg_25, width, label='H1 2025', color='#94A3B8')
r4 = ax3.bar(x_pkg + width/2, pkg_26, width, label='H1 2026', color=['#8B5CF6', '#3B82F6'])

ax3.set_title("C. Package (+35.2%) vs Routine (+1.6%)", fontsize=12, fontweight='bold', color=navy, pad=12)
ax3.set_xticks(x_pkg)
ax3.set_xticklabels(pkg_cats, fontsize=10.5, fontweight='bold')
ax3.set_ylabel("Result Rows", fontsize=10, color=slate)
ax3.legend(frameon=True, facecolor='#FFFFFF')
ax3.grid(axis='y', linestyle='--', alpha=0.5)

ax3.text(0 - width/2, pkg_25[0] + 6000, f"{pkg_25[0]:,}\n(12.5%)", ha='center', fontsize=8.5, color=slate)
ax3.text(0 + width/2, pkg_26[0] + 6000, f"{pkg_26[0]:,}\n(15.9%)", ha='center', fontsize=8.5, fontweight='bold', color='#7C3AED')
ax3.text(1 - width/2, pkg_25[1] + 6000, f"{pkg_25[1]:,}", ha='center', fontsize=8.5, color=slate)
ax3.text(1 + width/2, pkg_26[1] + 6000, f"{pkg_26[1]:,}\n(+1.6%)", ha='center', fontsize=8.5, fontweight='bold', color='#2563EB')
ax3.set_ylim(0, 360000)

plt.tight_layout()
plt.savefig(str(slides_dir / 'slide4_chart.png'), dpi=300, bbox_inches='tight')
plt.close()
print("Generated slides/slide4_chart.png")
