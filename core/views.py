from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


# 🏠 الصفحة الرئيسية
@csrf_protect
def home(request):
    """عرض الصفحة الرئيسية بعد تسجيل الدخول"""
    return render(request, 'home.html')


# 🧩 إنشاء حساب جديد + دخول مباشر بعد التسجيل
@csrf_protect
def register_view(request):
    """
    إنشاء حساب مستخدم جديد مع التحقق من الحقول والأمان.
    بعد التسجيل يتم تسجيل الدخول تلقائيًا وتحويل المستخدم للصفحة الرئيسية.
    """
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        # ✅ التحقق من تعبئة جميع الحقول
        if not all([username, email, password1, password2]):
            messages.error(request, "⚠️ يرجى تعبئة جميع الحقول المطلوبة.")
            return redirect('core:register')

        # ✅ التحقق من تطابق كلمتي المرور
        if password1 != password2:
            messages.error(request, "❌ كلمتا المرور غير متطابقتان.")
            return redirect('core:register')

        # ✅ التحقق من أن البريد الإلكتروني صالح (تنسيق)
        if "@" not in email or "." not in email.split("@")[-1]:
            messages.error(request, "📧 يرجى إدخال بريد إلكتروني صحيح.")
            return redirect('core:register')

        # ✅ التحقق من عدم وجود اسم المستخدم أو البريد مسبقًا
        if User.objects.filter(username=username).exists():
            messages.error(request, "⚠️ اسم المستخدم مستخدم مسبقًا.")
            return redirect('core:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "⚠️ البريد الإلكتروني مستخدم مسبقًا.")
            return redirect('core:register')

        # ✅ إنشاء المستخدم الجديد وتفعيله
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.is_active = True
        user.save()

        # ✅ تسجيل الدخول التلقائي بعد التسجيل
        login(request, user)
        messages.success(request, f"🎉 تم إنشاء الحساب بنجاح! مرحبًا بك يا {user.username} 👋")
        return redirect('core:home')

    # عرض صفحة التسجيل
    return render(request, 'core-templates/register.html')


# 🔐 تسجيل الدخول
@csrf_protect
def login_view(request):
    """
    تسجيل دخول المستخدم بعد التحقق من البيانات.
    """
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')

        # ✅ التحقق من إدخال البيانات
        if not username or not password:
            messages.error(request, "⚠️ يرجى إدخال اسم المستخدم وكلمة المرور.")
            return redirect('core:login')

        # ✅ مصادقة المستخدم
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f"👋 أهلاً {user.username}! تم تسجيل الدخول بنجاح.")
                return redirect('core:home')
            else:
                messages.warning(request, "🚫 الحساب غير مفعل. يرجى التواصل مع الإدارة.")
                return redirect('core:login')
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة.")
            return redirect('core:login')

    # عرض صفحة تسجيل الدخول
    return render(request, 'core-templates/login.html')


# 🚪 تسجيل الخروج
def logout_view(request):
    """
    تسجيل خروج المستخدم وإعادة توجيهه لصفحة تسجيل الدخول.
    """
    logout(request)
    messages.success(request, "🚪 تم تسجيل الخروج بنجاح. نراك قريبًا 👋")
    return redirect('core:login')
