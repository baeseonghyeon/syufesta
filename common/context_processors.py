from django.conf import settings

def global_settings(req):
    return {
        'ASSETS_VERSION' : '0.2.0'
     }
    