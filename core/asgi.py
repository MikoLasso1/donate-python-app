# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - Miko Lasso
"""

import os

from django.core.asgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_asgi_application()


