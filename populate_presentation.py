import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pathlib import Path
import io
import shutil

BASE_DIR = Path(__file__).resolve().parent
template_path = BASE_DIR / "slides" / "Build1_Slide_Template.pptx"
img_tree_path = BASE_DIR / "slides" / "slide3_growth_tree.png"
img_chart_path = BASE_DIR / "slides" / "slide4_chart.png"

# Read template safely into memory
with open(template_path, 'rb') as f:
    template_bytes = io.BytesIO(f.read())

prs = pptx.Presentation(template_bytes)

# Colors
C_NAVY = RGBColor(15, 41, 74)
C_SLATE = RGBColor(51, 65, 85)
C_DARK = RGBColor(30, 41, 59)
C_GREEN = RGBColor(21, 128, 61)
C_RED = RGBColor(185, 28, 28)

def format_para(p, text, font_name='Arial', size_pt=14, bold=False, italic=False, color=C_DARK, space_after=6):
    p.text = text
    p.font.name = font_name
    p.font.size = Pt(size_pt)
    p.font.bold = bold
    p.font.italic = italic
    p.font.color.rgb = color
    p.space_after = Pt(space_after)

# =========================================================================
# SLIDE 1: Title
# =========================================================================
s1 = prs.slides[0]
for shape in s1.shapes:
    if shape.has_text_frame:
        t = shape.text_frame.text
        if 'BRIEF' in t and ('<LETTER>' in t or 'BRIEF A' in t):
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'BRIEF A · GROWTH H1 2025 vs H1 2026 · GROUP 2', 'Arial', 11, bold=True, color=RGBColor(2, 132, 199))
        elif '<The question, as a title>' in t or 'Where Did the Growth Come From' in t:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'Where Did the Growth Come From — and Why Did Jaipur and Chennai Lag?', 'Georgia', 34, bold=True, color=C_NAVY)
        elif '<The claim, in one sentence' in t or 'Test results grew 5.75%' in t:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'Test results grew 5.75% from H1 2025 to H1 2026 (357,769 to 378,358 rows), propelled by a 37.7% surge in home collection and 35.2% package test adoption, while clinic results declined 12.1% and patient acquisition lagged in Jaipur (-9.9%) and Chennai (+1.3%).', 'Arial', 14, color=C_SLATE)
        elif '<Member>' in t or 'Harshal Patil' in t:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'Harshal Patil · Kshitij · Gaurang', 'Arial', 12, bold=True, color=C_NAVY)

# =========================================================================
# SLIDE 2: 1 · THE QUESTION
# =========================================================================
s2 = prs.slides[1]
for shape in s2.shapes:
    if shape.has_text_frame:
        t = shape.text_frame.text
        if "<Dr Menon's words" in t or 'Dr Menon' in t:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, "Dr Menon's words, and our translation", 'Georgia', 26, bold=True, color=C_NAVY)
        elif 'Her words:' in t:
            tf = shape.text_frame
            tf.clear()
            
            p1 = tf.paragraphs[0]
            format_para(p1, 'Her words:', 'Arial', 13, bold=True, color=C_NAVY, space_after=3)
            
            p2 = tf.add_paragraph()
            format_para(p2, '“We grew 5% in H1 2026, but I need to know where that growth came from. Is it new patients or existing ones coming back? Are clinics driving it or home collection? And why are Jaipur and Chennai missing their targets?”', 'Georgia', 12.5, italic=True, color=C_DARK, space_after=12)
            
            p3 = tf.add_paragraph()
            format_para(p3, 'Our translation:', 'Arial', 13, bold=True, color=C_NAVY, space_after=3)
            
            p4 = tf.add_paragraph()
            format_para(p4, 'A multiplicative Growth Tree (Results = Patients × Visits/Patient × Tests/Visit × Results/Test Booked) combined with Channel Shift (+13.5 pp Home vs -7.7 pp Clinic), Package expansion (12.5% to 15.9% share), and Plan Attainment analysis across all six cities.', 'Arial', 12, color=C_DARK, space_after=12)
            
            p5 = tf.add_paragraph()
            format_para(p5, 'The decision it drives:', 'Arial', 13, bold=True, color=C_NAVY, space_after=3)
            
            p6 = tf.add_paragraph()
            format_para(p6, 'Fleet capital reallocation toward scaling home phlebotomy capacity (+37.7% growth) versus consolidating clinic overheads (-12.1%), plus restructuring commercial patient acquisition in lagging markets (Jaipur -9.9%, Chennai +1.3%).', 'Arial', 12, color=C_DARK, space_after=0)

