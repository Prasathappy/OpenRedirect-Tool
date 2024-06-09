import requests
from urllib.parse import urlparse, urljoin

def Open_Redirect(url, redirect_url):
    try:
        div_base = urlparse(url)
        test = urljoin(url, f"?next={redirect_url}")
        response = requests.get(test, allow_redirects=False)
        if 'Location' in response.headers:
            location = response.headers['Location']
            div_location = urlparse(location)
            if div_location.netloc != div_base.netloc:
                return True
        return False
    except requests.RequestException as e:
        print(f"Error while checking URL: {e}")
        return False

 