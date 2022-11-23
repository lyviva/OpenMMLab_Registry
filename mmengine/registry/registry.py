class Registry:
    def __init__(self, name):
        self.name = name
        self.module_dict = {}

    def _register_module(self, module_class):
        module_name = module_class.__name__
        self.module_dict[module_name] = module_class

    def register_module(self):
        def _register(cls):
            self._register_module(module_class=cls)
            return cls
        return _register