# =========================================================================
# SLIDE 3: 2 · THE PICTURE
# =========================================================================
s3 = prs.slides[2]
for shape in s3.shapes:
    if shape.has_text_frame:
        t = shape.text_frame.text
        if '<Your completed diagram' in t or 'The Growth Tree' in t:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'The Growth Tree & Channel Decomposition: H1 2025 vs H1 2026', 'Georgia', 24, bold=True, color=C_NAVY)
        elif '[Insert the diagram' in t:
            shape.text_frame.clear()

has_pic3 = any(s.shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.PICTURE and s.name != 'Picture 4' for s in s3.shapes)
if not has_pic3 and img_tree_path.exists():
    s3.shapes.add_picture(str(img_tree_path), Inches(0.55), Inches(1.85), Inches(12.20), Inches(4.50))

# =========================================================================
# SLIDE 4: 3 · THE CLAIM
# =========================================================================
s4 = prs.slides[3]
for shape in s4.shapes:
    if shape.has_text_frame:
        t = shape.text_frame.text
        if '<One sentence>' in t or 'The one sentence' in t:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'The one sentence Dr Menon can say to her board', 'Georgia', 24, bold=True, color=C_NAVY)
        elif '<The sentence Dr Menon can say' in t or 'Kalpa grew test volume' in t:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, '“Kalpa grew test volume by 5.75% (378,358 results across six cities in H1 2026 vs 357,769 in H1 2025), driven entirely by a 37.7% surge in home collection (+13.5 pp) and 35.2% growth in health packages (+4.4 pp), masking a 12.1% clinic volume decline (-7.7 pp) and acute patient acquisition shortfalls in Jaipur (-9.9%) and Chennai (+1.3%).”', 'Georgia', 22, italic=True, color=C_NAVY)

# =========================================================================
# SLIDE 5: 4 · THE EVIDENCE
# =========================================================================
s5 = prs.slides[4]
for shape in s5.shapes:
    if shape.has_text_frame:
        t = shape.text_frame.text
        if '<Two or three numbers' in t or 'Channel shift' in t:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'Channel shift, package lift, and regional shortfall', 'Georgia', 24, bold=True, color=C_NAVY)
        elif 'Number 1:' in t or 'Number 1 ·' in t:
            tf = shape.text_frame
            tf.clear()
            
            p1 = tf.paragraphs[0]
            format_para(p1, 'Number 1 · Channel Divergence:', 'Arial', 12, bold=True, color=C_NAVY, space_after=2)
            p1_b = tf.add_paragraph()
            format_para(p1_b, 'Home collection grew +37.7% (152,709 vs 110,929 results; +13.5 pp contribution) across every city, while clinic results fell -12.1% (223,727 vs 245,042; -7.7 pp drag).', 'Arial', 10.5, color=C_DARK, space_after=10)
            
            p2 = tf.add_paragraph()
            format_para(p2, 'Number 2 · Package Adoption:', 'Arial', 12, bold=True, color=C_NAVY, space_after=2)
            p2_b = tf.add_paragraph()
            format_para(p2_b, 'Package tests (PK01–PK04) surged +35.2% (60,110 vs 44,467 rows), expanding package share from 12.5% to 15.9% across channels (+4.4 pp contribution), while routine single tests grew only +1.6%.', 'Arial', 10.5, color=C_DARK, space_after=10)
            
            p3 = tf.add_paragraph()
            format_para(p3, 'Number 3 · Regional Shortfall vs Plan:', 'Arial', 12, bold=True, color=C_NAVY, space_after=2)
            p3_b = tf.add_paragraph()
            format_para(p3_b, 'Jaipur (-9.9% YoY) and Chennai (+1.3% YoY) attained only 63.6% and 70.4% of H1 2026 plan targets (vs ~75% other cities) due to a -12.1% and -5.0% collapse in unique patients; lab fulfilment stayed rock solid at 82.5%–83.3%.', 'Arial', 10.5, color=C_DARK, space_after=0)
            
        elif '[Insert slides/slide4_chart.png]' in t:
            shape.text_frame.clear()

