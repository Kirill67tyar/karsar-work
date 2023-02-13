from django.shortcuts import render, HttpResponse


def exp_view(request):
    email = 'unknown'
    if request.user.is_authenticated:
        email = request.user.email

    return render(
        request=request,
        template_name='catalog/list.html',
        context={'email': email, }
    )
