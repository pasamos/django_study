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
	if request.method == 'POST':
	    #print request.user
	    username=request.POST['username']
	    password=request.POST['password']
	    if username=='' or password=='':
		    return render(request, "login.html", {"message":"input username and password!"})

            userinfo = UserInfo.objects.filter(name=username).values('name', 'password')
            if list(userinfo)!=[]:
                correctPassword=list(userinfo)[0]['password']
                if correctPassword==password:
                    context={}
                    context['username'] = username
                    context['message'] = 'login success!:'
                    request.session['username'] = username
                    return render(request, "home.html", context)
                else:
                    return render(request, "login.html",{"message":"wrong password!"})
            else:
                return render(request, "login.html",{"message":"wrong username!"})

        if request.method == 'GET':
            userSession = request.session.get('username',default=None)
            if userSession!=None:
                context={}
                context['username'] = userSession
                context['message'] = 'login success!:'
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
	userlist = UserInfo.objects.all() #return QuerySet
	print ' '
        print '-------------objects.all()-------------'
	print userlist
	print '-------------QuerySet to list-------------'
	print list(userlist) #change QuerySet to list
	print '-------------sql-------------'
	print str(UserInfo.objects.all().query) #print sql
	
	user = UserInfo.objects.values_list('name') #return QuerySet[tuple]
        print '-------------objects.values_list-------------'
	print user
	user2 = UserInfo.objects.values_list('name', flat=True) #set flat=True then do not return tuple
        print '-------------objects.values_list flat true-------------'
	print user2
	user3 = UserInfo.objects.values('name', 'password') #return QuerySet[dict]
        print '-------------objects.values-------------'
	print user3
        #user4 = UserInfo.objects.get(name='cc') #return object;if not exists then raise exception
        #print '-------------objects.get-------------'
	#print user4
        #user5 = UserInfo.objects.filter(name='cc') #return QuerySet
        #print '-------------objects.filter-------------'
	#print user5

        #UserInfo.objects.order_by("id")
	#UserInfo.objects.order_by("id")[0:2]
	#UserInfo.objects.order_by("-id").all()[:1][0]
	#UserInfo.objects.filter(name="cc").order_by("id")
	#UserInfo.objects.all().exists()

	for var in userlist:
		response += var.name + "-" + var.password + " " 

	context={}
	context['message'] = 'users:'+response
	context['data'] = userlist
	return render(request, "home.html", context)

def insertuser(request):
        if request.POST:
            username=request.POST['username']
            age=request.POST['age']
            sex=request.POST['sex']
	    password=request.POST['password']

	    context={}
            if username=='' or password=='':
                context['message'] = 'please input username and password!'
		return render(request, "home.html", context)

            if UserInfo.objects.filter(name=username).exists():
                context['message'] = 'failed: name exists!'
                return render(request, "home.html", context)
	        
            #UserInfo.objects.create(name=username, age=age, sex=sex, password=password)

            #result = UserInfo.objects.get_or_create(name=username, age=age, sex=sex, password=password)
            #return tuple (object, True/False)
            #print '-------------insert result-------------'
            #print result
            
            user = UserInfo(name=username, age=age, sex=sex, password=password)
            user.save()

            context['message'] = 'insert done!'

            userlist = UserInfo.objects.all()
            context['data'] = userlist
            return render(request, "home.html", context)
        
def updateuser(request):
    if request.POST:
        updatename=request.POST['updatename']
        context={}
        if updatename == None or updatename == '':
            context['message'] = 'please input update name!'
            return render(request, "home.html", context)

        age=request.POST['newage']
        sex=request.POST['newsex']
	password=request.POST['newpassword']

        #UserInfo.objects.filter(name=updatename).update(age='20')
	
        if UserInfo.objects.filter(name=updatename).exists():
            user = UserInfo.objects.filter(name=updatename)
            for item in user:
                item.age = age
                item.sex = sex
                item.password = password
                item.save()
	
            userlist = UserInfo.objects.all()
            context={}
            context['message'] = 'update done!'
            context['data'] = userlist
            return render(request, "home.html", context)
        else:
            context['message'] = 'failed: name not exists!'
            return render(request, "home.html", context)
            
def deleteuser(request):
    if request.POST:
        deletename=request.POST['deletename']
        context={}
        
        if deletename == None or deletename == '':
            context['message'] = 'please input delete name!'
            return render(request, "home.html", context)
        
        #user = UserInfo.objects.order_by('-id').all()[:1][0]
        #UserInfo.objects.filter(name=deletename).delete()
        #UserInfo.objects.all().delete()
        if UserInfo.objects.filter(name=deletename).exists():
            user = UserInfo.objects.filter(name=deletename)
            user.delete()

            userlist = UserInfo.objects.all()
            context['message'] = 'delete done!'
            context['data'] = userlist
            return render(request, "home.html", context)
        else:
            context['message'] = 'failed: name not exists!'
            return render(request, "home.html", context)

            
def removesession(request):
        context={}
        username = request.session.get('username',default=None)
        if username!=None:
            del request.session['username']
            context['message'] = 'remove session done!'
        else:
            context['message'] = 'failed: no session exists!'
            
        return render(request, "home.html", context)

def ajaxlist(request):
        userlist = UserInfo.objects.values('name', 'age', 'sex', 'loginCount')
        return JsonResponse(list(userlist), safe=False)

    