has_pic5 = any(s.shape_type == pptx.enum.shapes.MSO_SHAPE_TYPE.PICTURE and s.name != 'Picture 4' for s in s5.shapes)
if not has_pic5 and img_chart_path.exists():
    s5.shapes.add_picture(str(img_chart_path), Inches(6.05), Inches(1.85), Inches(6.70), Inches(4.50))

# =========================================================================
# SLIDE 6: 5 · THE CAVEAT AND THE ALTERNATIVE
# =========================================================================
s6 = prs.slides[5]
for shape in s6.shapes:
    if shape.has_text_frame:
        t = shape.text_frame.text
        if '<What would change the claim' in t or 'What would change' in t:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'What would change the claim; the approach we rejected', 'Georgia', 24, bold=True, color=C_NAVY)
        elif 'The one thing that would change this claim:' in t:
            tf = shape.text_frame
            tf.clear()
            
            p1 = tf.paragraphs[0]
            format_para(p1, 'The one thing that would change this claim:', 'Arial', 13, bold=True, color=C_NAVY, space_after=3)
            
            p2 = tf.add_paragraph()
            format_para(p2, 'Package unbundling in lab accounting: A package (PK01–PK04) is logged as a single row in results tables. If each package bundles 4 to 6 discrete clinical lab tests, true clinical test volume grew by ~11% to 13% rather than 5.75%, making the home wellness transition even more dominant. (Additionally, 3,720 orphan results without bookings add +0.03 pp, and 94 null test codes remain UNKNOWN).', 'Arial', 11.5, color=C_DARK, space_after=14)
            
            p3 = tf.add_paragraph()
            format_para(p3, 'The approach we rejected on the way here:', 'Arial', 13, bold=True, color=C_NAVY, space_after=3)
            
            p4 = tf.add_paragraph()
            format_para(p4, 'Attributing Jaipur and Chennai shortfalls to the Nova software migration in April 2026. Four rigorous checks disproved this: (1) The growth deficit was already present in January 2026 (-0.2% vs +9.5% other cities), 3 months before Nova launched; (2) Returning patient retention is actually higher (37.4% & 35.8% vs ~30%); (3) Patient ID syntax is identical; (4) Lab fulfilment (results per test booked) remained unaffected at 0.82–0.83. The problem is commercial demand/patient acquisition, not IT.', 'Arial', 11.5, color=C_DARK, space_after=0)

