# Dennis Ivy
from django.shortcuts import render
from io import BytesIO
from django.http import  HttpResponse
from django.template.loader import get_template
from django.views import View

from xhtml2pdf import pisa


def dod(request):
    return render(request, 'documents/bed.html')


#  pdf
def render_to_pdf(template_src, context_dict=None):
    if context_dict is None:
        context_dict = {}
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='documents/pdf_view.html')
    return None

data = {
    "company": "Andrii V.S",
    "address": "123 Street name",
    "city": "Kiyv",
    "zipcode": "9988773",

    "phone": "+38979988773",
    "email": "goal@gmail.com",
    "website": "www.goal.com",
}

# Opens up page as PDF
class ViewPDF(View):
    def get(self, request, *args, **kwargs):

        pdf = render_to_pdf('documents/pdf_template.html', data)
        return HttpResponse(pdf, content_type='documents/pdf_view.html')


# Automaticly downloads to PDF file
class DownloadPDF(View):
    def get(self, request, *args, **kwargs):

        pdf = render_to_pdf('documents/pdf_template.html', data)

        response = HttpResponse(pdf, content_type='documents/pdf_view.html')
        filename = "Invoice_%s.pdf" %("12341231")
        content = "attachement; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response


def index(request):
    context = {}
    return render(request, 'documents/index.html', context)