from django.shortcuts import render
import logging

logger = logging.getLogger('command')


def v1(request):
    aaa = 0
    if "aaa" in request.GET:
        # query_paramが指定されている場合の処理
        try:
            aaa = int(request.GET.get("aaa"))
            logger.info(f'aaa:{aaa}')
        except Exception as e:
            logger.error(e)

    return render(request, 'travis_ci/v1.html', {'aaa': aaa})
