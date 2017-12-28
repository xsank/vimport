# vimport
Support importing multi-version modules at the same time.


# examples

``` python
lib_1 = import_module("lib", version=1)
lib_2 = import_module("lib", version=2)

lib_1.show()
lib_2.show()

modules = list_all_version_of_module("lib")
print(modules)

unload_module("lib", 1)

lib_2 = reload_module("lib", 2)
lib_2.show()

unload_all_module("lib")
modules = list_all_version_of_module("lib")
print(modules)

```

# others
I have learn a lot from the project of the [multiversion](https://github.com/mitsuhiko/multiversion).
But it has not been maintained for nearly 7 years. And it is not support running different version in the same file.
So i wrote another project to do so.
Vimport works well in both python2 or python3. Please submit issue if you meet any problems.