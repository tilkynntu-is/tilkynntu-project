from django.shortcuts import render
#make views here

def viewer(request):
    return render(request, 'reportviewer/viewer.html')  # Ensure the path to your template is correct

