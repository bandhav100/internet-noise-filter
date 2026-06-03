from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import date

pdf = SimpleDocTemplate(
    "outputs/trend_report.pdf"
)

styles = getSampleStyleSheet()

elements = []

title = Paragraph(
    "Trend Intelligence Report",
    styles["Title"]
)

elements.append(title)

elements.append(
    Spacer(1, 12)
)

today = Paragraph(
    f"Date: {date.today()}",
    styles["Normal"]
)

elements.append(today)

elements.append(
    Spacer(1, 12)
)

with open(
    "outputs/report.txt",
    "r"
) as file:

    report = file.read()

for line in report.split("\n"):

    elements.append(
        Paragraph(
            line,
            styles["Normal"]
        )
    )

pdf.build(
    elements
)

print(
    "PDF report generated successfully!"
)
