# File Name: PDFUtilities.py
# Student Name: Nate Hoang, Andrew Rozsits, Ray Happel
# email:  hoangnbd@mail.uc.edu, rozsitaj@mailk.uc.edu, happelrc@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   3/26
# Course #/Section:   4010-001
# Semester/Year:   Spring 25
# Brief Description of the assignment:  Using github and working as a group to produce an image and a cool visual design

# Brief Description of what this module does. This module links our python to data sets to produce visuals
# Citations: Chatgpt, https://www.w3schools.com/, gemini

# Anything else that's relevant:

import reportlab.pdfgen.canvas as canvas
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import os

class PDFUtilities:
    """
        Create a PDF with some benchmark questions
    """
    def __init__(self):
        __file = ""
        
    def create_question_PDF(self, title, benchmark_name, questions):
        """
        Create a PDF with some benchmark questions
        @param title String: The title that will appear in the PDF        
        @param benchmark_name String: The folder in dataPackage where the PDF file should be saved
        @questions list of dictionaries: The questions to include in the PDF
        """
        def create_paragraph(text):
            return Paragraph(text, styles["Normal"])

        # If the path does not exist, build it
        path = "./dataPackage/" + benchmark_name + "/"
        if not os.path.exists(path):
            os.makedirs(path)
        path = "./dataPackage/" + benchmark_name + "/results/"
        if not os.path.exists(path):
            os.makedirs(path)
        doc = SimpleDocTemplate(path + benchmark_name + "_questions.pdf")
        styles = getSampleStyleSheet()
        """
        data = [
            ["Question ID", "Question"],
            ["Row 1, Cell 1 (long text)", "Row 1, Cell 2"],
            ["Row 2, Cell 1", "Row 2, Cell 2 (long text)"],
            ["Row 3, Cell 1", "Row 3, Cell 2"],
            ["Row 4, Cell 1 (long text)", "Row 4, Cell 2 (long text)"],
        ]
        """
        if title != None and len(title.strip()) > 0:
            row_idx = 1 # We are zero-based and we skip the title row
            data = [[" ", title]]   # List of lists. Each sublist is a row with 2 columns. Init the first row to the title
        else:
            row_idx = 0
            data = []   # List of lists. Each sublist is a row with 2 columns

        table_style = [
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('FONTNAME', (0, 0), (-1, -1), styles['Normal'].fontName),
            ('FONTSIZE', (0, 0), (-1, -1), styles['Normal'].fontSize),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('INNERGRID', (0, 0), (-1, -1), 0.25, 'black'),
            ('BOX', (0, 0), (-1, -1), 0.25, 'black'),
#           ('BACKGROUND', (0,   0), (-1,   0), 'lightblue'),
        ]
        for question in questions:
            row = [question["question id"], question["prompt"]]
            data.append(row)
            letter = "A"
            for possible_answer in question["possible answers"]:
                row = [" ", letter + ": " + possible_answer]
                data.append(row)
                num = ord(letter)
                num += 1
                letter = chr(num) 
                row_style = ("BACKGROUND" , (0, row_idx), (-1, row_idx), 'lightblue')
                table_style.append(row_style), 

            row_idx += 5

        table_data = [[create_paragraph(cell) for cell in row] for row in data]

        table = Table(table_data, colWidths=[0.5*inch, 5*inch])

        table.setStyle(TableStyle(table_style))

        flowables = [table]

        doc.build(flowables)
        
    def demo(self):
        myCanvas = canvas.Canvas("output.pdf")

        # Set font and color
        myCanvas.setFont("Helvetica", 20)
        myCanvas.setFillColorRGB(0, 0, 0)

        # Draw text
        myCanvas.drawString(100, 750, "Hello, world!")

        # Save the PDF
        myCanvas.save()
        

