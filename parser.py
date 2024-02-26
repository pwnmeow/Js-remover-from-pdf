import PyPDF2
import sys

def remove_js(pdf_path, output_pdf_path):
    # Open the source PDF
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        writer = PyPDF2.PdfWriter()

        # Copy pages from reader to writer, removing annotations and actions
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            if '/Annots' in page:
                annotations = page['/Annots']
                for annotation in annotations:
                    if '/A' in annotation:  # Remove actions
                        del annotation['/A']
            writer.add_page(page)

        # Attempt to remove document-level JavaScript
        if '/Names' in reader.trailer['/Root']:
            names = reader.trailer['/Root']['/Names']
            if '/JavaScript' in names:
                del names['/JavaScript']

        # Write to a new PDF file
        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_js_pypdf2.py input.pdf output.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_pdf_path = sys.argv[2]
    remove_js(pdf_path, output_pdf_path)

