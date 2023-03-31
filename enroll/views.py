from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistrationForm
from .models import Student
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
# Create your views here.
   
# This Class will add new item and show all items
class UserAddShowView(TemplateView):
    template_name = 'enroll/addandshow.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stud = Student.objects.all()
        fm = StudentRegistrationForm()
        context = {'form': fm, 'student': stud}
        return context

    def post(self, request):
        fm = StudentRegistrationForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            st = Student(name=nm, email=em, password=pwd)
            st.save()
        return HttpResponseRedirect('/')

# This Class will add new item and show all items
class UserDeleteView(RedirectView):
    url = '/'

    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        Student.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)

# This Class will update and edit
class UserUpdateView(View):
    def get(self, request, id):
        st = Student.objects.get(pk=id)
        fm = StudentRegistrationForm(instance=st)
        return render(request, 'enroll/updatestudent.html', {'form': fm})

    def post(self, request, id):
        st = Student.objects.get(pk=id)
        fm = StudentRegistrationForm(request.POST, instance=st)
        if fm.is_valid():
            fm.save()
            # return render(request, 'enroll/updatestudent.html', {'form': fm})
            return HttpResponseRedirect('/')     


    