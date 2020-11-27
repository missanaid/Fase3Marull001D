from django import forms

from . models import Galeria, Anime


class AnimeForm(forms.ModelForm):
    nombre_anime = forms.CharField(label='Nombre Anime', max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    episodios = forms.IntegerField(label='Episodios', widget=forms.NumberInput(
        attrs={
            'class': 'form-control'
        }
    ))
    sinopsis = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))

    class Meta:
        model = Anime
        fields = ('nombre_anime', 'episodios', 'sinopsis')


class GaleriaForm(forms.ModelForm):
    nombre_anime = forms.CharField(label='Nombre Anime', max_length=200, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ))
    descripcion = forms.CharField(label='Descripción', max_length=1000, widget=forms.Textarea(
        attrs={
            'class': 'form-control'
        }
    ))
    imagen = forms.ImageField(label='Imagen',
                              widget=forms.ClearableFileInput(
                                  attrs={
                                      'class': 'form-control'
                                  }
                              ))

    class Meta:
        model = Galeria
        fields = ('nombre_anime', 'descripcion', 'imagen')
        widgets = {'id': forms.HiddenInput()}
