from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# 🧩 إنشاء حساب جديد
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ اسم المستخدم موجود مسبقًا.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "🎉 تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
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
            messages.success(request, f"مرحبًا {user.username} 👋")
            return redirect('home')
        else:
            messages.error(request, "❌ بيانات الدخول غير صحيحة.")

    return render(request, 'core-templates/login.html')

# 🚪 تسجيل الخروج
def logout_view(request):
    logout(request)
    messages.info(request, "تم تسجيل الخروج بنجاح.")
    return redirect('login')
