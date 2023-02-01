# Packages: simply a folder containing one or more modules.
# Modules: A set of python files, we can use the method of other packages.

# To import
# 1. import package.moduleName.method_name > have to use package.moduleName.method_name.method_name to use the method in function.
import shopping_pkg.shopping_cart_mod
print(shopping_pkg.shopping_cart_mod.buy('Apple'))


# 2. from package.moduleName import method_name > Can directly use imported method name
from shopping_pkg.shopping_cart_mod import buy
print(buy('Apple'))