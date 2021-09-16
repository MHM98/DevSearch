from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import project ,Review
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model=project
        fields=['title','featured_image','description','demo_link','source_link','tags'] 
        widgets={
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self,*args,**kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)

        #self.fields['title'].widget.attrs.update({'class':'input'})

        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) # it's kinda hard to undrestand, read documentations to get more infos about it
            
        

class ReviewForm(ModelForm):
    class Meta:
        model=Review
        
        fields=['value','body']

    
        lables={
            'value':'place your vote',
            'body':'Add a comment'
        }
    def __init__(self,*args,**kwargs):
        super(ReviewForm, self).__init__(*args,**kwargs)

        #self.fields['title'].widget.attrs.update({'class':'input'})

        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})