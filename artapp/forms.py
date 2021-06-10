from django import forms
from . models import Profile, Comments, Post



class PostImagesForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'date',]


class PostComments(forms.ModelForm):
    class Meta: 
        model = Comments
        exclude = ['image','posted','user']
        
class PostProfile(forms.ModelForm):
    class Meta:
        models = Profile
        exclude = ['user',]
        
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_picture', 'bio']
        
        
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')                                                                                    
