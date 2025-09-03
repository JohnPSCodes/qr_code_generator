import validators

def validate_url(url: str) -> bool:
    """Validates if the given URL is valid"""
    return validators.url(url)