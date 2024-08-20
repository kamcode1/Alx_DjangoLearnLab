from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'member'

@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, 'relationship_app/member_dashboard.html')
