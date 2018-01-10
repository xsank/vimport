# vimport
Support importing multi-version modules at the same time.
You can use setup.py to build your version-module, vimport also support this for the point is that
your version directory should be separated by "-" into module name part and version part.


# examples

``` python
lib_1 = import_module("lib", version="0.0.1")
lib_2 = import_module("lib", version="0.0.2")

lib_1.show()
lib_2.show()

modules = list_all_version_of_module("lib")

unload_module("lib", version="0.0.1")

lib_2 = reload_module("lib", version="0.0.2")
lib_2.show()

unload_all_module("lib")

```

# others
I have learn a lot from the project of the [multiversion](https://github.com/mitsuhiko/multiversion).
But it has not been maintained for nearly 7 years. And it is not support running different version in the same file.
So i wrote another project to do so.

Vimport works well in both python2 or python3. Please submit issue if you meet any problems.