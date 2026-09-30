import io
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_regulatory_pdf(disease_data, divergence_res):
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
    story = []
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=20, leading=24, textColor=colors.HexColor('#0B1220'))
    sub_title_style = ParagraphStyle('SubTitle', parent=styles['Normal'], fontName='Helvetica', fontSize=10, leading=14, textColor=colors.HexColor('#4A5568'))
    section_style = ParagraphStyle('SectionHeading', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=colors.HexColor('#1A202C'), spaceAfter=6)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor('#2D3748'))

    story.append(Paragraph("Cross-Species Translational Fidelity Atlas", title_style))
    story.append(Paragraph("FAIR-Compliant Regulatory Benchmarking Report", sub_title_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("1. FAIR Dataset & Ontology Metadata", section_style))
    ont = disease_data.get("ontology", {})
    meta_table_data = [
        [Paragraph("<b>Disease Name</b>", body_style), Paragraph(str(disease_data.get("disease")), body_style), Paragraph("<b>MONDO ID</b>", body_style), Paragraph(str(ont.get("disease_id")), body_style)],
        [Paragraph("<b>Organ UBERON ID</b>", body_style), Paragraph(str(ont.get("organ_id")), body_style), Paragraph("<b>Evidence Tier</b>", body_style), Paragraph(f"Tier {disease_data.get('evidence_tier', 'A')}", body_style)],
        [Paragraph("<b>Human Taxonomy</b>", body_style), Paragraph(str(ont.get("human_taxonomy")), body_style), Paragraph("<b>Mouse Taxonomy</b>", body_style), Paragraph(str(ont.get("mouse_taxonomy")), body_style)],
        [Paragraph("<b>Independent Studies</b>", body_style), Paragraph(str(disease_data.get("studies_count", 3)), body_style), Paragraph("<b>Sample Size</b>", body_style), Paragraph(f"{disease_data.get('sample_size', 24)} samples", body_style)]
    ]
    meta_table = Table(meta_table_data, colWidths=[120, 150, 120, 150])
    meta_table.setStyle(TableStyle([('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#F7FAFC')), ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')), ('PADDING', (0,0), (-1,-1), 5)]))
    story.append(meta_table)
    story.append(Spacer(1, 14))

    story.append(Paragraph("2. Translational Fidelity Index (TFI) Scores", section_style))
    score_table_data = [
        ["Composite TFI Score", "Signature Subscore", "Integration Subscore", "Model Flag"],
        [f"{disease_data.get('composite_tfi')}%", f"{disease_data.get('signature_subscore')}%", f"{disease_data.get('integration_subscore')}%", str(disease_data.get('flag'))]
    ]
    score_table = Table(score_table_data, colWidths=[135, 135, 135, 135])
    score_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#131B2E')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E0')),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(score_table)
    story.append(Spacer(1, 14))

    story.append(Paragraph("3. Divergence Driver Analysis", section_style))
    story.append(Paragraph(divergence_res.get("narrative", "No divergence detected."), body_style))
    story.append(Spacer(1, 12))

    story.append(Paragraph("4. Top Cross-Species Target Genes Matrix", section_style))
    gene_rows = [["Gene", "Human log2FC", "Mouse log2FC", "Cross-Species Fidelity"]]
    for g in disease_data.get("target_genes", []):
        gene_rows.append([str(g.get("gene")), str(g.get("human_log2fc")), str(g.get("mouse_log2fc")), str(g.get("fidelity"))])
    gene_table = Table(gene_rows, colWidths=[120, 140, 140, 140])
    gene_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#24304A')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(gene_table)

    doc.build(story)
    buffer.seek(0)
    return buffer.getvalue()
