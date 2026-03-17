content = """\
{% extends 'base.html' %}

{% block title %}Sign Up - CivicCatalyst{% endblock %}

{% block content %}
<div class="min-h-screen flex">
    <!-- Left: Brand Panel -->
    <div class="hidden lg:flex lg:w-1/2 bg-gradient-to-br from-slate-900 via-blue-900 to-indigo-900 p-16 flex-col justify-between relative overflow-hidden">
        <div class="absolute inset-0 opacity-10"
            style="background-image: radial-gradient(circle at 2px 2px, white 1px, transparent 0); background-size: 32px 32px;">
        </div>
        <div class="relative">
            <div class="flex items-center space-x-3 mb-12">
                <div class="w-10 h-10 rounded-xl bg-white/10 backdrop-blur flex items-center justify-center">
                    <i data-lucide="map-pin" class="w-5 h-5 text-white"></i>
                </div>
                <span class="text-white font-black text-2xl tracking-tight">CivicCatalyst</span>
            </div>
            <h2 class="text-5xl font-black text-white leading-tight mb-6">
                Be the<br>
                <span class="text-blue-300">Change.</span>
            </h2>
            <p class="text-slate-400 text-lg leading-relaxed">
                Join thousands of citizens making their city better every day through instant reporting and transparent tracking.
            </p>
        </div>
        <div class="relative space-y-4">
            <div class="bg-white/5 backdrop-blur-sm border border-white/10 rounded-2xl p-5">
                <p class="text-slate-300 text-sm font-medium">Over <span class="text-white font-bold">2,500+</span> issues resolved this month across the city.</p>
                <div class="flex mt-3 -space-x-2">
                    <div class="w-8 h-8 rounded-full border-2 border-slate-800 bg-blue-500 flex items-center justify-center text-[10px] text-white font-bold">JD</div>
                    <div class="w-8 h-8 rounded-full border-2 border-slate-800 bg-indigo-500 flex items-center justify-center text-[10px] text-white font-bold">AS</div>
                    <div class="w-8 h-8 rounded-full border-2 border-slate-800 bg-slate-700 flex items-center justify-center text-[10px] text-white font-bold">MK</div>
                </div>
            </div>
        </div>
    </div>

    <!-- Right: Form Panel -->
    <div class="w-full lg:w-1/2 flex items-center justify-center p-8 bg-slate-50 py-12">
        <div class="w-full max-w-lg space-y-8">
            <div class="text-center lg:text-left space-y-2">
                <h1 class="text-4xl font-black text-slate-900 tracking-tight">Create Account</h1>
                <p class="text-slate-500 font-medium">Start reporting civic issues in your neighborhood.</p>
            </div>

            {% if form.errors %}
            <div class="p-4 bg-red-50 border border-red-100 rounded-2xl text-red-600 text-xs">
                <p class="font-black uppercase tracking-wider mb-2">Please fix errors:</p>
                <ul class="space-y-1">
                    {% for field, field_errors in form.errors.items %}
                    {% for error in field_errors %}
                    <li><span class="font-bold">{{ field|title }}:</span> {{ error }}</li>
                    {% endfor %}
                    {% endfor %}
                </ul>
            </div>
            {% endif %}

            <div class="bg-white rounded-3xl p-8 shadow-2xl border border-slate-100 relative overflow-hidden">
                <div class="absolute top-0 left-0 w-full h-1.5 bg-gradient-to-r from-blue-500 to-indigo-600"></div>

                <form method="post" enctype="multipart/form-data" class="space-y-5">
                    {% csrf_token %}

                    <div class="grid grid-cols-2 gap-4">
                        <div class="space-y-1.5">
                            <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 block ml-1">First Name</label>
                            <input type="text" name="first_name" placeholder="John"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-slate-800 font-bold text-sm placeholder:font-normal focus:outline-none focus:ring-4 focus:ring-blue-50 focus:border-blue-500 transition">
                        </div>
                        <div class="space-y-1.5">
                            <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 block ml-1">Last Name</label>
                            <input type="text" name="last_name" placeholder="Doe"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-slate-800 font-bold text-sm placeholder:font-normal focus:outline-none focus:ring-4 focus:ring-blue-50 focus:border-blue-500 transition">
                        </div>
                    </div>

                    <div class="space-y-1.5">
                        <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 block ml-1">Email Address</label>
                        <input type="email" name="email" placeholder="john@example.com"
                            class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-slate-800 font-bold text-sm placeholder:font-normal focus:outline-none focus:ring-4 focus:ring-blue-50 focus:border-blue-500 transition">
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div class="space-y-1.5">
                            <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 block ml-1">Mobile Number</label>
                            <input type="text" name="phone" placeholder="9876543210" required
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-slate-800 font-bold text-sm placeholder:font-normal focus:outline-none focus:ring-4 focus:ring-blue-50 focus:border-blue-500 transition">
                        </div>
                        <div class="space-y-1.5">
                            <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 block ml-1">Age</label>
                            <input type="number" name="age" placeholder="25"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-slate-800 font-bold text-sm placeholder:font-normal focus:outline-none focus:ring-4 focus:ring-blue-50 focus:border-blue-500 transition">
                        </div>
                    </div>

                    <div class="space-y-1.5">
                        <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 block ml-1">Profile Photo</label>
                        <input type="file" name="profile_photo"
                            class="w-full bg-slate-50 border border-slate-200 rounded-xl p-2 text-slate-400 text-xs focus:outline-none focus:border-blue-500 transition">
                    </div>

                    <div class="grid grid-cols-2 gap-4">
                        <div class="space-y-1.5">
                            <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 block ml-1">Password</label>
                            <input type="password" name="password1" placeholder="••••••••"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-slate-800 font-bold text-sm focus:outline-none focus:ring-4 focus:ring-blue-50 focus:border-blue-500 transition">
                        </div>
                        <div class="space-y-1.5">
                            <label class="text-[10px] font-black uppercase tracking-widest text-slate-400 block ml-1">Confirm</label>
                            <input type="password" name="password2" placeholder="••••••••"
                                class="w-full bg-slate-50 border border-slate-200 rounded-xl p-3.5 text-slate-800 font-bold text-sm focus:outline-none focus:ring-4 focus:ring-blue-50 focus:border-blue-500 transition">
                        </div>
                    </div>

                    <button type="submit"
                        class="w-full bg-slate-900 text-white font-black py-4 rounded-2xl hover:bg-slate-800 transition shadow-2xl shadow-slate-200 transform hover:-translate-y-1 active:scale-95 text-base flex items-center justify-center gap-2 mt-4">
                        <i data-lucide="user-plus" class="w-5 h-5"></i> Start Reporting
                    </button>
                </form>
            </div>

            <p class="text-center text-slate-500 text-sm">
                Already have an account? <a href="{% url 'login' %}" class="text-blue-600 font-black hover:underline">Log in \u2192</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}
"""

with open('templates/users/signup.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("signup.html fixed successfully.")
