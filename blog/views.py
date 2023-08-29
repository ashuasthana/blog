from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator
from django.core.mail import send_mail
from blog.forms import EmailSendForm,CommentForm
from django.conf import settings
from taggit.models import Tag



# Create your views here.

def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    template_name='blog/post_list.html'
    # post_list={'post_list':post_list}
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])

    #Pagination Code=====================================
    paginator=Paginator(post_list,4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request, template_name,{'page_obj':page_obj,'tag':tag})

def post_detail_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    # print("============================",Post.__dict__)
    # print("============================",dir(Post))

    #Post Comment Code=====================================

    comments=post.comments.filter(active=True)
    comment_submit=False

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # print("8888888888888888888888888888888")
            new_comment=form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            comment_submit=True
    else:
        form=CommentForm()
    return render(request,'blog/post_detail.html',{'post':post,'comments':comments,'form':form,'comment_submit':comment_submit})
    



    

#View for Share by mail=================================

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=='POST':
        form=EmailSendForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            # print(cd)#{'name': 'Ashish', 'eamil': 'as@gmail.com', 'to': 'as@gmail.com', 'commments': '555'}
            post_url = request.build_absolute_uri(post.get_absolute_url())
            # print(post_url,"*******************")
            s="'s"
            subject=f"Name:{cd['name']} Email:{cd['email']} recommends you to read, {post.title}."
            massage=f"""Read Post at:\n{post_url}\n\n {cd['name']+s} Commments: {cd['commments']}."""
            sender=settings.EMAIL_HOST_USER
            recipient_list=['ashuasthana07@gmail.com']
            print(massage)
            # send_mail(subject,massage,sender,recipient_list,fail_silently=False)
            sent=True

    form=EmailSendForm()  
    return render(request,'blog/sharebymail.html',{'post':post,'form':form,'sent':sent})

    