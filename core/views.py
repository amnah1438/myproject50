from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# 🏠 الصفحة الرئيسية
def home(request):
    return render(request, 'home.html')

# 🧩 إنشاء حساب جديد
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # التحقق من أن اسم المستخدم غير مستخدم مسبقًا
        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ اسم المستخدم موجود مسبقًا.")
        else:
            # إنشاء مستخدم جديد
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, "🎉 تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
            return redirect('login')  # إعادة التوجيه لصفحة تسجيل الدخول بعد النجاح

    # عرض صفحة إنشاء الحساب
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
            return redirect('home')  # التوجيه إلى الصفحة الرئيسية بعد تسجيل الدخول
        else:
            messages.error(request, "❌ بيانات الدخول غير صحيحة، حاول مرة أخرى.")

    # عرض صفحة تسجيل الدخول
    return render(request, 'core-templates/login.html')

# 🚪 تسجيل الخروج
def logout_view(request):
    logout(request)
    messages.info(request, "🚪 تم تسجيل الخروج بنجاح.")
    return redirect('login')
