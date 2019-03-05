from django.shortcuts import render,render_to_response,get_object_or_404
from django.http import HttpResponse,Http404
from article.models import Article


def article_detail(request, article_id):
    # try:
    #     article = Article.objects.get(id=article_id)
    #     content = {}
    #     content['article'] = article
    #     # return render(request,'article_detail.html',content)
    #     return  render_to_response('article_detail.html',content)
    # except  Article.DoesNotExist:
    #     raise Http404("not find")
        # return  HttpResponse('不存在')

    # 简化版
    article = get_object_or_404(Article,id=article_id)
    context = {}
    context['article'] = article
    return  render_to_response('article_detail.html',context)
