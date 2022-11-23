from mmdet.models.builder import build_backbone, build_head

class SampleModel():
    def __init__(self, backbone, head):
        self.backbone = build_backbone(backbone)
        self.head = build_head(head)

    def run(self):
        print('Backbone:',self.backbone.name)
        print('Head:', self.head.name)

cfg = dict(
    backbone=dict(type='ResNet', name='test_backbone'),
    head=dict(type='SepHead', name='test_head')
)
model = SampleModel(**cfg)
model.run()