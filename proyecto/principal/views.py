# Create your views here.
# coding=utf-8
from django.contrib.auth.hashers import make_password

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.decorators import login_required


def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))
