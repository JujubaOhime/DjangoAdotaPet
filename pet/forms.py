from django import forms

from AdotaPet import settings
from pet.models import Pet


class PesquisaPetForm(forms.Form):
    query_string = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control border-0 bg-secondary', 'max-lenght': '100',
                                      'placeholder': 'Buscar', 'aria-describedby': 'button-addon1',
                                      'style': 'border-radius: 25px; background-color: var(--blue) !important; color: var(--white)'}, ),
        required=False
    )
    # <input type="text" name="nome" id="id_nome" class="form-control form-control-sm" maxlength="100">


class PetForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PetForm, self).__init__(*args, **kwargs)

        self.fields['preco'].min_value = 0
        self.fields['preco'].error_messages = {'required': 'Campo obrigatório.',
                                               'invalid': 'Valor inválido.',
                                               'max_digits': 'Mais de 5 dígitos no total.',
                                               'max_decimal_places': 'Mais de 2 dígitos decimais.',
                                               'max_whole_digits': 'Mais de 3 dígitos inteiros.'}
        self.fields['preco'].widget.attrs.update({
            'class': 'form-control form-control-sm',
            'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57) || event.charCode == 44'
        })

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        widgets = {'data_nascimento': forms.DateInput(attrs={'type': 'date', 'min': '1899-01-01', 'max': '2010-12-31'}),
                   'sexo': forms.Select(),
                   'categoria': forms.Select(),
                   'cep': forms.TextInput(),
                   'estado': forms.TextInput(attrs={'id': 'id_estado', 'name': 'estado', 'readonly': 'readonly'}),
                   'cidade': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'telefone': forms.TextInput(),
                   'link_instagram': forms.URLInput(),
                   'link_facebook': forms.URLInput(),
                   'descricao': forms.Textarea(),
                   'disponivel': forms.CheckboxInput(),
                   'preco': forms.NumberInput(attrs={'maxlength': '7', 'min': '0', 'max': '10000', 'step': '0.05'}),
                   }
        fields = ('nome', 'descricao', 'categoria', 'preco', 'imagem', 'raca', 'sexo',
                  'cep', 'estado', 'cidade', 'telefone',  'data_nascimento', 'link_instagram', 'link_facebook', 'disponivel', 'quantidade'
                 )

        data_nascimento = forms.DateField(
            input_formats=settings.DATE_INPUT_FORMATS
        )

        disponivel = forms.BooleanField(
            required=False
        )


class PetAjax(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PetAjax, self).__init__(*args, **kwargs)


        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        widgets = {
                   'sexo': forms.Select(),
                   'categoria': forms.Select(),
                   'cep': forms.TextInput(),
                   'estado': forms.TextInput(attrs={'id': 'id_estado', 'name': 'estado', 'readonly': 'readonly'}),
                   'cidade': forms.TextInput(attrs={'readonly': 'readonly'}),
                   'telefone': forms.TextInput(),
                   'disponivel': forms.CheckboxInput(),
                   'preco': forms.NumberInput(attrs={'maxlength': '7', 'min': '0', 'max': '10000', 'step': '0.05'}),

                   }
        fields = ('nome', 'preco', 'quantidade',
                 )

class QuantidadeForm(forms.Form):

    pet_id = forms.CharField(widget=forms.HiddenInput())

    # <input type="hidden" name="produto_id" required="" id="id_produto_id" value="xxx">

    quantidade = forms.IntegerField(
        min_value=0,
        max_value=99,
        widget=forms.TextInput(attrs={'class': 'form-control btn-light quantidade mx-auto',
                                      'style': 'text-align: center; height: 20px; background-color: unset; width: 55px; border: 1px solid #252525',
                                      'onkeypress': 'return (event.charCode >= 48 && event.charCode <= 57)'}),
        required=True
    )