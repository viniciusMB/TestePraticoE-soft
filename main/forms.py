from django.forms import fields
from .models import User
from django import forms

YEARS = [x for x in range(1920, 2021)]
class CreateNewUser(forms.Form):
    nome = forms.CharField(widget = forms.HiddenInput(), max_length=15, required=False)
    sobrenome = forms.CharField(widget = forms.HiddenInput(), max_length=40, required=False)
    apelido = forms.CharField(max_length=10, required=False)
    email = forms.EmailField()
    idade = forms.IntegerField(max_value=200)
    dataNascimento = forms.DateField(label='Data de nascimento', widget=forms.SelectDateWidget(years=YEARS))
    obs = forms.CharField(label='Observação', max_length=100, required=False)
    
    
class RequiredFieldsMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        fields_required = getattr(self.Meta, 'fields_required', None)
        if fields_required:
            for key in self.fields:
                if key not in fields_required:
                    self.fields[key].required = False


class UpdateUser(RequiredFieldsMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ['nome', 'sobrenome', 'apelido', 'email', 'idade', 'dataNascimento', 'obs']
        fields_required = ['nome', 'sobrenome', 'email', 'idade', 'dataNascimento']