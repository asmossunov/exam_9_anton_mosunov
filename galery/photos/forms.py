from django import forms

from photos.models import Photo


class PhotoForm(forms.ModelForm):
    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'name': 'body', 'rows': 5, 'cols': 21})
    )

    class Meta:
        model = Photo
        fields = ('image', 'description',)
        widgets = {
            'description': forms.Textarea(attrs={'cols': 21, 'rows': 5}),
        }
