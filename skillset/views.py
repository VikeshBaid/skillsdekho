from django.shortcuts import render
from skillset.models import EmployeeProfileInfo, EmployerProfileInfo
from skillset.forms import UserForm, EmployeeProfileInfoForm, EmployerProfileInfoForm

#
# from django.db.models import Q
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'skillset/index.html')

def employee_sign_up(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        employee_profile_form = EmployeeProfileInfoForm(data=request.POST)

        if user_form.is_valid() and employee_profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = employee_profile_form.save(commit=False)
            profile.user = user

            if 'resume' in request.FILES:
                profile.resume = request.FILES['resume']

            profile.save()

            registered = True
        else:
            print(user_form.errors, employee_profile_form.errors)
    else:
        user_form = UserForm()
        employee_profile_form = EmployeeProfileInfoForm()

    return render(request, 'skillset/employee_signup.html',
                            {'user_form':user_form,
                             'employee_form':employee_profile_form,
                             'registered':registered})

def comp_sign_up(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        employer_profile_form = EmployerProfileInfoForm(request.POST)

        if user_form.is_valid() and employer_profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = employer_profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user_form.errors, employer_profile_form.errors)
    else:
        user_form = UserForm()
        employer_profile_form = EmployerProfileInfoForm()
    return render(request, 'skillset/employer_signup.html',
                            {'user_form':user_form,
                             'employer_form':employer_profile_form,
                             'registered': registered})

def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("Account Not Active")
        else:
            print("Someone tried to login and failed")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("Invalid Credentials")
    else:
        return render(request, 'skillset/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def search(request):
    search = False
    query = request.GET.get('q')
    query_list = []
    id_l=[]
    details = []
    if query:
        query_list = query.split(',')
        query_list = [q.strip() for q in query_list]
        skillset = EmployeeProfileInfo.objects.values('id','skillset')
        for q in skillset:
            id = q['id']
            skill_list = q['skillset'].split(',')
            skill_list = [e.strip() for e in skill_list]
            # print(skill_list)
            # print(query_list)
            for i in query_list:
                if i in skill_list:
                    id_l.append(q['id'])
    for q in set(id_l):
        detail = EmployeeProfileInfo.objects.filter(id=q).values('user__first_name', 'user__last_name', 'user__email', 'skillset')
        for i in detail:
            details.append(i)
    search = True

    return render(request, 'skillset/search.html', {"query_list": details, "search":search})
