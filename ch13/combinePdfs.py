#! python3
# combinePdfs.py - カレントディレクトリの全PDFをひとつのPDFに結合する
 
import PyPDF2, os  # ❶

# すべてのPDFファイル名を取得する
pdf_files = []
for filename in os.listdir('.'):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)  # ❷
pdf_files.sort(key=str.lower)  # ❸

pdf_writer = PyPDF2.PdfFileWriter()  # ❹

# すべてのPDFファイルをループする
for filename in pdf_files:
    pdf_file_obj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    # 先頭を除くすべてのページをループして追加する
    for page_num in range(1, pdf_reader.numPages):  # ❶
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)

# 結合したPDFをファイルに保存する
pdf_output = open('allminutes.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()

