from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404
from .models import DataBase
from django.views.generic import ListView, DetailView
from django.views import View
from .forms import CommentForm
from .models import Comment
# Create your views here.

class starting_page(ListView):
    template_name= "Blog_App/starting_page.html"
    model = DataBase
    ordering =["address"]
    def get_queryset(self):
        query = super().get_queryset()
        data = query[:]
        return data
   
    

def posts(request):
    return render(request,"Blog_App/All_Posts.html")



# class post_details(DetailView):
#     template_name = "Blog_App/post-details.html"
#     model = DataBase
#     context_object_name= "post"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["commentform"] = CommentForm()
#         return context
    
class post_details(View):

    def get(self, request, slug):
        post = DataBase.objects.get(slug=slug)
        return render(request, "Blog_App/post-details.html", {
            "post": post,
            "commentform": CommentForm(),
            #"comment": post.comment.all()
            "comment": post.comment.all()

        })

    def post(self, request, slug):  # Include slug here
        post = DataBase.objects.get(slug=slug)
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            # Save the comment but associate it with the correct post
            comment = comment_form.save(commit=False)
            comment.post = post  # Assuming your Comment model has a post ForeignKey
            comment.save()

            # After saving, redirect back to the post details page
            return HttpResponseRedirect(f"/posts/{slug}")

        # If the form is not valid, render the page with errors
        return render(request, "Blog_App/post-details.html", {
            "post": post,
            "commentform": comment_form
        })

        

