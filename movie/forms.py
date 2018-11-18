from django import forms

from .models import Customertable,Movietable

class adduser(forms.ModelForm):

    class Meta:
        model = Customertable
        fields = ['first_name', 'last_name','email_id','phone_no','address1','address2','city','zip_code','country']


class addfilms(forms.ModelForm):

	class Meta:
		model = Movietable
		fields = ['name','price','released_date','category']




	
