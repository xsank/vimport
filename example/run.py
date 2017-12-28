from vimport import import_module, unload_module, reload_module, list_all_version_of_module, unload_all_module

if __name__ == "__main__":
    lib_1 = import_module("lib", version=1)
    lib_2 = import_module("lib", version=2)

    lib_1.show()
    lib_2.show()

    lib_1 = import_module("lib", version=1)
    lib_1.show()

    modules = list_all_version_of_module("lib")
    print(modules)

    unload_module("lib", version=1)

    modules = list_all_version_of_module("lib")
    print(modules)

    lib_2 = reload_module("lib", version=2)
    lib_2.show()

    modules = list_all_version_of_module("lib")
    print(modules)

    unload_all_module("lib")
    modules = list_all_version_of_module("lib")
    print(modules)
