from django.shortcuts import render
from django.http import HttpResponse
from .forms import ArtistSubmission

# Create your views here.
def genres(request):
    return HttpResponse("Placeholder")

def submit(request):
    if request.method == 'POST':
        form = ArtistSubmission(request.POST)
        if form.is_valid():
            artist = form.save()
            return HttpResponse("Successful Submission")
    
    else:
        form = ArtistSubmission()
    
    return render(request, 'submission.html', {'form': form})

        
