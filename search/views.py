from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseRedirect
from .forms import SearchForm,SubmissionForm,ProjectSubmissionForm
import pycurl
from xml.etree import cElementTree as ET
from io import BytesIO
import mysql.connector
from oauth2client import client, crypt
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from search.models import Syllabus , Project 
import glob
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from registration.views import RegistrationView

from django.contrib.auth import get_user_model


add_query = ("INSERT INTO testing_wiki (query,garbage) VALUES (%s,%s) ")


wiki_query=""

class result1:
    name=""
    content=""
    snippet=""
    id=1

class syllabi:
	name=""
	url=""






# Create your views here.


'''def index(request):
	context={}
	template = loader.get_template('search/index.html')
	return HttpResponse(template.render(context, request))
'''
@csrf_exempt
def index(request):
	form = SearchForm()
	template = loader.get_template('search/index.html')
	context={'form': form}
	if request.method=="POST":
		idtoken=request.POST['idtoken']
		context={'form': form, 'userid':idtoken}
		return HttpResponse(template.render(context, request)) 
    #    raise crypt.AppIdentityError("Wrong hosted domain.")
	return HttpResponse(template.render(context, request))
    
    # if this is a POST request we need to process the form data
'''    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            query= form.cleaned_data['search_query']
            context={'query':query}
            # redirect to a new URL:
            template=loader.get_template('search/result.html')
            return HttpResponse(template.render(context, request))
    # if a GET (or any other method) we'll create a blank form
    else:
        
'''
    



@csrf_exempt
def login(request):
	template = loader.get_template('search/afterlogin.html')
	if request.method=='POST':
		
		token=request.POST.get('idtoken','deftok77')
		CLIENT_ID='535075582690-pianvlpvq9lm07lbv71dh5fdgklvoe8n.apps.googleusercontent.com'
		try:
			idinfo = client.verify_id_token(token, CLIENT_ID)

    # Or, if multiple clients access the backend server:
    #idinfo = client.verify_id_token(token, None)
    #if idinfo['aud'] not in [CLIENT_ID_1, CLIENT_ID_2, CLIENT_ID_3]:
    #    raise crypt.AppIdentityError("Unrecognized client.")
			if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
				raise crypt.AppIdentityError("Wrong issuer.")
			user = User.objects.create_user('luis')
			user.save()
    # If auth request is from a G Suite domain:
    #if idinfo['hd'] != GSUITE_DOMAIN_NAME:
    #    raise crypt.AppIdentityError("Wrong hosted domain.")
		except crypt.AppIdentityError:
			print("ivalid token")
		#nothing here
		# Invalid token
		user2 = User.objects.create_user('mike12')
		user2.save()
		userid=idinfo['sub']
		user3 = User.objectes.create_user(userid)
		user3.save()		
		context={'userid':userid}
		return HttpResponse(template.render(context,request))
	
		

	



def result(request):
    
    query=""
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            buffer = BytesIO()
            result_list=[]
            query=form.cleaned_data['search_query']
            query=query.replace(" ","+")
             
            c = pycurl.Curl()
            def_url="http://solr:SolrRocks@45.79.170.4:8983/solr/courselibrary/select?hl.fl=content&hl=on&indent=on&wt=xml&q="
            calling_url=def_url+query
            c.setopt(c.URL,calling_url)
            c.setopt(c.WRITEDATA, buffer)
            c.perform()
            body = buffer.getvalue()
            xmlstr = body.decode("iso-8859-1")
           
            #for fetching content and id 
            root = ET.fromstring(xmlstr)
            result=root.findall("result")
            documents=result[0].findall("doc")
            for i in documents:
                result_object=result1()
                string=i.findall("str")
                for j in string:
                    name=j.get("name")
                    if name=="content":
                        result_object.content=j.text
                        print(result_object.content)
                    if name=="id":
                        result_object.id=j.text
                        print(result_object.id)
                    if name=="file123":
                        result_object.name=j.text
                        print(result_object.name)
                result_list.append(result_object)
                
            #for fetching highlighting snippet
            result123=root.findall("lst")
            for k in result123:
                highlight_element=k.get("name")
                if highlight_element=="highlighting":
                    list_unhigh=k.findall("lst")
                    for l in list_unhigh:
                        for obj in result_list:
                            if obj.id==l.get("name"):
                                
                                attr=l.findall("arr")
                                
                                for m in attr:
                                    highlighting_strelement=m.findall("str")
                                    for n in highlighting_strelement:
                                        obj.snippet=n.text
                                        (obj.snippet)
            
            display_list=[]
            for w in result_list:
                w.id=w.id
                w.id=w.id.replace("/var/www/coursewiki/search/media/"," ")
                w.id=w.id.strip(" ")
                w.id=w.id.strip(".txt")
                #w.id=w.id.replace(" ","%20")
                
                display_list.append(w)
            query=query.replace("+"," ")    
            context={'query_result':display_list,
                     'url_called':calling_url,'query':query}
            # redirect to a new URL:
            template=loader.get_template('search/result.html')
            return HttpResponse(template.render(context, request))
    # if a -GET- (or any other method) we'll create a blank form
    else:
        form = SearchForm()
        template = loader.get_template('search/index.html')
        context={'form': form}
    return HttpResponseRedirect('/search')
    #return HttpResponse(template.render(context, request))
    

