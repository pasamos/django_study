from hello.models import UserInfo
from django.http import HttpResponse

class LoginCountMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
 
    def __call__(self, request):
        # Code to be executed for each request before the view (and later middleware) are called.
        if request.path=='/test/':
            userSession = request.session.get('username',default=None)
            if userSession==None:
                return HttpResponse('<h1>Forbidden, please login</h1>  <a href=''http://127.0.0.1:8000/''>login</a>')
            
        response = self.get_response(request)

        # Code to be executed for each request/response after the view is called.
        if request.POST and request.path=='/login/':
            username=request.POST['username']
            password=request.POST['password']

            if UserInfo.objects.filter(name=username).filter(password=password).exists():
                user = UserInfo.objects.get(name=username)
                count=user.loginCount
                print 'current count: ' + str(count)
                user.loginCount = count+1
                user.save()
                print 'count added!'
 
        return response
