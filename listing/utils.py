def custom_tag_string(tag_string):
    """ takes in a string, returns a list """
    if not tag_string:
        return []
    if ',' not in tag_string:
        return [tag_string.title()]
    return [t.strip().title() for t in tag_string.split(',')]