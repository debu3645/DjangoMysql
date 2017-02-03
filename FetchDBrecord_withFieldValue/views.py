from django.shortcuts import render
from django.http import HttpResponse
from Vineet24janapp.models import Myproject  # bind to sqlite db
from Vineet24janapp.models import Vineettable1, universitydb, Postxx  # bind to sqlite db
from .forms import RegForm, LoginForm, PrintForm, PostxxForm
from django.views.generic.list import ListView  # This on for CBV (Class based view)
from django.views.generic import CreateView   # for CreateView
from reportlab.pdfgen import canvas  # for reportlab
from django.core.cache import cache
def myfunc1(request, roll_num):
	return HttpResponse("Hello .. Your roll num is %s" %roll_num ) 

def myfunc2(request):
	my_hello = "hello WORLD"
	my_array = ["abc", "def", "xyz"]
	my_age = 25;
	#return HttpResponse(my1st.html)
	#newproject = Myproject(Title="Philipes", description="This is for Philipes", client="PHILIPS")
	#newproject.save()
	my_proj_list = Myproject.objects.all() #select * query
	
	return render(request, 'my1st.html', {"my_hello":my_hello,"my_array1":my_array, "my_age":my_age, "my_proj_list": my_proj_list},) 		

	
def func3(request):
	#my_hello3 = "hello WORLD"
	#my_array3 = ["aaa", "bbb", "ccc"]
	my_age = 25
	#my_proj_list3 = Vineettable1.objects.all() #select * query
	
	#return render(request, 'my2nd.html', {"my_hello":my_hello,"my_array2":my_array, "my_age":my_age, "my_proj_list1": my_proj_list1},) 	
	return render(request, 'index.html',{"my_age":my_age},) 	
# Create your views here.

def uniregister(request):
	#my_hello3 = "hello WORLD"
	#my_array3 = ["aaa", "bbb", "ccc"]
	#my_age = 25
	#my_proj_list3 = Vineettable1.objects.all() #select * query
	#if request.method == "POST":
	#	form = RegForm(request)
	#else:
	form = RegForm()
	#return render(request, 'my2nd.html', {"my_hello":my_hello,"my_array2":my_array, "my_age":my_age, "my_proj_list1": my_proj_list1},) 	
	return render(request, 'register1.html',{'form':form},) 

def saveregister(request):
	all_entries = Postxx.objects.get(id=2)
	if request.method == "POST":
		form = RegForm(request.POST)
		if form.is_valid():
			Name1 = form.cleaned_data['Name']
			Address1 = form.cleaned_data['DOB']
			Role1 = form.cleaned_data['Role']
			Mobile1 = form.cleaned_data['Mobile']
			universitysave = universitydb(Name = Name1, Address = Address1, Role = Role1, Mobile = Mobile1)
			universitysave.save()
	else:
		form = RegForm()
	#return render(request, 'my2nd.html', {"my_hello":my_hello,"my_array2":my_array, "my_age":my_age, "my_proj_list1": my_proj_list1},) 	
	return render(request, 'register1.html',{'form':form},{'all_entries':all_entries}) 

def unilogin(request):
	#my_hello3 = "hello WORLD"
	#my_array3 = ["aaa", "bbb", "ccc"]
	#my_age = 25
	#my_proj_list3 = Vineettable1.objects.all() #select * query
	#if request.method == "POST":
	#	form = RegForm(request)
	#else:
	form2 = LoginForm()
	#return render(request, 'my2nd.html', {"my_hello":my_hello,"my_array2":my_array, "my_age":my_age, "my_proj_list1": my_proj_list1},) 	
	return render(request, 'unilogin.html',{'form2':form2},) 
	
def checklogin(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data['User']
			password = form.cleaned_data['Password']
			if user== "viny123" and password=="viny123":
				form1 = RegForm()
				return render(request, 'register1.html',{'form':form1},) 
			else:
				form3 = LoginForm()
				return render(request, 'unilogin.html',{'form2':form3},)
				
	else:
		form = LoginForm()
		return render(request, 'unilogin.html',{'form2':form},) 

class cbvView(ListView):   # CBV View method
	model = universitydb
	template_name = "register2.html"

def genpdf(request):   # CBV View method
    # Create the HttpResponse object with the appropriate PDF headers.
	#form = PrintForm(request.POST)
	#abc = universitydb.objects.filter(Name='Charlie')
	#if form.is_valid():
		#Name1 = form.cleaned_data['myprint']
		#Name1 = form
	universitylist = ""
	#Name1 = form.cleaned_data['myprint']
	#if 'universitydbList' in request.session:		
	if request.session.has_key('universitydblist'):
		universitylist = request.session['universitydbList']
#for a in request.session['universitydbList']
	else:
		universitylist = "456"
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename="vinydjango1.pdf"'
    # Create the PDF object, using the response object as its "file."
	p = canvas.Canvas(response)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
	#p.drawString(100, 100, "Hello world.")
	p.drawString(100, 100, universitylist)
    # Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	return response

class pdfViews(ListView):   # CBV View method
	model = universitydb
	
	#def get_context_data(self, **kwargs):
	def get_queryset(self):
	#def dispatch(self, **kwargs):
		#print "xyzzz"
		self.request.session['universitydbList'] = "1234"
		#print "abc..."
	#unvrst = universitydb.objects.all()[:1].get()
	'''
	form10 = PrintForm(initial={
                'Name': 'Charlie',
            })
     '''
	template_name = "showpdf.html"
	#context_object_name = "form10"


'''
def pdfViews(request):
	form10 = PrintForm()
	universitydb1 = universitydb.objects.all()
	#return render(request, 'my2nd.html', {"my_hello":my_hello,"my_array2":my_array, "my_age":my_age, "my_proj_list1": my_proj_list1},) 	
	return render(request, 'showpdf.html',{'form10':form10, 'universitydb1':universitydb1},) 
'''	

class PostCreate(CreateView):
	model = Postxx
	#model = vineet24janapp_postxx
	fields = ['title']
	template_name = "crtview.html"
	#form_class = PostxxForm
	def form_valid(self, form):
		self.object = form.save()	
	success_url = '/'

def savemysql(request):
	if request.method == "POST":
		form = PostxxForm(request.POST)
		if form.is_valid():
			title1 = form.cleaned_data['title']
			save_in_mysql = Postxx(title = title1)
			save_in_mysql.save()
	else:
		form = PostxxForm()
 	
	return render(request, 'savemysql.html',{'form':form},) 

def cachetbl(request):
	entry = Postxx.objects.get(title='Malgudi Days')
	entry2 = Postxx.objects.get(id=8)
	
	#cache.set()
	if request.method == "POST":
		form = PostxxForm(request.POST)
		if form.is_valid():
			title1 = form.cleaned_data['title']
			save_in_mysql = Postxx(title = title1)
			save_in_mysql.save()
	else:
		form = PostxxForm()
 	
	return render(request, 'cache1.html',{'form':form,'entry':entry, 'entry2':entry2}) 