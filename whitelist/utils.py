def get_user_agent(request):
    """ Get the user agent from the request
    """
    user_agent = request.META.get('HTTP_USER_AGENT')
    return user_agent


def get_resource(request):
    """ Get the resource being requested
    """
    path = request.path
    path = [x for x in path.split('/') if x]
    if path:
        return path[-1]
    else:
        return None


def get_ip_address(request):
    """ Get the IP Address from the request
    """
    ip_address = request.META.get('REMOTE_ADDR')
    if not ip_address or ip_address == '127.0.0.1':
        ip_address = request.META.get(
            'HTTP_X_FORWARDED_FOR', ip_address
        ).split(',')[0].strip()
    return ip_address


def is_request_genuine(ip_address, domain):
    """ Reverse and Forward DNS lookup
        Host must be a subdomain of 'domain'
    """

    if not ip_address:
        return False

    # Check host name
    host_info = socket.gethostbyaddr('ip_address')
    if not host_info:
        return False
    host_name = host_info[0]
    if not host_name:
        return False
    if not host_name.endswith(domain):
        return False

    # Double check IP
    host_ip = socket.gethostbyname(host_name)

    return host_ip == ip_address
