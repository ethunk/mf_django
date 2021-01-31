from django.http import HttpResponse
from django.shortcuts import redirect, render

from fool.models import Article, StockTicker, Comment
from fool.forms import CommentForm
from django.shortcuts import render


HOME_ARTICLE_PROMO = (
    """As autumn marches on, the trees are losing their leaves, and Barrick is """
    """losing its glitter."""
)

def index(request):
    return redirect('home')


def home(request):
    main_article = Article.objects.get(promo=HOME_ARTICLE_PROMO)
    secondary_articles = Article.objects.all().exclude(id=main_article.id).order_by('?')[0:3]
    context = {
        'main_article': main_article,
        'secondary_articles': secondary_articles,
    }
    return render(request, 'fool/home.html', context)

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    tickers = StockTicker.objects.all().order_by('?')[0:6]
    comments = article.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.cleaned_data
            comment['article_id'] = article.pk
            Comment(**comment).save()

    context = {
        'article': article,
        'tickers': tickers,
        'comments': comments,
        'comment_form': comment_form}

    return render(request, 'fool/article.html', context)


# def post_comment(request, slug):
#     template_name = 'post_detail.html'
#     post = get_object_or_404(Post, slug=slug)
#     comments = post.comments.filter(active=True)
#     new_comment = None
#     # Comment posted
#     if request.method == 'POST':
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():

#             # Create Comment object but don't save to database yet
#             new_comment = comment_form.save(commit=False)
#             # Assign the current post to the comment
#             new_comment.post = post
#             # Save the comment to the database
#             new_comment.save()
#     else:
#         comment_form = CommentForm()

#     return render(request, template_name, {'post': post,
#                                            'comments': comments,
#                                            'new_comment': new_comment,
#                                            'comment_form': comment_form})
