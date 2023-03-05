from ctypes import *
from platform import *
import ctypes


class simple(ctypes.Structure):
    _fields_ = [("s", c_int)]


class input(ctypes.Structure):
    _fields_ = [("a", c_int), ("b", simple)]


class output(ctypes.Structure):
    _fields_ = [("c", c_int)]


dll = ctypes.cdll.LoadLibrary('./libtest_func.dll')
win_c_dll = ctypes.cdll.LoadLibrary('msvcrt.dll')

in_var = input(10, simple(15))
out_var = output()
# win_c_dll.printf(b"int: %d \n", 42)
test_func = dll.test_func
test_func.argtypes = [ctypes.POINTER(output), ctypes.POINTER(input)]
test_func.restype = c_void_p
test_func(byref(out_var), byref(in_var))
print('return: ', out_var.c)
