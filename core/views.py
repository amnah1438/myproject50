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
        username = request.POST.get('username').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # ✅ تحقق من وجود جميع الحقول
        if not username or not email or not password or not confirm_password:
            messages.error(request, "⚠️ يرجى تعبئة جميع الحقول.")
            return redirect('register')

        # ✅ تحقق من تطابق كلمتي المرور
        if password != confirm_password:
            messages.error(request, "❌ كلمتا المرور غير متطابقتين.")
            return redirect('register')

        # ✅ تحقق من أن اسم المستخدم أو البريد الإلكتروني غير مستخدم مسبقًا
        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ اسم المستخدم موجود مسبقًا.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "⚠️ البريد الإلكتروني مستخدم مسبقًا.")
            return redirect('register')

        # ✅ إنشاء مستخدم جديد وتفعيله مباشرة
        user = User.objects.create_user(username=username, email=email, password=password)
        user.is_active = True
        user.save()

        messages.success(request, "🎉 تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.")
        return redirect('login')

    return render(request, 'core-templates/register.html')


# 🔐 تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password')

        # ✅ التحقق من أن الحقول ليست فارغة
        if not username or not password:
            messages.error(request, "⚠️ يرجى إدخال اسم المستخدم وكلمة المرور.")
            return redirect('login')

        # ✅ التحقق من صحة بيانات المستخدم
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f"مرحبًا {user.username} 👋 تم تسجيل الدخول بنجاح.")
                return redirect('home')
            else:
                messages.warning(request, "🚫 الحساب غير مفعل. يرجى التواصل مع الإدارة.")
        else:
            messages.error(request, "❌ بيانات الدخول غير صحيحة، حاول مرة أخرى.")

    return render(request, 'core-templates/login.html')


# 🚪 تسجيل الخروج
def logout_view(request):
    logout(request)
    messages.info(request, "🚪 تم تسجيل الخروج بنجاح.")
    return redirect('login')
