from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models.users import User

# Create your views here.


def index(request):

    return HttpResponse("""
        <ul>
            <li><a href="hello">Hello<a></li>
            <li><a href="world">world<a></li>
            <li><a href="users">list of users</a></li>
            <li><a href="user/0">Get one user</a> or <a href="user/1">Another one</a></li>
        </ul>
    """)


def hello(request):
    """Basic route with a template"""

    # getting our template
    template = loader.get_template('hello.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())


def world(request):
    """Basic route with a template"""

    # getting our template
    template = loader.get_template('world.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render())


def users(request):
    u = User()

    context = {
        'users': u.getUsers(),
    }

    # getting our template
    template = loader.get_template('users.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context))


def user(request, user_id):
    u = User()

    context = {
        'name': u.getUser(user_id)['name'],
        'email': u.getUser(user_id)['email'],
    }

    print(context)

    # getting our template
    template = loader.get_template('user.html')

    # rendering the template in HttpResponse
    return HttpResponse(template.render(context))