# =========================================================================
# SLIDE 7: 6 · THE ACTION
# =========================================================================
s7 = prs.slides[6]
for shape in s7.shapes:
    if shape.has_text_frame:
        t = shape.text_frame.text
        if '<What to do, what it costs' in t or 'What to do' in t:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'What to do, what it costs, what being wrong costs', 'Georgia', 24, bold=True, color=C_NAVY)
        elif 'Do: <the action' in t or 'Do (on Monday morning):' in t:
            tf = shape.text_frame
            tf.clear()
            
            p1 = tf.paragraphs[0]
            format_para(p1, 'Do (on Monday morning):', 'Arial', 12.5, bold=True, color=C_NAVY, space_after=2)
            p1_b = tf.add_paragraph()
            format_para(p1_b, '(1) Reallocate digital acquisition spend directly to patient acquisition in Jaipur and Chennai; (2) Expand home collection phlebotomist capacity by 25% across Bengaluru, Pune, and Ahmedabad; (3) Bundle routine single tests into wellness packages.', 'Arial', 11, color=C_DARK, space_after=10)
            
            p2 = tf.add_paragraph()
            format_para(p2, 'It costs:', 'Arial', 12.5, bold=True, color=C_NAVY, space_after=2)
            p2_b = tf.add_paragraph()
            format_para(p2_b, 'Reallocating ~Rs 15–20 Lakhs of existing H2 acquisition spend + onboarding ~30 contract phlebotomists (~Rs 9 Lakhs/month variable labor).', 'Arial', 11, color=C_DARK, space_after=10)
            
            p3 = tf.add_paragraph()
            format_para(p3, 'If we are wrong, it costs:', 'Arial', 12.5, bold=True, color=C_NAVY, space_after=2)
            p3_b = tf.add_paragraph()
            format_para(p3_b, 'Temporary excess phlebotomist idle hours in Q3 (which can be downscaled within 30 days), compared to the severe permanent penalty of losing clinic volume with no home offset.', 'Arial', 11, color=C_DARK, space_after=10)
            
            p4 = tf.add_paragraph()
            format_para(p4, 'What we would do with two more days:', 'Arial', 12.5, bold=True, color=C_NAVY, space_after=2)
            p4_b = tf.add_paragraph()
            format_para(p4_b, 'Connect billing and settlement tables to calculate unit contribution margin per home visit vs clinic visit, accounting for the Rs 150 home fee versus clinic fixed real estate overhead.', 'Arial', 11, color=C_DARK, space_after=0)

# =========================================================================
# SLIDE 8: Questions
# =========================================================================
s8 = prs.slides[7]
for shape in s8.shapes:
    if shape.has_text_frame:
        t = shape.text_frame.text
        if 'The approach log' in t:
            tf = shape.text_frame
            tf.clear()
            p1 = tf.paragraphs[0]
            format_para(p1, 'The approach log, decisions log, and challenges log are open in the repository:', 'Arial', 14, color=C_DARK, space_after=12)
            p2 = tf.add_paragraph()
            format_para(p2, 'https://github.com/harshal-caa/c2-build1-brief-c-group-2', 'Arial', 16, bold=True, color=RGBColor(2, 132, 199), space_after=0)

# =========================================================================
# SLIDE 9: APPENDIX A
# =========================================================================
s9 = prs.slides[8]
for shape in s9.shapes:
    if shape.has_text_frame:
        t = shape.text_frame.text
        if 'Appendix A' in t and shape.name == 'TextBox 6':
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'Appendix A · The decisions that moved the headline', 'Georgia', 24, bold=True, color=C_NAVY)
        elif 'Rule 1:' in t or 'Rule 1 ·' in t:
            tf = shape.text_frame
            tf.clear()
            
            p1 = tf.paragraphs[0]
            format_para(p1, 'Rule 1 · Timestamp Parsing Harmonization:', 'Arial', 12, bold=True, color=C_NAVY, space_after=2)
            p1_b = tf.add_paragraph()
            format_para(p1_b, 'Correcting mixed ISO (+05:30) vs DD/MM/YYYY formats prevented 78,000 legitimate H1 bookings from misclassifying into Jul–Dec.', 'Arial', 10.5, color=C_DARK, space_after=8)
            
            p2 = tf.add_paragraph()
            format_para(p2, 'Rule 2 · Nova Duplicate Rescheduled Bookings Filter:', 'Arial', 12, bold=True, color=C_NAVY, space_after=2)
            p2_b = tf.add_paragraph()
            format_para(p2_b, 'Filtered 1,500 rescheduled duplicate rows in Nova (Jaipur & Chennai) which never receive lab results, restoring accurate test fulfilment rates to 83.8%.', 'Arial', 10.5, color=C_DARK, space_after=8)
            
            p3 = tf.add_paragraph()
            format_para(p3, 'Rule 3 · 1-to-1 Null Test Code Recovery:', 'Arial', 12, bold=True, color=C_NAVY, space_after=2)
            p3_b = tf.add_paragraph()
            format_para(p3_b, 'Recovered 2,108 null test codes (1,019 in 2025, 1,089 in 2026) by matching unique booked tests on the same booking ID; 94 unrecoverable rows labeled UNKNOWN.', 'Arial', 10.5, color=C_DARK, space_after=8)
            
            p4 = tf.add_paragraph()
            format_para(p4, 'Rule 4 · Geographic Standardization:', 'Arial', 12, bold=True, color=C_NAVY, space_after=2)
            p4_b = tf.add_paragraph()
            format_para(p4_b, 'Normalized "Bangalore" to "Bengaluru" and attributed orphan result rows using booking ID city prefixes (e.g. BK-AHM, BK-CHE).', 'Arial', 10.5, color=C_DARK, space_after=0)

