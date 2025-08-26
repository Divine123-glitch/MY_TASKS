# Modularizing_your_code2.py

# --- Section: Different Ways to Import Modules (math module example 1) ---
import math

# Lets put it to use
print(math.sqrt(9))
# - Note that you must specify the module name when calling a function within it.

# --- Section: Different Ways to Import Modules (math module example 2) ---
import math as m

# lets put it to use
print(m.sqrt(25))

# --- Section: Different Ways to Import Modules (math module example 3) ---
from math import sqrt, pi

print(sqrt(36))
print(pi)

# --- Section: Different Ways to Import Modules (math module example 4) ---
from math import *

print(sqrt(49))
print(pi)


# --- Section: Creating Your Package (__init__.py) ---
print("my_package is being imported")

# Optional: import functions directly for easier access
from .math_utils import add, subtract
from .string_utils import capitalize_text

# --- Section: Creating Your