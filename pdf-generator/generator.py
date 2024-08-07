from fpdf import FPDF

project = input("Insert the project description: ")
estimate_hours = input("Insert the estimated hours: ")
hourly_rate = input("Insert the hourly rate: ")
deadline = input("Insert the estimate deadline: ")

total_estimate = int(estimate_hours) * int(hourly_rate)


pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial")

pdf.image("template.png", x=0, y=0)

pdf.text(115, 145, project)
pdf.text(115, 160, estimate_hours)
pdf.text(115, 175, hourly_rate)
pdf.text(115, 190, deadline)
pdf.text(115, 205, str(total_estimate))

pdf.output("Project_Budget.pdf")
print("PDF created successfully!")