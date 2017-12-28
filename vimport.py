import os
import sys
import imp
import importlib

NAMESPACE = "vimport.namespace"

multi_version_space = imp.new_module(NAMESPACE)
multi_version_space.__path__ = []
multi_version_space.__cache__ = {}
multi_version_space.__map__ = {}

sys.modules[NAMESPACE] = multi_version_space


def __module_check(name, version):
    if type(name) is not str:
        raise RuntimeError('module name should be string')

    # we will test this later...
    if type(version) is not int:
        raise RuntimeError('version should be int only')


def __version_module_name(name, version):
    return '%s_%s' % (name, version)


def __intern_module_name(name, version):
    return '%s.%s' % (NAMESPACE, __version_module_name(name, version))


def __real_module_name(name, version):
    return '%s.%s' % (__intern_module_name(name, version), name)


def __is_module_loaded(name, version):
    v_module = __version_module_name(name, version)
    return v_module in sys.modules


def __load_module(name, version):
    v_dir = v_module = __version_module_name(name, version)
    for path in sys.path:
        full_path = os.path.join(path, v_dir)
        if os.path.isdir(full_path):
            intern_name = __intern_module_name(name, version)
            module = imp.new_module(intern_name)
            setattr(multi_version_space, v_module, module)
            module.__path__ = [full_path]
            sys.modules[module.__name__] = module
            return True
    return False


def unload_all_module(name):
    _map = multi_version_space.__map__
    v_modules = _map.get(name)
    if v_modules:
        for m in v_modules:
            multi_version_space.__cache__.pop(m)
            sys.modules.pop(m)
        _map.pop(name)
        return True
    return False


def unload_module(name, version):
    __module_check(name, version)
    i_module = __intern_module_name(name, version)
    _cache = multi_version_space.__cache__
    _map = multi_version_space.__map__
    if name in _map and i_module in _cache:
        _cache.pop(i_module)
        _map.get(name).remove(i_module)
        sys.modules.pop(i_module)
        return True
    return False


def import_module(name, version, force=False):
    __module_check(name, version)
    mod_name = __intern_module_name(name, version)
    _cache = multi_version_space.__cache__
    _map = multi_version_space.__map__

    if force:
        unload_module(name, version)

    if mod_name not in _cache:
        if not __is_module_loaded(name, version):
            if __load_module(name, version):
                real_name = __real_module_name(name, version)
                i_module = importlib.import_module(real_name)
                _cache[mod_name] = i_module
                _map.setdefault(name, set()).add(mod_name)
    return _cache.get(mod_name)


def reload_module(name, version):
    unload_module(name, version)
    return import_module(name, version)


def list_all_version_of_module(name):
    v_modules = multi_version_space.__map__.get(name)
    res = []
    if v_modules:
        for m in v_modules:
            res.append(m.rsplit(".", 1)[-1])
    return res
