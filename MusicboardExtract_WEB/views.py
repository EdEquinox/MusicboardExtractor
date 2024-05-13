from django.shortcuts import render
from django.http import HttpResponse
from .forms import MyForm
from .forms import ListenLaterForm
from .forms import AlbumForm
from .forms import ReviewsForm
from apps.extractList import process_form_data
from apps.extractList import process_form_data_album
from apps.extractList import process_form_data_later
from apps.extractList import process_form_data_reviews

def home(request):
    if request.method == 'POST':        
        if 'submit' in request.POST:
            form = MyForm(request.POST)
            if form.is_valid():
                # Do something with form.cleaned_data
                url = form.cleaned_data['url']
                
                data = process_form_data(url)
                
                # Create a HttpResponse object with the CSV data and the appropriate headers
                response = HttpResponse(data, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="listMusicboard.csv"'
                response.set_cookie('fileDownload', 'true', max_age=60)  # Set cookie
                
                return response  # Return the response
        elif 'submit_listen' in request.POST:
            form_listen = ListenLaterForm(request.POST)
            if form_listen.is_valid():
                # Do something with form.cleaned_data
                url = form_listen.cleaned_data['url']
                
                data = process_form_data_later(url)
                
                # Create a HttpResponse object with the CSV data and the appropriate headers
                response = HttpResponse(data, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="listenLaterMusicboard.csv"'
                response.set_cookie('fileDownload', 'true', max_age=60)
                
                return response
        elif 'submit_album' in request.POST:
            form_album = AlbumForm(request.POST)
            if form_album.is_valid():
                # Do something with form.cleaned_data
                url = form_album.cleaned_data['url']
                
                data = process_form_data_album(url)
                
                # Create a HttpResponse object with the CSV data and the appropriate headers
                response = HttpResponse(data, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="albumMusicboard.csv"'
                response.set_cookie('fileDownload', 'true', max_age=60)
                
                return response
        
        elif 'submit_reviews' in request.POST:
            form_reviews = ReviewsForm(request.POST)
            if form_reviews.is_valid():
                # Do something with form.cleaned_data
                url = form_reviews.cleaned_data['url']
                
                data = process_form_data_reviews(url)
                
                # Create a HttpResponse object with the CSV data and the appropriate headers
                response = HttpResponse(data, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="reviewsMusicboard.csv"'
                response.set_cookie('fileDownload', 'true', max_age=60)
                
                return response
    else:
        form = MyForm()
        form_listen = ListenLaterForm()
        form_album = AlbumForm()
        form_reviews = ReviewsForm()
    return render(request, 'home.html', {'form': form, 'form_listen': form_listen, 'form_album': form_album, 'form_reviews': form_reviews})
