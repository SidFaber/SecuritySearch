import ipaddress

def normalizeIP (ip_str):
    '''
    Return a normalized dotted-quad version of an IP address
    from a string. Return None if the string is not parseable
    as an IP address.
    '''
    try:
        ip_obj = ipaddress.IPv4Address (ip_str)
    except ipaddress.AddressValueError:
        return None
    return str(ip_obj)

# TODO: make name, title, homepage_url read-only properties that
#   are required when instantiating the object
# TODO: Move most of the javascript/html out of the template and into here
#   as generator functions.
# TODO: Rewrite the html_string functionality as a code generator
class SearchProvider (object):
    def __init__(self, name, title):
        self.name = name
        self.title = title
        self.homepage_url = ""
        self.html_string = "&nbsp;"

    def json_url(self, q):
        raise NotImplemented ("Method json_url is not implemented")
        


class IpapiSearch (SearchProvider):
    def __init__(self):
        super().__init__("ipapi", "IPApi")
        self.homepage_url = "https://ipapi.co/"
        self.html_string = '"<b>"+json.ip+"</b>: ASN "+json.asn+"; City "+json.city+"; Region "+json.region+"; Country "+json.country'
    
    def json_url (self, q):
        addr = normalizeIP(q)
        if addr is None:
            return None
        else:
            return "https://ipapi.co/" + addr + "/json/"

class IpinfoSearch (SearchProvider):
    def __init__(self):
        super().__init__("ipinfo", "IPInfo")
        self.homepage_url = "https://ipinfo.io/"
        self.html_string = '"<b>"+json.ip+"</b>: Hostname "+json.hostname+"; City "+json.city+"; Region "+json.region+"; Country "+json.country+"; Coords "+json.loc+"; Postal Code "+json.postal+"; Timezone "+json.timezone'
    
    def json_url (self, q):
        addr = normalizeIP(q)
        if addr is None:
            return None
        else:
            # TODO: Remove hardcoded API token.
            return "https://ipinfo.io/json/"+addr+"?token=6416bca288f5fe"

