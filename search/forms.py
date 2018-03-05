
from django import forms


class SearchForm(forms.Form):
    search_query = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'start searching...'}),label="",max_length=100)


class ReviewForm(forms.Form):
	review = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Write your review'}),label="",max_length=500)

class SubmissionForm(forms.Form):
	title=forms.CharField(label="Course Title",max_length=500)
	content=forms.CharField(label="Syllabus Content",max_length=10000)

class ProjectSubmissionForm(forms.Form):
	first_name=forms.CharField(widget=forms.Textarea(attrs={'cols':'50','rows':"1",'placeholder':'To avoid showing your username'}),label="First Name",max_length=300,required=False)
	public_profile=forms.CharField(widget=forms.Textarea(attrs={'cols':'50','rows':'2','placeholder':'e.g. Linkedin,Github etc (do NOT add http or https)'}),label="Public Profile",max_length=2000,required=False)
	project_name=forms.CharField(widget=forms.Textarea(attrs={'cols':"50",'rows':"1"}),label="Project Name",max_length=200)
	project_description=forms.CharField(widget=forms.Textarea(attrs={'cols':"50",'rows':"10"}),label="Project Description",max_length=500)
	project_location=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter school/area/city','rows':"1",'cols':50}),label='Location',max_length=150)
	project_url=forms.CharField(widget=forms.Textarea(attrs={'cols':"50",'rows':"1"}),label="Project Link",max_length=500)







