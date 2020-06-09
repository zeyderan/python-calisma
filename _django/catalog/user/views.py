from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.

#login işlemleri
def login(request):
    if request.method == 'POST':# request metodu post ise
        username = request.POST['username'] #requesten username ve pass al
        password = request.POST['password']

        #veritabanına bakar ve kullanıcı adı şifresi uyuşursu
        #bir user nesnesi döner yoksa None döner
        user = auth.authenticate(username=username,password=password)
        if user is not None:# eğer user veritabanında varsa yanı None değilse
            auth.login(request,user)#user'a bir session ver
            print('login başarılı')
            return redirect('index')#ana sayfaya yönendir
        else:
            print('kullanıcı adı ve ya parola yanlış')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def register(request):
    # resiter e post mesajı gelirse
    if request.method == 'POST':
        # form değerlerini al
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        #şifreler eşleşiyorsa
        if password == repassword:
            #Kullanıcı adını database de arar
            #eşleşme bulursa hata verir
            #register sayfasıa geri gönderir
            if User.objects.filter(username = username).exists():
                 print('kullanıcı adı daha önce alınmış')
                 return redirect('register')
            else:#username daha önceden alınmadı ise maili kontrol eder
                if User.objects.filter(email = email).exists():
                 print('email daha önce alınmış')
                 return redirect('register')
                else:#mail de daha önceden alınmamış ise
                    # kullanıcı oluştur
                    user = User.objects.create_user(username=username,password=password,email=email)
                    user.save()#veritabanına kaydet
                    print('kullanıcı oluşturuldu')
                    return redirect('login')#login sayfasına yönlendir
        else:#parolalar eşleşmez ise
            print('parola eşleşmiyor')
            return redirect('register')
        return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    return render(request, 'user/logout.html')