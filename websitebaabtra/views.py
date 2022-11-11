from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'websitetemplates/home.html')
def placements(request):
    return render(request,'websitetemplates/placements.html')
def blog(request):
    return render(request,'websitetemplates/blog.html')
def gallery(request):
    return render(request,'websitetemplates/gallery.html')
def enquire(request):
    return render(request,'websitetemplates/enquire.html')