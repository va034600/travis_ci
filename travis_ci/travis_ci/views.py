from django.shortcuts import render


def v1(request):
    return render(request, 'travis_ci/v1.html', {})
