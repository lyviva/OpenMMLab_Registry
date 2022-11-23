from mmdet.registry import HEAD

@HEAD.register_module()
class SepHead(object):
    def __init__(self, name):
        self.name = name
        print('Registry Head')
