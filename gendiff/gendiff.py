import json


def parse(data, format_name):
    if format_name == '.json':
        return json.load(open(data))


def diff(dict1, dict2):
    result = []
    keys = sorted(dict1.keys() | dict2.keys())
    for key in keys:
        node = {'name': key}
        if key not in dict1:
            node['status'] = 'added'
            node['data'] = dict2[key]
        elif key not in dict2:
            node['status'] = 'deleted'
            node['data'] = dict1[key]
        elif type(dict1[key]) is dict and type(dict2[key]) is dict:
            node['status'] = 'nested'
            node['children'] = diff(dict1[key], dict2[key])
        elif dict1[key] == dict2[key]:
            node['status'] = 'not changed'
            node['data'] = dict1[key]
        else:
            node['status'] = 'changed'
            node['data before'] = dict1[key]
            node['data after'] = dict2[key]
        result.append(node)
    return result


def generate_diff(file_1, file_2):
    dict_1 = dict(parse(file_1))
    dict_2 = dict(parse(file_2))
    list_diff = diff(dict_1, dict_2)
    return list_diff