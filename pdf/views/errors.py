from ..utils import render_with_appname

def handle_404(request, exception=None):
    context = {}
    return render_with_appname(request, "404.html", context=context, status=404)

def handle_500(request, *args, **argv):
    '''
    'logger = logging.getLogger(__name__)
    error = argv[0] if argv else None
    logger.error("Internal Server Error: %s", error)'
    '''

    context = {}
    return render_with_appname(request, "500.html", context=context, status=500)