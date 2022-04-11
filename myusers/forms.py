
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class usersform(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
        
        
    def __init__(self, *args, **kwargs):
        super(usersform, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if name == 'complete' or field =='complete':
                continue    
            field.widget.attrs.update({'class':'form-control','placeholder':name})
            
            

            