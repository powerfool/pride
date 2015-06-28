from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response


# Create your views here.
def home(request):
    if request.method == 'POST':
        print "now"
        # import ipdb;ipdb.set_trace();
        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        # handle_uploaded_file(request.FILES['file'])
        # return HttpResponseRedirect('/success/url/')
    else:
        # form = UploadFileForm()
        print "now"
    return render_to_response('pride/home.html', {})


#     return render(request, 'pride/home.html', {})


# # Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file
