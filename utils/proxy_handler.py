def get_proxy_dict(proxy_url=None):
    if not proxy_url:
        return {}
        
    return {
        "http": proxy_url,
        "https": proxy_url
    }
