import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# Sheet 1: Board Number & Headline
ws1 = wb.active
ws1.title = "Board Number"
ws1.views.sheetView[0].showGridLines = True

# Fonts and Fills
font_header = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
font_sub = Font(name="Calibri", size=11, bold=True, color="0F294A")
font_bold = Font(name="Calibri", size=11, bold=True)
font_regular = Font(name="Calibri", size=11)
font_italic = Font(name="Calibri", size=10, italic=True)

fill_navy = PatternFill(start_color="0F294A", end_color="0F294A", fill_type="solid")
fill_light_blue = PatternFill(start_color="E0F2FE", end_color="E0F2FE", fill_type="solid")
fill_light_green = PatternFill(start_color="DCFCE7", end_color="DCFCE7", fill_type="solid")
fill_light_red = PatternFill(start_color="FEE2E2", end_color="FEE2E2", fill_type="solid")

thin_border = Border(
    left=Side(style='thin', color='CBD5E1'),
    right=Side(style='thin', color='CBD5E1'),
    top=Side(style='thin', color='CBD5E1'),
    bottom=Side(style='thin', color='CBD5E1')
)

ws1.merge_cells("A1:E1")
ws1["A1"] = "KALPA HEALTH · EXECUTIVE BOARD METRICS · BRIEF A (GROWTH H1 2025 vs H1 2026)"
ws1["A1"].font = font_header
ws1["A1"].fill = fill_navy
ws1["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws1.row_dimensions[1].height = 32

data_board = [
    ["Metric", "H1 2025", "H1 2026", "Absolute Delta", "Growth % / Contribution"],
    ["Total Test Results (Board Headline)", 357769, 378358, 20589, "+5.75%"],
    ["Unique Patients", 204444, 212126, 7682, "+3.76%"],
    ["Visits per Patient", 1.4883, 1.4737, -0.0146, "-0.98%"],
    ["Tests Booked per Visit", 1.4111, 1.4420, 0.0309, "+2.19%"],
    ["Results per Test Booked (Fulfilment)", 0.8322, 0.8382, 0.0060, "+0.72%"],
    ["", "", "", "", ""],
    ["CHANNEL BREAKDOWN", "H1 2025 Results", "H1 2026 Results", "Growth Rate", "Growth Contribution (pp)"],
    ["Home Collection", 110929, 152709, "+37.66%", "+13.46 pp"],
    ["Clinic Visits", 245042, 223727, "-12.14%", "-7.74 pp"],
    ["Unmatched / Inferred", 1798, 1922, "+6.90%", "+0.03 pp"],
    ["Total Results", 357769, 378358, "+5.75%", "+5.75 pp"],
    ["", "", "", "", ""],
    ["PACKAGE vs ROUTINE TESTS", "H1 2025 Results", "H1 2026 Results", "Growth Rate", "Share of Total (2025 -> 2026)"],
    ["Packages (PK01 to PK04)", 44467, 60110, "+35.18%", "12.43% -> 15.89% (+3.46 pp)"],
    ["Routine Tests (Non-Package)", 313302, 318248, "+1.58%", "87.57% -> 84.11% (-3.46 pp)"]
]

for r_idx, row in enumerate(data_board, start=3):
    for c_idx, val in enumerate(row, start=1):
        cell = ws1.cell(row=r_idx, column=c_idx, value=val)
        cell.font = font_regular
        cell.border = thin_border
        if r_idx in [3, 10, 16]:
            cell.font = font_bold
            cell.fill = fill_light_blue
        if c_idx in [2, 3, 4] and isinstance(val, (int, float)):
            cell.number_format = '#,##0.0000' if isinstance(val, float) else '#,##0'
            cell.alignment = Alignment(horizontal="right")
        elif c_idx == 5:
            cell.alignment = Alignment(horizontal="center")
            if "+37" in str(val) or "+13" in str(val) or "+35" in str(val):
                cell.font = Font(name="Calibri", size=11, bold=True, color="047857")
            elif "-12" in str(val) or "-7" in str(val):
                cell.font = Font(name="Calibri", size=11, bold=True, color="B91C1C")

# Sheet 2: City Breakdown & Plan Comparison
ws2 = wb.create_sheet(title="City Attainment & Growth")
ws2.views.sheetView[0].showGridLines = True

ws2.merge_cells("A1:G1")
ws2["A1"] = "CITY-WISE VOLUME, GROWTH & H1 2026 PLAN ATTAINMENT"
ws2["A1"].font = font_header
ws2["A1"].fill = fill_navy
ws2["A1"].alignment = Alignment(horizontal="center", vertical="center")
ws2.row_dimensions[1].height = 32

city_headers = ["City", "H1 2025 Actual", "H1 2026 Actual", "Growth %", "H1 2026 Plan Target", "Variance vs Plan", "Plan Attainment %"]
city_data = [
    ["Ahmedabad", 62828, 69737, "+11.00%", 90773, -21036, "76.8%"],
    ["Bengaluru", 81457, 88707, "+8.90%", 120085, -31378, "73.9%"],
    ["Chennai", 65243, 66108, "+1.33%", 93912, -27804, "70.4%"],
    ["Hyderabad", 59918, 64687, "+7.96%", 86421, -21734, "74.9%"],
    ["Jaipur", 36950, 33297, "-9.89%", 52372, -19075, "63.6%"],
    ["Pune", 49575, 53907, "+8.75%", 72177, -18270, "74.7%"],
    ["Total / Average", 355971, 376443, "+5.75%", 515740, -139297, "73.0%"]
]

for c_idx, h in enumerate(city_headers, start=1):
    cell = ws2.cell(row=3, column=c_idx, value=h)
    cell.font = font_bold
    cell.fill = fill_light_blue
    cell.border = thin_border
    cell.alignment = Alignment(horizontal="center")

for r_idx, row in enumerate(city_data, start=4):
    for c_idx, val in enumerate(row, start=1):
        cell = ws2.cell(row=r_idx, column=c_idx, value=val)
        cell.font = font_bold if r_idx == 10 else font_regular
        cell.border = thin_border
        if c_idx in [2, 3, 5, 6] and isinstance(val, int):
            cell.number_format = '#,##0'
            cell.alignment = Alignment(horizontal="right")
        elif c_idx in [4, 7]:
            cell.alignment = Alignment(horizontal="center")
            if "Jaipur" in str(row[0]) or "Chennai" in str(row[0]):
                cell.fill = fill_light_red

for ws in [ws1, ws2]:
    for col in ws.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws.column_dimensions[col_letter].width = max(max_len + 4, 15)

wb.save("slides/board_number.xlsx")
print("Generated slides/board_number.xlsx")
