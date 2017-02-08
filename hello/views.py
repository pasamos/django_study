from django.shortcuts import render
from django.http import HttpResponse
from hello.models import UserInfo
import sqlite3
from django.http import JsonResponse

def hello(request):
    return HttpResponse("Hello world ! ")

def add(request):
    #http://127.0.0.1:8000/add/?a=1&b=3
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    #http://127.0.0.1:8000/add/3/3/
    c = int(a) + int(b)
    return HttpResponse(str(c))

def test(request):
    context={}
    context['text'] = 'test Page!'
    context['list'] = ["aaa", "bbb", "cc", "dd", "eeeee"]
    #context['dict'] = {}
    context['dict'] = {'name': 'cc', 'age': 24, 'sex':'male'}
    
    return render(request, 'test.html', context)

def login(request):
	if request.POST:
		#print request.user
		username=request.POST['username']
		password=request.POST['password']
		if username=='' or password=='':
			return render(request, "login.html")
		
		context={}
		context['username'] = username
		context['message'] = 'login success!:'
		request.session['username'] = username
		return render(request, "home.html", context)

	return render(request, "login.html")

def dbtables(request):
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM sqlite_master WHERE type=\'table\' ')
    values = cursor.fetchall()
    cursor.close()
    conn.close()

    context={}
    context['message'] = 'tables:'
    context['data'] = list(values)

    context['username'] = request.session.get('username',default=None)
    return render(request, "home.html", context)

def getusers(request):
	response = ""
	userlist = UserInfo.objects.all()
	print str(UserInfo.objects.all().query) #print sql
	
	user = UserInfo.objects.values_list('name') #return tuple
	print user
	print list(user) #change QuerySet to list
	
	user2 = UserInfo.objects.values_list('name', flat=True) #set flat=True then do not return tuple
	print user2
	
	user3 = UserInfo.objects.values('name', 'age') #return dict
	print user3
	
	#response2 = UserInfo.objects.filter(id=1)
	#response3 = UserInfo.objects.get(name='cc')
	#UserInfo.objects.order_by('name')[0:2]
        #UserInfo.objects.order_by("id")
	#UserInfo.objects.filter(name="cc").order_by("id")
	#UserInfo.objects.all().exists()

	for var in userlist:
		response += var.name + " "

	context={}
	context['message'] = 'user names:'+response
	context['data'] = userlist
	return render(request, "home.html", context)

def insertuser(request):
	#UserInfo.objects.create(name='cc',age=24,sex='male')
	#UserInfo.objects.get_or_create(name='cc',age=24,sex='male') #return tuple (object, True/False)
	user = UserInfo(name='cc',age=24,sex='male')
	user.save()
	
	userlist = UserInfo.objects.all()
	context={}
	context['message'] = 'insert done!'
	context['data'] = userlist
	return render(request, "home.html", context)

	
def updateuser(request):
	user = UserInfo.objects.order_by('-id').all()[:1][0]
	user.name = 'cccc'
	user.save()
	#UserInfo.objects.filter(id=1).update(name='cccc')
	
	userlist = UserInfo.objects.all()
	context={}
	context['message'] = 'update done!'
	context['data'] = userlist
	return render(request, "home.html", context)
    
def deleteuser(request):
	user = UserInfo.objects.order_by('-id').all()[:1][0]
	user.delete()
	#UserInfo.objects.filter(id=1).delete()
	#UserInfo.objects.all().delete()
	userlist = UserInfo.objects.all()
	
	context={}
	context['message'] = 'delete done!'
	context['data'] = userlist
	return render(request, "home.html", context)
    
def removesession(request):
        context={}
        username = request.session.get('username',default=None)
        if username!=None:
            del request.session['username']
            context['message'] = 'remove session done!'
        else:
            context['message'] = 'no session exists!'
            
        return render(request, "home.html", context)

def ajaxlist(request):
        a = range(100)
        return JsonResponse(a, safe=False)

    
