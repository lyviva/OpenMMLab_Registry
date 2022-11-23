from mmdet.registry import BACKBONE

@BACKBONE.register_module()
class ResNet(object):
    def __init__(self, name):
        self.name = name
        print('Registry ResNet')