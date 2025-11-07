from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# 🏠 الصفحة الرئيسية
def home(request):
    return render(request, 'home.html')


# 🧍‍♀️ إنشاء حساب جديد
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # التحقق من تطابق كلمتي المرور
        if password1 != password2:
            messages.error(request, "كلمتا المرور غير متطابقتين ❌")
            return redirect('register')

        # التحقق من أن المستخدم غير موجود مسبقًا
        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم موجود مسبقًا ⚠️")
            return redirect('register')

        # إنشاء المستخدم الجديد
        user = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "تم إنشاء الحساب بنجاح ✅ يمكنك تسجيل الدخول الآن.")
        return redirect('login')

    return render(request, 'core-templates/register.html')


# 🔐 تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"مرحبًا {user.username} 👋 تم تسجيل الدخول بنجاح.")
            return redirect('home')
        else:
            messages.error(request, "بيانات الدخول غير صحيحة ❌")

    return render(request, 'core-templates/login.html')


# 🚪 تسجيل الخروج (اختياري)
def logout_view(request):
    logout(request)
    messages.info(request, "تم تسجيل الخروج بنجاح 👋")
    return redirect('login')
