from django import forms

from .models import Item


class NewItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ('category', 'name', 'description', 'price', 'image')
		widgets = {
		    'category': forms.Select(attrs={
		    	 'class': 'form-control px-6 py-2 rounded border',
                  
		    	}),
		    'name': forms.TextInput(attrs={
		    	  'class': 'form-control px-6 py-2 rounded border',
                  
		    	}),
		    'description': forms.Textarea(attrs={
		    	  'class': 'form-control px-6 py-2 rounded border',
                  
		    	}),
		    'price': forms.TextInput(attrs={
		    	  'class': 'form-control px-6 py-2 rounded border',
                  
		    	}),
		    'image': forms.FileInput(attrs={
		    	  'class': 'form-control px-6 py-2 rounded border',
                  
		    	}),
		}
		
class EditItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ( 'name', 'description', 'price', 'image', 'is_sold')
		widgets = {
		    
		    'name': forms.TextInput(attrs={
		    	  'class': 'form-control px-6 py-2 rounded border',
                  
		    	}),
		    'description': forms.Textarea(attrs={
		    	  'class': 'form-control px-6 py-2 rounded border',
                  
		    	}),
		    'price': forms.TextInput(attrs={
		    	  'class': 'form-control px-6 py-2 rounded border',
                  
		    	}),
		    'image': forms.FileInput(attrs={
		    	  'class': 'form-control px-6 py-2 rounded border',
                  
		    	}),
		}