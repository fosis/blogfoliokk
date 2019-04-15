from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Column, Row

from .models import Blog, Entry

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'tagline']
        labels = {'name': 'Nazwa bloga', 'tagline': 'Tagi tematyczne'}
        widgets ={
            'tagline': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 2,
                    }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'rows': 2,
                    }),
                }
        
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-BlogForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
                
        self.helper.layout = Layout(            
        Column(
            Fieldset(
                'Uzupełnij poniższe pola w celu dodania nowego bloga:',
                'name',
                'tagline',
            css_class='form-group col-md-10 mb-0'),
        css_class='pt-1'),        
        Column(
            FormActions(
                Submit('submit', 'Dodaj nowy blog', css_class='button white'),
            css_class='form-group col-md-10 mb-1'),
        css_class='pt-2'),
        )
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['headline', 'body_text']
        labels = {'headline': 'Tytuł wpisu', 'body_text': 'Tekst wpisu'}
        widgets = {'body_text': forms.Textarea(attrs={'cols': 80, 'class': 'form-control'}),
            'headline': forms.TextInput(attrs={'class': 'form-control', 'rows': 2,})}
                
    def __init__(self, *args, **kwargs):
        super(EntryForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-EntryForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(            
            Column(Fieldset(''),
                    css_class='pt-1'),        
            Column(
                FormActions(
                    Submit('submit', 'Dodaj nowy wpis', css_class='button white'),
                css_class='form-group col-md-10 mb-1'),
            css_class='pt-2'),
            )


def check_form_edit_or_new(form_type, form):
    """Checks if displayed form is for new entry or edited one."""
    if form_type != 'new':        
        edit = Fieldset('Zmień poniższy wpis:', 
                        'headline',
                        'body_text',
                        css_class='form-group col-md-10 mb-0')
        btn = Submit('submit', 'Zapisz zmiany', css_class='button white')
        return (edit, btn)
    else:        
        new = Fieldset('Uzupełnij poniższe pola w celu dodania nowego nowego wpisu:', 
                       'headline',
                       'body_text',
                       css_class='form-group col-md-10 mb-0')
        return new
