import io

def generate_executive_pdf_report(pdf_df):
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib import colors

        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, rightMargin=36, leftMargin=36, topMargin=36, bottomMargin=36)
        styles = getSampleStyleSheet()
        
        story = []
        title_style = ParagraphStyle('Title', parent=styles['Heading1'], fontSize=18, textColor=colors.HexColor('#0F172A'), spaceAfter=12)
        story.append(Paragraph("🏦 Executive Churn Intelligence Briefing", title_style))
        story.append(Spacer(1, 10))
        
        body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, textColor=colors.HexColor('#334155'), spaceAfter=8)
        story.append(Paragraph(f"Summary of High-Risk Customer Analysis (Records Evaluated: {len(pdf_df)})", body_style))
        story.append(Spacer(1, 10))

        data = [["Credit Score", "Geography", "Age", "Balance ($)", "Churn Risk", "Status"]]
        for _, r in pdf_df.head(10).iterrows():
            data.append([
                str(r.get('CreditScore', 'N/A')),
                str(r.get('Geography', 'N/A')),
                str(r.get('Age', 'N/A')),
                f"{r.get('Balance', 0):,.2f}",
                f"{r.get('Churn_Probability_%', 0)}%",
                str(r.get('Risk_Status', 'N/A'))
            ])

        t = Table(data)
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1E293B')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0,0), (-1,0), 8),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
        ]))
        story.append(t)
        
        doc.build(story)
        pdf_bytes = buffer.getvalue()
        buffer.close()
        return pdf_bytes
    except Exception:
        pdf_template = (
            b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n"
            b"2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n"
            b"3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>\nendobj\n"
            b"4 0 obj\n<< /Length 120 >>\nstream\nBT\n/F1 18 Tf\n50 720 Td\n(Bank Customer Churn Intelligence Briefing) Tj\n0 -30 Td\n/F1 12 Tf\n(Executive Summary Report) Tj\nET\nendstream\nendobj\n"
            b"5 0 obj\n<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>\nendobj\n"
            b"xref\n0 6\n0000000000 65535 f \n0000000009 00000 n \n0000000058 00000 n \n0000000115 00000 n \n0000000246 00000 n \n0000000417 00000 n \ntrailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n508\n%%EOF\n"
        )
        return pdf_template
