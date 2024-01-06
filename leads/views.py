from django.shortcuts import render, redirect
from .models import Lead, Agent
from .forms import LeadForm
from django.contrib import messages

# FOR CLASS-BASED VIEWS
from django.views import generic
from django.shortcuts import reverse

# FOR MAIL SENDING
from django.core.mail import send_mail


class IndexView(generic.TemplateView):
    template_name = 'leads/index.html'
    
    
class LeadsPageView(generic.ListView):
    template_name = 'leads/leads.html'
    queryset = Lead.objects.all()
      
    
class LeadDetailView(generic.DetailView):
    template_name = 'leads/lead-detail.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"
    
    
class LeadCreateView(generic.CreateView):
    template_name = 'leads/create-lead.html'
    form_class = LeadForm
    
    def get_success_url(self):
        return reverse("leads:leads")
    
    def form_valid(self, form):
        # TODO SEND EMAIL
        
        send_mail(
            subject= "New Lead created",
            message= "This is a notification mail that a new lead has been added to the PRIME CRM, Please login and check it out",
            from_email="mail@primecrm.com",
            recipient_list= ["user@primecrm.com"]
        )
        
        return super(LeadCreateView, self).form_valid(form)
    

class LeadUpdateView(generic.UpdateView):
    template_name = 'leads/update-lead.html'
    form_class = LeadForm
    
    def get_success_url(self):
        return reverse("leads:leads")
    
    
class LeadDeleteView(generic.DeleteView):
    template_name = 'leads/delete-lead.html'
    queryset = Lead.objects.all()
    
    def get_success_url(self):
        return reverse("leads:leads")
    
"""
def index(request):
    context = {
        
    }
    return render(request, 'leads/index.html', context)
    

def leadPage(request):
    leads = Lead.objects.all()
    
    context = {
        'leads': leads,
    }
    return render(request, 'leads/leads.html', context)
    
def leadDetailPage(request, pk):
    lead = Lead.objects.get(id=pk)
    
    context = {
        'lead': lead,
    }
    return render(request, 'leads/lead-detail.html', context)

def createLead(request):
    form = LeadForm()
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            print('lead is good') 
            return redirect('leads:leads')
            
    context = {
        'form': form,
    }
    return render(request, 'leads/create-lead.html', context) 
    
def updateLead(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadForm(instance=lead)
    if request.method == 'POST':
        form = LeadForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Details updated successfully") 
            return redirect('leads:leads')
    
    context = {
        'lead': lead,
        'form': form,
    }
    return render(request, 'leads/update-lead.html', context)
    
def deleteLead(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect('leads:leads')
"""



    
    

    
    