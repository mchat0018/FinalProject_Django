from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
    )
from django.views.generic.edit import FormView
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
        ctg=get_object_or_404(Categories,id=self.kwargs.get('id'))
        return Blog.objects.filter(field_tag=ctg).all()

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['popular']=Blog.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:4] 
        context['categories']=Categories.objects.all()
        return context

 
def blogDetail(request,pk):
    if request.method=='POST':
        form=CommentForm(request.POST)
        blg=get_object_or_404(Blog, id=pk)
        form.instance.blog=blg
         
        if form.is_valid():
            form.save()
            messages.success(request,f'Your comment has been posted')
            return reverse('blog_detail',kwargs={'pk':pk})
    
    else:
        form=CommentForm()
        blg=get_object_or_404(Blog, id=pk)

    context={
        'form': form,
        'post': blg,
        'comments':Comment.objects.filter(blog=blg).all(),
        'popular': Blog.objects.annotate(comment_count=Count('comment')).order_by('-comment_count')[:4],
        'categories': Categories.objects.all()
    }    

    return render(request,'blog/blog_detail.html',context)
    
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

















    