# =========================================================================
# SLIDE 10: APPENDIX B
# =========================================================================
s10 = prs.slides[9]
for shape in s10.shapes:
    if shape.has_text_frame:
        t = shape.text_frame.text
        if 'Appendix B' in t and shape.name == 'TextBox 6':
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            format_para(p, 'Appendix B · The cold run verification', 'Georgia', 24, bold=True, color=C_NAVY)
        elif 'Fresh Codespace' in t or 'Test Environment:' in t:
            tf = shape.text_frame
            tf.clear()
            
            p1 = tf.paragraphs[0]
            format_para(p1, 'Test Environment: Fresh GitHub Codespace / local Python 3.12+ execution', 'Arial', 12, bold=True, color=C_NAVY, space_after=4)
            
            p2 = tf.add_paragraph()
            format_para(p2, 'Runtime: 2 min 45 sec for full pipeline ingestion, cleaning, and reconciliation', 'Arial', 11, color=C_DARK, space_after=6)
            
            p3 = tf.add_paragraph()
            format_para(p3, 'Headline Number: +5.75% (H1 2025: 357,769 -> H1 2026: 378,358 rows), exact match', 'Arial', 11, bold=True, color=C_GREEN, space_after=6)
            
            p4 = tf.add_paragraph()
            format_para(p4, 'Mathematical Reconciliation: Multiplicative tree error = 0.000%; channel contribution sum = 5.75 pp', 'Arial', 11, color=C_DARK, space_after=6)
            
            p5 = tf.add_paragraph()
            format_para(p5, 'Git Tracking: Branch harshal_branch | Commit verified & reproducible', 'Arial', 11, color=C_SLATE, space_after=0)

# Save presentation safely to temporary in-memory buffer
temp_buf = io.BytesIO()
prs.save(temp_buf)
content = temp_buf.getvalue()

targets = [
    BASE_DIR / 'slides' / 'Brief_A_Growth_Presentation.pptx',
    BASE_DIR / 'brief_a_kshitij' / 'Brief_A_Growth_Presentation.pptx'
]

saved_paths = []
locked_paths = []

for target in targets:
    try:
        with open(target, 'wb') as f:
            f.write(content)
        saved_paths.append(str(target))
    except PermissionError:
        locked_paths.append(str(target))
        # Save to fallback file so updated version is immediately available
        fallback = target.parent / (target.stem + "_updated.pptx")
        with open(fallback, 'wb') as f:
            f.write(content)
        saved_paths.append(f"{fallback} (fallback, original was open in PowerPoint)")

print("Presentation generation completed:")
for s in saved_paths:
    print(f"  Saved: {s}")
if locked_paths:
    print("  Note: The following files were locked by PowerPoint:")
    for l in locked_paths:
        print(f"    - {l}")
    print("  Close PowerPoint and re-run if you want to overwrite the open file directly.")