def show_syllabus(request,syllabus_name):
	if (request.method=="GET"):
		
		temp_syllabus_name=syllabus_name
		syllabus_obj=Syllabus.objects.get(syllabus_name=temp_syllabus_name+'.txt')
		temp_syllabus_pk=syllabus_obj.pk
		context={'temp_syllabus_name':temp_syllabus_name,'temp_syllabus_pk':temp_syllabus_pk,'syllabus_obj':syllabus_obj}
		template=loader.get_template('search/syllabus_template.html')
		return HttpResponse(template.render(context,request))
	if (request.method=="POST"):

                temp_syllabus_name=syllabus_name
                syllabus_obj=Syllabus.objects.get(syllabus_name=temp_syllabus_name+'.txt')
                temp_syllabus_pk=syllabus_obj.pk
                context={'temp_syllabus_name':temp_syllabus_name,'temp_syllabus_pk':temp_syllabus_pk,'syllabus_obj':syllabus_obj}
                template=loader.get_template('search/syllabus_template.html')
                return HttpResponse(template.render(context,request))  

def all_content(request):
	all_syllabi_tostrip=glob.glob('/var/www/coursewiki/search/media/*.txt')
	all_syllabi=[]
	for item in all_syllabi_tostrip:
		syllabi_obj=syllabi()
	
		item=item.replace('/var/www/coursewiki/search/media/',' ')
		item=item.strip(' ')
		item=item.replace(' ','%20')
		syllabi_obj.url=item.strip('.txt')
		syllabi_obj.name=syllabi_obj.url.replace('%20',' ')
		all_syllabi.append(syllabi_obj)
	context={'all_syllabi':all_syllabi}
	template=loader.get_template('search/all_content_list.html')
	return HttpResponse(template.render(context,request))




def syllabus_submission(request):
	if request.method=='POST':
		form1=SubmissionForm(request.POST)
		context={}
		template=loader.get_template('search/thankyou.html')
		if form1.is_valid():
			title=form1.cleaned_data['title']+'.txt'
			content=form1.cleaned_data['content']
			path="submission_files/"+title
			textfile=open(path,"w")
			textfile.writelines(content)
			textfile.close()
			return HttpResponse(template.render(context,request))
		

			
			
			
	if request.method=="GET":
		form=SubmissionForm()
		context={"form":form}
		template=loader.get_template('search/syllabus_submission.html')
		return HttpResponse(template.render(context,request))

def project_board(request):
	if request.method=="GET":
		
		projectlist=Project.objects.all()
		paginator = Paginator(projectlist,10)#show 10 items per page
		page=request.GET.get('page')
		if page is None:
			page=1
		
		projects=paginator.page(page)
		context={"projects":projects}
		template=loader.get_template('search/projectboard.html')
		return HttpResponse(template.render(context,request))
	
					

@login_required			
def project_submission(request):
	if request.method=="GET":
		form=ProjectSubmissionForm()
		context={"form":form}
		template=loader.get_template('search/submitproject.html')
		return HttpResponse(template.render(context,request))
	if request.method=="POST":
		form=ProjectSubmissionForm(request.POST)
		context={}
		template=loader.get_template('search/thankyou.html')
		if form.is_valid():
			project_object=Project()
			project_object.user_id_id=request.user.id
			project_object.project_name=form.cleaned_data['project_name']
			project_object.project_description=form.cleaned_data['project_description']
			project_object.project_url=form.cleaned_data['project_url']
			project_object.project_location=form.cleaned_data['project_location']
			project_object.public_profile=form.cleaned_data['public_profile']
			project_object.first_name=form.cleaned_data['first_name']
			project_object.save()
			return HttpResponse(template.render(context,request))




