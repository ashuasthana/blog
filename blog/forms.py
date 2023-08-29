from django import forms
from blog.models import Comment

#Form for Send Email======================================================
class EmailSendForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    to=forms.EmailField()
    commments=forms.CharField(required=False,widget=forms.Textarea)

#Form for Post Comment====================================================== 

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment   
        fields=('name','email','body')


