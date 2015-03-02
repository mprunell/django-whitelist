from django.http import HttpResponseNotFound
from .utils import (get_user_agent,
                    get_resource,
                    get_ip_address,
                    is_request_genuine)

whitelist = ['Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)']
protected_resources = ['sitemap.xml']


class WhiteListMiddleware(object):
    """
    Rejects requests to sitemap.xml which are not from genuine bots.
    """
    def process_request(self, request):

        self.whitelist = {
            'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)': 'googlebot.com',
            'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm': 'search.msn.com',
        }

        if request.method == 'GET':
            # Get user agent and the resource being requested
            user_agent = get_user_agent(request)
            resource = get_resource(request)

            # If the resource is sitemap.xml,
            # do not return unless identity verified
            if resource in ['sitemap.xml']:

                # If resource is protected,
                # user agent needs to be present and whitelisted.
                if not user_agent or not self.whitelist.has_key(user_agent):
                    return HttpResponseNotFound()

                # Forward and reverse DNS lookup
                ip_address = get_ip_address(request)
                is_allowed = is_request_genuine(ip_address, self.whitelist['user_agent'])
                if not is_allowed:
                    return HttpResponseNotFound
