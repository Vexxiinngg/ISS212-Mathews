'''
Jmoody
ISS 212
4.2025 Wk 12 Tool Development 8 - whatthepdf1.py
Citation: Python for Networking & Security vol 3 - JOrtega
'''

from PyPDF2 import PdfReader
import os
#Prompting the user to enter the path to the PDF file
def get_metadata():
    pdf_path = input("Enter the path to the PDF file: ")

    #Checking if the provided path is valid
    if not os.path.isfile(pdf_path):
        print("Invalid file path. Please make sure the file exists.")
        return

    print("[--- Metadata : " + pdf_path)
    print("------------------------------------------------------------------------------------")

    #Opens the PDF file in a read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        pdfReader = PdfReader(pdf_file)

        #Extracts the metadata of the PDF
        info = pdfReader.metadata

        #Prints each of the metadata item from the PDF
        for metaItem in info:
            print('[+] ' + metaItem.strip('/') + ': ' + info[metaItem])

        #Prints the layout Information
        layout = pdfReader.page_layout
        print('[+] Layout: ' + str(layout))

        #Extracts the XMP metadata
        xmpinfo = pdfReader.xmp_metadata

        #Prints the specific metadata if they exist within the PDF
        if hasattr(xmpinfo, 'dc_contributor'): print('[+] Contributor:', xmpinfo.dc_contributor)
        if hasattr(xmpinfo, 'dc_identifier'): print('[+] Identifier:', xmpinfo.dc_identifier)
        if hasattr(xmpinfo, 'dc_date'): print('[+] Date:', xmpinfo.dc_date)
        if hasattr(xmpinfo, 'dc_source'): print('[+] Source:', xmpinfo.dc_source)
        if hasattr(xmpinfo, 'dc_subject'): print('[+] Subject:', xmpinfo.dc_subject)
        if hasattr(xmpinfo, 'xmp_modify_date'): print('[+] ModifyDate:', xmpinfo.xmp_modify_date)
        if hasattr(xmpinfo, 'xmp_metadata_date'): print('[+] MetadataDate:', xmpinfo.xmp_metadata_date)
        if hasattr(xmpinfo, 'xmpmm_document_id'): print('[+] DocumentId:', xmpinfo.xmpmm_document_id)
        if hasattr(xmpinfo, 'xmpmm_instance_id'): print('[+] InstanceId:', xmpinfo.xmpmm_instance_id)
        if hasattr(xmpinfo, 'pdf_keywords'): print('[+] PDF-Keywords:', xmpinfo.pdf_keywords)
        if hasattr(xmpinfo, 'pdf_pdfversion'): print('[+] PDF-Version:', xmpinfo.pdf_pdfversion)

if __name__ == "__main__":
    get_metadata()
