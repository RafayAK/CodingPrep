"""
This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""

add_to_basekey = lambda basekey, key: basekey + "." + key

def get_keys(d:dict):
    try:
        return list(d.keys())
    except AttributeError:
        return None

def flatten_dict(dictionary:dict):
    flat_dict = {}

    def helper(basekey, values):
        if isinstance(values, dict):
            # that means "values" to this "key" were a dict
            for k in get_keys(values):
                helper(add_to_basekey(basekey, k), values[k])
        else:
            # values was not a dict for this key
            flat_dict[basekey] = values

    for key in get_keys(d):
        helper(key, dictionary[key])

    return flat_dict


if __name__ == '__main__':

    d = {
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
            }
        }
    }

    print(flatten_dict(d))