from django.shortcuts import render
from .models import Category, Announcement
# Create your views here.

def homepage(request):
    elonlar = Announcement.objects.all()
    category = Category.objects.all()
    context = {
        'elonlar': elonlar,
        'category': category,
    }
    return render(request, 'index.html', context)


def select_by_category(request, category_id):
    elonlar = Announcement.objects.filter(category=category_id)
    category = Category.objects.all()
    context = {
        'elonlar': elonlar,
        'category': category,
    }
    return render(request, 'index.html', context)



def announcement_detail(request, announcement_id):
    elon = Announcement.objects.get(id=announcement_id)
    category = Category.objects.all()
    context = {
        'elon': elon,
        'category': category,
    }
    return render(request, 'detail.html', context)