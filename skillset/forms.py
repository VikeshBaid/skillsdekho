from django import forms
from django.contrib.auth.models import User
from skillset.models import EmployeeProfileInfo, EmployerProfileInfo

class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):
    username = forms.CharField(label = 'Username' ,max_length=50)
    first_name = forms.CharField(label = 'First Name', max_length = 50, required = True)
    last_name = forms.CharField(label = 'Last Name', max_length = 50, required = True)
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(label='Password', widget=forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label='Verify Password', widget=forms.PasswordInput(render_value=False))

    class Meta():
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password')

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Username already exists")

    def clean(self):
                if self.cleaned_data['password'] != self.cleaned_data['password1']:
                        raise forms.ValidationError("The passwords did not match.  Please try again.")
                return self.cleaned_data

class EmployeeProfileInfoForm(forms.ModelForm):
    experince = forms.CharField(label = 'Experience (in years)' ,max_length=2)
    class Meta():
        model = EmployeeProfileInfo
        exclude = ('user',)
        widgets = {
            'date_of_birth': DateInput(),
        }

class EmployerProfileInfoForm(forms.ModelForm):
    company_name = forms.CharField(label='Company Name')
    company_gst_no = forms.CharField(label='GST Number')
    company_cin = forms.CharField(label='CIN Number', required=False)
    location = forms.CharField(label='Address')
    contact_info = forms.CharField(label='Contact Number')
    # required_skill = forms.CharField(label = 'Skills Required')

    class Meta():
        model = EmployerProfileInfo
        exclude = ('user',)
