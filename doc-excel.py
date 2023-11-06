from docx import Document

doc = Document("C:\Users\nagan\OneDrive\Documents\py-excel\abc.doc")

dpa_data = []
is_dpa = False

for paragraph in doc.paragraphs:
    text = paragraph.text
    if is_dpa:
        dpa_data.append(text)
        is_dpa = False
    if "DPA" in text:
        is_dpa = True

import pandas as pd

df = pd.DataFrame({"DPA Data": dpa_data})

excel_file = "output.xlsx"

df.to_excel(excel_file, index=False)


