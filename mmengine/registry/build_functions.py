# 定义一个根据参数实例化对象的方法，这含义就是说配置文件里的Type字段需要和你实际的类名对应上。然后实例化出一个对象。
def build_from_cfg(cfg, registry):
    obj_type = cfg.pop('type')
    obj_cls = registry.module_dict[obj_type]
    return obj_cls(**cfg)