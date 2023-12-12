from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from cdn_plus.models import DBTable
from django.contrib import messages
from .forms import CdnForm
from django.views import View
from django.shortcuts import render

# Create your views here.

def members(request):
    users = DBTable.objects.all().values()
    template = loader.get_template('allMembers.html')
    
    context = {
        "mymembers": users
    }
    return HttpResponse(template.render(context, request))

def inventory(request):
    users = DBTable.objects.all().values()
    template = loader.get_template('inventory_page.html')
    
    context = {
        "mymembers": users
    }
    return HttpResponse(template.render(context, request))

def show_map(request):
    # users = DBTable.objects.all().values()
    template = loader.get_template('map.html')
    
    return HttpResponse(template.render())

def multi_form(request):
    # users = DBTable.objects.all().values()
    template = loader.get_template('tab_form.html')
    
    return HttpResponse(template.render())

def dashboard(request):
    template = loader.get_template('dashboard.html')
    return HttpResponse(template.render())

def dns(request):
    users = DBTable.objects.all().values()
    template = loader.get_template('dns.html')
    
    context = {
        "mymembers": users
    }
    return HttpResponse(template.render(context, request))

def edit_item(request, firstName):
    messages.success(request, 'Item edited successfully.')
    content = '<p>dummy content</p>'
    return HttpResponse(content)

def delete_item(request, firstName):
    messages.success(request, 'Item deleted successfully.')
    content = '<p>dummy content</p>'
    return HttpResponse(content)

class DistributionView(View):
    template_name = 'distribution_form.html'

    def get(self, request, *args, **kwargs):
        form = CdnForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = CdnForm(request.POST)
        if form.is_valid():
            # Process the form data here
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # You can perform further actions here, such as saving to the database
            # For demonstration purposes, let's just print the data
            print(f"Name: {name}, Email: {email}, Message: {message}")

            messages.success(request, 'Form submitted successfully.')
            return redirect('distribution')

        return render(request, self.template_name, {'form': form})