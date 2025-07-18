from django.shortcuts import render
from django.http import HttpResponse
from .models import WaitlistEntry

def waitlist_form(request):
    if request.method == 'POST':
        security_needs = request.POST.getlist('securityNeeds')
        WaitlistEntry.objects.create(
            full_name=request.POST.get('fullName'),
            mobile=request.POST.get('mobile'),
            email=request.POST.get('email'),
            city=request.POST.get('city'),
            user_type=request.POST.get('userType'),
            urgency=request.POST.get('urgency'),
            security_needs=", ".join(security_needs),
            budget=request.POST.get('budget'),
            notes=request.POST.get('notes'),
            consent=bool(request.POST.get('consent'))
        )
        return HttpResponse("Thank you for joining the waitlist!")
    
    return render(request, 'survey/form.html')
