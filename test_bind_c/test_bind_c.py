from ctypes import *
from platform import *
import ctypes

float_array_3 = c_float * 3


class simple(ctypes.Structure):
    _fields_ = [("s", c_float)]


class input(ctypes.Structure):
    _fields_ = [("a", c_int), ("b", simple), ("float_array", float_array_3)]


class output(ctypes.Structure):
    _fields_ = [("c", c_float), ("float_array", float_array_3)]


dll = ctypes.cdll.LoadLibrary('./test_bind_c/libtest_func_export.dll')
win_c_dll = ctypes.cdll.LoadLibrary('msvcrt.dll')

in_var_float_array = float_array_3()
in_var_float_array[0] = c_float(1)
in_var_float_array[1] = c_float(2)
in_var_float_array[2] = c_float(3)
in_var = input(10, simple(15), in_var_float_array)
out_var = output()
# win_c_dll.printf(b"int: %d \n", 42)
test_func = dll.test_func
test_func.argtypes = [ctypes.POINTER(output), ctypes.POINTER(input)]
test_func.restype = c_void_p
test_func(byref(out_var), byref(in_var))
print(
    f'after call c function. out.c: {out_var.c}, out.float_array[0]: {out_var.float_array[0]}, '
    f'out.float_array[1]: {out_var.float_array[1]}, out.float_array[2]: {out_var.float_array[2]}')
