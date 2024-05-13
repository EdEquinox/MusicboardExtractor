from django import forms

class MyForm(forms.Form):
    url = forms.CharField(
        label='',
        max_length=200, 
        widget=forms.TextInput(attrs={
            'class': 'subscribe-input',
            'placeholder': 'Enter your link',
            'type': 'url',
            'style': 'border: none'
                                      })
        )
    
class ListenLaterForm(forms.Form):
    url = forms.CharField(
        label='',
        max_length=200, 
        widget=forms.TextInput(attrs={
            'class': 'subscribe-input',
            'placeholder': 'Enter your link',
            'type': 'url',
            'style': 'border: none'
            })
        )
    
class AlbumForm(forms.Form):
    url = forms.CharField(
        label='',
        max_length=200, 
        widget=forms.TextInput(attrs={
            'class': 'subscribe-input',
            'placeholder': 'Enter your link',
            'type': 'url',
            'style': 'border: none'
            })
        )
    
class ReviewsForm(forms.Form):
    url = forms.CharField(
        label='',
        max_length=200, 
        widget=forms.TextInput(attrs={
            'class': 'subscribe-input',
            'placeholder': 'Enter your link',
            'type': 'url',
            'style': 'border: none'
            })
        )
