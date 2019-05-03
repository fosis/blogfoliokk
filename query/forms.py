from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Column, Row

from .models import Blog, Entry, Author

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'tagline']
        labels = {'name': 'Blog name', 'tagline': 'Thematic tags'}
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
                'Fill fields below to add new blog:',
                'name',
                'tagline',
            css_class='form-group col-md-10 mb-0'),
        css_class='pt-1'),        
        Column(
            FormActions(
                Submit('submit', 'Add new blog', css_class='button white'),
            css_class='form-group col-md-10 mb-1'),
        css_class='pt-2'),
        )
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['headline', 'body_text']
        labels = {'headline': 'Entry title', 'body_text': 'Entry text'}
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
                    Submit('submit', 'Add new entry', css_class='button white'),
                css_class='form-group col-md-10 mb-1'),
            css_class='pt-2'),
            )

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['nickname', 'email']
        labels = {'nickname': 'Nickname', 'email': 'Contact information - email',}
        widgets = {'nickname': forms.Textarea(attrs={'cols': 50, 'rows': 1, 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'rows': 1,})}
            
    def __init__(self, *args, **kwargs):
        super(AuthorForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-AuthorForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        
        self.helper.layout = Layout(
            Column(Fieldset(
                'Fill fields below to add new artistic nickname and contact information:',
                'nickname',
                'email',
                ),
                css_class='form-group col-md-10 mb-0'),
            Column(
                FormActions(
                    Submit('submit', 'Add new author', css_class='button white'),
                css_class='form-group col-md-10 mb-1'),
            css_class='pt-2'),
            )
                

def check_form_edit_or_new(form_type, form):
    """Checks if displayed form is for new entry or edited one."""
    if form_type != 'new':        
        edit = Fieldset('Change below entry:', 
                        'headline',
                        'body_text',
                        css_class='form-group col-md-10 mb-0')
        btn = Submit('submit', 'Save changes', css_class='button white')
        return (edit, btn)
    else:        
        new = Fieldset('Fill fields below to add new entry:', 
                       'headline',
                       'body_text',
                       css_class='form-group col-md-10 mb-0')
        return new

def check_form_blog_edit_or_new(form_type, form):
    """Checks if displayed form is for new blog or edited one."""
    if form_type != 'new':        
        edit = Fieldset('Change blog data:', 
                        'name',
                        'tagline',
                        css_class='form-group col-md-10 mb-0')
        btn = Submit('submit', 'Save changes', css_class='button white')
        return (edit, btn)
    else:        
        new = Fieldset('Fill fields below to add new blog:', 
                       'name',
                       'tagline',
                       css_class='form-group col-md-10 mb-0')
        return new
