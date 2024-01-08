from django.views.generic import TemplateView,ListView
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from . import bussiness




# Create your views here.


# this view for Home Page
class Home(ListView):
    template_name = "index.html"
    context_object_name = 'blogs'
    def get_queryset(self):
            with open('blog_details.json', encoding="utf8") as f:
                blogs = json.load(f)
            return blogs[:3]

# this view for About
class About(TemplateView):
    template_name = "about.html"

#this view for Service
class Service(ListView):
    template_name = 'service.html'
    context_object_name = 'services'
    def get_queryset(self):
        with open('service.json', encoding="utf8") as f:
            services = json.load(f)
        return services



class SerivceDetail(TemplateView):
    template_name = 'service_detail.html'

    def get(self,request,*args,**kwargs):
        id = self.kwargs.get('id')
        return bussiness.get_content(request, id, self.template_name, "service.json", 'service')

    
#BlogList for displaying all blogs
class BlogList(ListView):
    template_name = 'blog_list.html'
    context_object_name = 'blogs'
    def get_queryset(self):
        with open('blog_details.json', encoding="utf8") as f:
            blogs = json.load(f)
        return blogs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page')
        paginator = Paginator(context['blogs'],9)

        try:
            blogs = paginator.page(page)
        except PageNotAnInteger:
            blogs = paginator.page(1)
        except EmptyPage:
            blogs = paginator.page(paginator.num_pages)

        context['blogs'] = blogs
        return context

class BlogDetail(TemplateView):
    template_name = 'blog_detail.html'

    def get(self,request,*args,**kwargs):
        blog_id = self.kwargs.get('id')
        return bussiness.get_content(request, blog_id, self.template_name, "blog_details.json", 'blog')
        



class Portfolio(TemplateView):
    template_name = 'portfolio.html'

class PortfolioDetail(TemplateView):
    template_name = 'portfolio_detail.html'

    def get(self,request,*args,**kwargs):
        portfolio_id = self.kwargs.get('id')
        return bussiness.get_content(request, portfolio_id, self.template_name, "portfolio.json", 'portfolio')

class Contact(TemplateView):
    template_name = 'contact.html'

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        subject = request.POST.get('subject')
        recipient_list = [settings.EMAIL_HOST_USER, ]
        try:
            send_mail(subject, content, email, recipient_list)
            response_data = {'success': True}
            
        except Exception as e:
            response_data = {'success': False, 'error_message': str(e)}
            print("what is eroor:",response_data.error_message)
        return JsonResponse(response_data)

class Team(TemplateView):
    template_name = 'team.html'

class Industries(TemplateView):
    template_name = 'industries.html'



class IndustriesDetail(TemplateView):
    template_name = 'industries_detail.html'

    def get(self,request,*args,**kwargs):
        industries_id = self.kwargs.get('id')
        return bussiness.get_content(request, industries_id, self.template_name, "industries.json", 'industries')

class Privacy(TemplateView):
    template_name = 'privacy.html'

class Term(TemplateView):
    template_name = 'term.html'