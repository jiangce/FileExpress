# -*- coding: utf-8 -*-


def get_filter_set(filters=None):
    if isinstance(filters, str):
        filters = {filters}
    elif isinstance(filters, (tuple, list, set)):
        filters = set(filters)
    else:
        filters = {'*'}
    return filters
