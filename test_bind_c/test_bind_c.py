from ctypes import *
from platform import *
import ctypes
import numpy as np

float_array_3 = c_float * 3
int_array_3 = c_int * 3


class simple(ctypes.Structure):
    _fields_ = [("s", c_float), ("s2", c_float)]


class input(ctypes.Structure):
    _fields_ = [("a", c_int), ("b", simple), ("b2", simple), ("float_array", float_array_3), ("int_array", int_array_3)]


class output(ctypes.Structure):
    _fields_ = [("c", c_float), ("float_array", float_array_3), ("int_array", int_array_3)]


dll = ctypes.cdll.LoadLibrary('./test_bind_c/libtest_func_export.dll')
win_c_dll = ctypes.cdll.LoadLibrary('msvcrt.dll')

# in_var_float_array = float_array_3()  # method 1: ok
# in_var_float_array[0] = c_float(1)
# in_var_float_array[1] = c_float(2)
# in_var_float_array[2] = c_float(3)
data = np.array([1.0, 2.0, 3.0])  # method 2: fail
data = data.astype(np.float32)
in_var_float_array = data.ctypes.data_as(POINTER(c_float))
# in_var_float_array = (c_float * 3)(1, 2, 3)   # method 3: ok
in_var_int_array = int_array_3()
in_var_int_array[0] = c_int(4)
in_var_int_array[1] = c_int(5)
in_var_int_array[2] = c_int(6)
in_var = input(10, simple(15), simple(15), in_var_float_array, in_var_int_array)
out_var = output()
# win_c_dll.printf(b"int: %d \n", 42)
test_func = dll.test_func
test_func.argtypes = [POINTER(output), POINTER(input)]
test_func.restype = c_void_p
test_func(byref(out_var), byref(in_var))
print(
    f'after call c function. out.c: {out_var.c}')
print(
    f'out.float_array[0]: {out_var.float_array[0]}, out.float_array[1]: {out_var.float_array[1]}, out.float_array[2]: {out_var.float_array[2]}')
print(
    f'out.int_array[0]: {out_var.int_array[0]}, out.int_array[1]: {out_var.int_array[1]}, out.int_array[2]: {out_var.int_array[2]}')
