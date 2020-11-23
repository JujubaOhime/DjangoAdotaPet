
from categoria.models import Categoria
from django import forms

class CategoriaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CategoriaForm, self).__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Categoria
        ordering = ('nome', )
        fields = ('nome', )

class PesquisaCategoriaForm(forms.Form):
    query_string = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control border-0 bg-secondary', 'max-lenght': '100',
                                      'placeholder': 'Buscar', 'aria-describedby': 'button-addon1',
                                      'style': 'border-radius: 25px; background-color: var(--blue) !important; color: var(--white)'}, ),
        required=False
    )
