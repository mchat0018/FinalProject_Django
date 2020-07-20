from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
    )
from django.views.generic.edit import FormMixin
from django.contrib.auth.models import User
from .models import Blog,Comment,Categories
from .forms import CommentForm
from django.db.models import Count
from django.urls import reverse
from django.contrib import messages

# Create your views here.


class BlogHome(ListView):
    model=Blog
    context_object_name='posts'
    ordering=['-date_posted']
    #paginate_by=5

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context['newest']=Blog.objects.order_by('-date_posted')[:4]
        context['popular']= Blog.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:4] , 
        context['categories']= Categories.objects.all()
        return context

class CategoryBlogPosts(ListView):
    model=Blog
    template_name='blog/category_blog_list.html'
    context_object_name='category_posts'
    ordering=['-date_posted']

    def get_queryset(self):
        ctg=get_object_or_404(Categories,field=self.kwargs.get('field'))
        return Blog.objects.filter(field_tag=ctg).all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['popular']=Blog.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:4] 
        context['categories']=Categories.objects.all()
        return context
   
class PostDetail(FormMixin,DetailView):
    model=Blog
    template_name='blog/blog_detail.html'
    context_object_name='post'
    form_class=CommentForm

    def get_success_url(self):
        return reverse('blog_detail', kwargs={'pk': self.get_object().id})
    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['form']=CommentForm(initial={'blog':self.get_object()})
        context['comments']=Comment.objects.filter(blog=self.get_object()).all()
        context['categories']=Categories.objects.all()
        context['popular']=Blog.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:4]
        return context

    def post(self,request,*args,**kwargs):
        self.object=self.get_object()
        form=self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)

def search(request):
    query=request.GET['search']
    if len(query)>70:
        search_results=Blog.objects.none()
    else:
        title_matches = Blog.objects.filter(title__icontains=query)
        content_matches = Blog.objects.filter(content__icontains=query)
        search_results=title_matches.union(content_matches)
    
    if search_results.count() == 0:
        messages.warning(request,f'No search results found. Please refine your query')

    context={
        'query':query,
        'results':search_results,
        'popular': Blog.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:4] ,
        'categories': Categories.objects.all()
    }
    return render(request,'blog/search.html',context)

















    



