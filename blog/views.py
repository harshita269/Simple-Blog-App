from django.shortcuts import render

posts = [
    {
        'author': 'Harshita Khare',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'March 16 , 2020'

    },
    {
        'author': 'Raghavnedra Khare',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'March 17 , 2020'

    },

]


def home(request):
    context = {
        'posts': posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')
