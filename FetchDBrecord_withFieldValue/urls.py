from django.conf.urls import url
from Vineet24janapp import views
from views import PostCreate, cachetbl
from django.views.generic.list import ListView
#from Vineet24janapp import models 
from Vineet24janapp.models import universitydb,collegedb
from django.views.generic import CreateView,DetailView


#from django.views.generic import ListView # for cbv (Class based view)
urlpatterns = [
    url(r'^results/(?P<roll_num>[0-9]+)$', views.myfunc1, name='myresult'),
	url(r'^restemplate/$', views.myfunc2, name='my2ndresult'),
	url(r'^vineet1/$', views.func3, name='myviny'),
	#url(r'^universityreg/$', views.uniregister, name='unregister'),
	url(r'^savereg/$', views.saveregister, name='saveregister1'),
	url(r'^universityreg/$', views.unilogin, name='unilogin'),
	url(r'^checklogin/$', views.checklogin, name='checklogin'),
	#url(r'^cbview/$', views.cbvView.as_view()), #class based view
	url(r'^cbview/$',ListView.as_view(model=universitydb, template_name="register2.html")), ## Generic View
	url(r'^college/$',CreateView.as_view(model=collegedb, template_name="register2.html"), name="createcollege"),
	url(r'^genpdf/$', views.genpdf, name='generatepdf'),
	url(r'^listpdfview/$',ListView.as_view(model=universitydb, template_name="showpdf.html")),
	#url(r'^listpdf/$', views.pdfViews.as_view()),
	url(r'^pdfpdf/$', views.genpdf, name='pdfpdf'), ## Generic View] ## Generic View
	url(r'^mypdf/$', views.pdfViews, name='mypdf'),
	url(r'^createpost/$', PostCreate.as_view(), name='create'),  ## This one for verifying createView on Postxx
	url(r'^mysqlsv/$', views.savemysql, name='saveinmysql'),
	url(r'^cache1/$', views.cachetbl, name='cache1test')]


