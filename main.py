import PyPDF2
import os

def protect_pdf(input_path, output_path, password):
    with open(input_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        pdf_writer = PyPDF2.PdfWriter()
        
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])
            
        pdf_writer.encrypt(password)
        
        output_folder = os.path.dirname(output_path)
        os.makedirs(output_folder, exist_ok=True)
        
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_path = "pdf-file/logo.pdf"
    output_pdf_path = "output/protected_logo.pdf"
    password = "123456789"
    
    protect_pdf(input_pdf_path, output_pdf_path, password)
    print(f"PDF file protected and saved to: {output_pdf_path}")