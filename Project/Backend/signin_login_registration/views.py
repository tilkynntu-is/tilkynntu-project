from django.shortcuts import render

# Create your views here.
def viewer(request):
    return render(request, 'signin/signin.html')  # Ensure the path to your template is correct

