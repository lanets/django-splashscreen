# -*- coding: utf-8 -*-
#
#    Copyright (C) Alexandre Viau <alexandre@alexandreviau.net>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#
# This file's copyright is owned by Alexandre Viau so that it can be released
# under Expat at https://github.com/lanets/django-splashscreen
#

import re

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from lanets.apps.administration.models import Configuration


allowed_urls = [
    re.compile(r'^(/)*administration/.*'),
    re.compile(r'^(/)*admin/.*'),
    re.compile(r'^(/)*static/.*'),
    re.compile(r'^(/)*accounts/.*'),
    re.compile(r'^(/)*splashscreen/.*'),
]


class SplashScreenMiddleware(object):

    def process_request(self, request):
        config = Configuration.get_config()
        if not config.splashscreen:
            return

        for allowed_url in allowed_urls:
            if allowed_url.match(request.path_info):
                return

        return HttpResponseRedirect(reverse('main:splashscreen'))

