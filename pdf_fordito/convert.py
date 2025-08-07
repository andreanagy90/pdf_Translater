from pdf2docx import Converter
import subprocess, os
from files import get_input
#from translate import translater

pdf_file, doc_file = get_input()
new_file = None

def pdf_to_docx():
    print("Converting..")
    cv = Converter(pdf_file)
    cv.convert(doc_file, start=0, end=None)
    cv.close()
    print("Done")
    return doc_file


def docx_to_pdf(doc_file):
    print("Coverting docx to pdf..")
    output_folder = os.path.dirname(doc_file)

    subprocess.run([
        "soffice",
        "--headless",
        "--convert-to","pdf",
        "--outdir", output_folder, doc_file
    ], check= True)

    base_name = os.path.splitext(os.path.basename(doc_file))[0]
    pdf_output = os.path.join(output_folder, base_name + ".pdf")
    print("Successfull")

    return pdf_output