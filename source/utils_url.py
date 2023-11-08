def concatenate_url(base_url, *path_segments):
    """
    Concatenate the base URL with additional path segments.
    """
    if not base_url.endswith('/'):
        base_url += '/'

    full_url = base_url + "/".join(segment.strip('/') for segment in path_segments)

    return full_url

