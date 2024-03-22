import json

def build_filter(args):
    return Filter(args)

class Filter:
    def __init__(self, args):
        args = args.split(',')
        self.args = [a.encode('ascii', 'replace') for a in args]

    def notes_filter(self, filter_data, extra):
        extra_data = dict([
            (a.decode(), extra[a].decode()) for a in self.args if a in extra
        ])
        if extra_data:
            filter_data.update(extra_data)
