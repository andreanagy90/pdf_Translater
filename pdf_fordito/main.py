from convert import pdf_to_docx, docx_to_pdf
from translate import translater

def main():
    docx_path = pdf_to_docx()
    translated = translater()
    pdf_path = docx_to_pdf(translated)
    print(f"Your results is here {pdf_path}")

main()