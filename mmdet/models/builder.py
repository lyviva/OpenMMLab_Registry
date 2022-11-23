from mmengine.registry.build_functions import build_from_cfg
from mmdet.registry import BACKBONE, HEAD

def build_backbone(cfg):
    return build_from_cfg(cfg, BACKBONE)

def build_head(cfg):
    return build_from_cfg(cfg, HEAD)