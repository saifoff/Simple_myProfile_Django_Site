from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method =='POST':
        contact = Contact()
        name = request.POST.get('name')
        last_name = request.POST.get('last_name')
        country = request.POST.get('country')
        subject = request.POST.get('subject')
        

    return render(request,'contact.html')    
def about(request):
    return render(request,'About.html')

def feedback(request):
    return render(request,'feedback.html')