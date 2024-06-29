from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from PyPDF2 import PdfMerger

def pdf_merge(request):
    if request.method == 'POST':
        pdfs = request.FILES.getlist('pdfs')
        merger = PdfMerger()
        
        for pdf in pdfs:
            merger.append(pdf)
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="merged.pdf"'
        merger.write(response)
        merger.close()
        
        return response
    
    return render(request, 'pdf_merge.html')
import pypandoc

def convert_to_pdf(request):
    if request.method == 'POST':
        file = request.FILES['file']
        output_path = 'output.pdf'
        pypandoc.convert_file(file.temporary_file_path(), 'pdf', outputfile=output_path)
        
        with open(output_path, 'rb') as f:
            response = HttpResponse(f.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="converted.pdf"'
        
        return response
    
    return render(request, 'convert_to_pdf.html')
