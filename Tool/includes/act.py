import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

def Open_redirect(url,redirect_url):
    redirect_param = [
        'redirect', 'redirect_uri', 'url', 'next', 'return', 'returnTo', 
        'post_logout_redirect_uri', 'continue', 'goto', 'destination', 
        'redir', 'callback', 'forward', 'redirect_url', 'redirect_to',
        'back', 'view', 'back_url', 'data', 'out', 'path', 'ref', 'uri'
    ]

    parsed_url = urlparse(url)
    original_query = parse_qs(parsed_url.query)

    for param in redirect_param:
        query_params = original_query.copy()
        query_params[param] = redirect_url
        modified_query = urlencode(query_params, doseq=True)
        modified_url = urlunparse(parsed_url._replace(query=modified_query))
        print(f"Testing with parameter {param}: {modified_url}")

        try:
            response = requests.get(modified_url, allow_redirects=True)
            final_url = response.url
            print(f"Final URL after redirects: {final_url}")

            if redirect_url in final_url:
                print(f"Vulnerable to open redirect via parameter {param}")
                return True
            else:
                print(f"Not Vulnerable to open redirect via parameter {param}")
        except requests.RequestException as e:
            print(f"Error checking URL: {e}")
    return False

