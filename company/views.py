from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from company.models import CompanyForm, AddressForm, ContactInformationForm
from django.views.generic.edit import FormView
from company.models import companyForm, addressForm, contactInformationForm, company, address
from django.views.generic import FormView, ListView

# Create your views here.
# class CompanyView(TemplateView):
#     template_name = "company/companyoverview.html"

# class CompanyFormView(FormView):
#     template_name = 'company/createCompanyProfile.html'
#     form_class = CompanyForm
#     success_url = '/'

#     def form_valid(self, form):
#         print("Hurra det virker!!!!!! jaaaaaa det gør det hurraaaa !!!!")
#         return super().form_valid(form)

def companyFormView(request):
    if request.method == 'POST':
        companyForm = CompanyForm(request.POST)
        addressForm = AddressForm(request.POST)
        contactInformationForm = ContactInformationForm(request.POST)
        if companyForm.is_valid() and addressForm.is_valid() and contactInformationForm.is_valid():
            address = addressForm.save()
            contactInfo = contactInformationForm.save()
            
            companyForm.instance.companyAddress = address
            companyForm.instance.companyContactInformation = contactInfo
            companyForm.save()

            return redirect('landingpage')
    else:
        companyForm = CompanyForm()
        addressForm = AddressForm()
        contactInformationForm = ContactInformationForm()

    return render(request, 'company/createCompanyProfile.html', {'companyForm': companyForm, 'addressForm': addressForm, 'contactInformationForm': contactInformationForm})
    def form_valid(self, form):
        print("Hurra det virker!!!!!! jaaaaaa det gør det hurraaaa !!!!")
        return super().form_valid(form)

class CompanyView(ListView):
    model = company
    template_name = "company/companyoverview.html"
