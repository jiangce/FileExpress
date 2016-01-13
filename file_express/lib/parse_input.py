# -*- coding: utf-8 -*-


def get_input(prompt, method=None, default=None):
    result = ''
    if default is None:
        prompt = '%s<EXIT退出>：' % prompt
    else:
        prompt = '%s【默认 - %s】<EXIT退出>：' % (prompt, default)
    while result == '':
        result = input(prompt).strip()
        if result.lower() == 'exit':
            exit(0)
        result = result or default or ''
        if method:
            try:
                result = method(result)
            except:
                result = ''
    return result
