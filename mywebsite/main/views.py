from django.http.response import HttpResponseNotFound
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from main.models import Detail
from main.models import Item
from main.models import Post


mycontext = {
    'static_mydetails': '',
    'static_itemlist': '',
    'static_postlist': '',
}


def home_view(req, *args, **kwargs):

    url = ''

    if 'page' not in req.GET:
        return redirect_to_home()
    else:
        url = '/?page=' + req.GET['page']

    if not is_url_valid(url):
        return redirect_to_home()

    render_header()
    render_body(url)

    return render(req, 'html/index.html', mycontext)


def redirect_to_home():
    return redirect('/?page=Home')


def render_header():

    detaillist = mark_safe('')

    for detail in Detail.objects.all():
        detaillist += render_to_string('html/detail.html', {
            'img': detail.img,
            'url': detail.url
        })

    mycontext['static_mydetails'] = detaillist

    itemlist = mark_safe('')

    for item in Item.objects.all():
        itemlist += render_to_string('html/item.html', {
            'title': item.title,
            'url': item.url,
            'img': item.img
        })

    mycontext['static_itemlist'] = itemlist


def render_body(url):

    postlist = mark_safe('')

    for post in Post.objects.order_by('priority__value').all():
        if (post.posttype.url == url):

            date_string = post.date
            if post.date == None:
                date_string = ''

            postlist += render_to_string('html/post.html', {
                'title': post.title,
                'date': date_string,
                'body': mark_safe(post.body)
            })

    mycontext['static_postlist'] = postlist


def is_url_valid(url):

    for item in Item.objects.all():
        if url == item.url:
            return True

    return False


def response_404(req, exception=None):
    return redirect_to_home()
