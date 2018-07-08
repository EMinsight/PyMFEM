# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_vector')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_vector')
    _vector = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_vector', [dirname(__file__)])
        except ImportError:
            import _vector
            return _vector
        try:
            _mod = imp.load_module('_vector', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _vector = swig_import_helper()
    del swig_import_helper
else:
    import _vector
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

import array
import ostream_typemap

def add_vector(*args):
    """
    add_vector(Vector v1, Vector v2, Vector v)
    add_vector(Vector v1, double alpha, Vector v2, Vector v)
    add_vector(double const a, Vector x, Vector y, Vector z)
    add_vector(double const a, Vector x, double const b, Vector y, Vector z)
    """
    return _vector.add_vector(*args)

def subtract_vector(*args):
    """
    subtract_vector(Vector v1, Vector v2, Vector v)
    subtract_vector(double const a, Vector x, Vector y, Vector z)
    """
    return _vector.subtract_vector(*args)

def CheckFinite(v, n):
    """CheckFinite(double const * v, int const n) -> int"""
    return _vector.CheckFinite(v, n)

def infinity():
    """infinity() -> double"""
    return _vector.infinity()
class Vector(_object):
    """Proxy of C++ mfem::Vector class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Vector, name)
    __repr__ = _swig_repr

    def Load(self, *args):
        """
        Load(Vector self, std::istream ** arg2, int np, int * dim)
        Load(Vector self, std::istream & arg2, int Size)
        Load(Vector self, std::istream & arg2)
        """
        return _vector.Vector_Load(self, *args)


    def SetSize(self, s):
        """SetSize(Vector self, int s)"""
        return _vector.Vector_SetSize(self, s)


    def SetData(self, d):
        """SetData(Vector self, double * d)"""
        return _vector.Vector_SetData(self, d)


    def SetDataAndSize(self, d, s):
        """SetDataAndSize(Vector self, double * d, int s)"""
        return _vector.Vector_SetDataAndSize(self, d, s)


    def NewDataAndSize(self, d, s):
        """NewDataAndSize(Vector self, double * d, int s)"""
        return _vector.Vector_NewDataAndSize(self, d, s)


    def MakeDataOwner(self):
        """MakeDataOwner(Vector self)"""
        return _vector.Vector_MakeDataOwner(self)


    def Destroy(self):
        """Destroy(Vector self)"""
        return _vector.Vector_Destroy(self)


    def Size(self):
        """Size(Vector self) -> int"""
        return _vector.Vector_Size(self)


    def Capacity(self):
        """Capacity(Vector self) -> int"""
        return _vector.Vector_Capacity(self)


    def GetData(self):
        """GetData(Vector self) -> double *"""
        return _vector.Vector_GetData(self)


    def OwnsData(self):
        """OwnsData(Vector self) -> bool"""
        return _vector.Vector_OwnsData(self)


    def StealData(self, *args):
        """
        StealData(Vector self, double ** p)
        StealData(Vector self) -> double *
        """
        return _vector.Vector_StealData(self, *args)


    def Elem(self, *args):
        """
        Elem(Vector self, int i) -> double
        Elem(Vector self, int i) -> double const &
        """
        return _vector.Vector_Elem(self, *args)


    def __call__(self, *args):
        """
        __call__(Vector self, int i) -> double
        __call__(Vector self, int i) -> double const &
        """
        return _vector.Vector___call__(self, *args)


    def __mul__(self, *args):
        """
        __mul__(Vector self, double const * arg2) -> double
        __mul__(Vector self, Vector v) -> double
        """
        return _vector.Vector___mul__(self, *args)


    def __imul__(self, v):
        ret = _vector.Vector___imul__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0            
        return self



    def __itruediv__(self, v):
        ret = _vector.Vector___itruediv__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0      
        return self



    def __isub__(self, v):
        ret = _vector.Vector___isub__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0            
        return self



    def __iadd__(self, v):
        ret = _vector.Vector___iadd__(self, v)
    #ret.thisown = self.thisown
        ret.thisown = 0                  
        return self



    def Add(self, a, Va):
        """Add(Vector self, double const a, Vector Va) -> Vector"""
        return _vector.Vector_Add(self, a, Va)


    def Set(self, a, x):
        """Set(Vector self, double const a, Vector x) -> Vector"""
        return _vector.Vector_Set(self, a, x)


    def SetVector(self, v, offset):
        """SetVector(Vector self, Vector v, int offset)"""
        return _vector.Vector_SetVector(self, v, offset)


    def Neg(self):
        """Neg(Vector self)"""
        return _vector.Vector_Neg(self)


    def Swap(self, other):
        """Swap(Vector self, Vector other)"""
        return _vector.Vector_Swap(self, other)


    def median(self, lo, hi):
        """median(Vector self, Vector lo, Vector hi)"""
        return _vector.Vector_median(self, lo, hi)


    def GetSubVector(self, *args):
        """
        GetSubVector(Vector self, intArray dofs, Vector elemvect)
        GetSubVector(Vector self, intArray dofs, double * elem_data)
        """
        return _vector.Vector_GetSubVector(self, *args)


    def SetSubVector(self, *args):
        """
        SetSubVector(Vector self, intArray dofs, double const value)
        SetSubVector(Vector self, intArray dofs, Vector elemvect)
        SetSubVector(Vector self, intArray dofs, double * elem_data)
        """
        return _vector.Vector_SetSubVector(self, *args)


    def AddElementVector(self, *args):
        """
        AddElementVector(Vector self, intArray dofs, Vector elemvect)
        AddElementVector(Vector self, intArray dofs, double * elem_data)
        AddElementVector(Vector self, intArray dofs, double const a, Vector elemvect)
        """
        return _vector.Vector_AddElementVector(self, *args)


    def SetSubVectorComplement(self, dofs, val):
        """SetSubVectorComplement(Vector self, intArray dofs, double const val)"""
        return _vector.Vector_SetSubVectorComplement(self, dofs, val)


    def Print_HYPRE(self, out):
        """Print_HYPRE(Vector self, std::ostream & out)"""
        return _vector.Vector_Print_HYPRE(self, out)


    def Randomize(self, seed=0):
        """
        Randomize(Vector self, int seed=0)
        Randomize(Vector self)
        """
        return _vector.Vector_Randomize(self, seed)


    def Norml2(self):
        """Norml2(Vector self) -> double"""
        return _vector.Vector_Norml2(self)


    def Normlinf(self):
        """Normlinf(Vector self) -> double"""
        return _vector.Vector_Normlinf(self)


    def Norml1(self):
        """Norml1(Vector self) -> double"""
        return _vector.Vector_Norml1(self)


    def Normlp(self, p):
        """Normlp(Vector self, double p) -> double"""
        return _vector.Vector_Normlp(self, p)


    def Max(self):
        """Max(Vector self) -> double"""
        return _vector.Vector_Max(self)


    def Min(self):
        """Min(Vector self) -> double"""
        return _vector.Vector_Min(self)


    def Sum(self):
        """Sum(Vector self) -> double"""
        return _vector.Vector_Sum(self)


    def DistanceSquaredTo(self, p):
        """DistanceSquaredTo(Vector self, double const * p) -> double"""
        return _vector.Vector_DistanceSquaredTo(self, p)


    def DistanceTo(self, p):
        """DistanceTo(Vector self, double const * p) -> double"""
        return _vector.Vector_DistanceTo(self, p)


    def CheckFinite(self):
        """CheckFinite(Vector self) -> int"""
        return _vector.Vector_CheckFinite(self)

    __swig_destroy__ = _vector.delete_Vector
    __del__ = lambda self: None

    def __init__(self, *args):
        """
        __init__(mfem::Vector self) -> Vector
        __init__(mfem::Vector self, Vector arg2) -> Vector
        __init__(mfem::Vector self, int s) -> Vector
        __init__(mfem::Vector self, double * _data, int _size) -> Vector
        __init__(mfem::Vector self, Vector v, int offset, int size) -> Vector
        """

        from numpy import ndarray, ascontiguousarray
        keep_link = False
        own_data = False  
        if len(args) == 1:
            if isinstance(args[0], list): 
                args = (args[0], len(args[0]))
                own_data = True	  
            elif isinstance(args[0], ndarray):
                if args[0].dtype != 'float64':
                    raise ValueError('Must be float64 array')
                else:
          	    args = (ascontiguousarray(args[0]), args[0].shape[0])
        # in this case, args[0] need to be maintained
        # in this object.
        	    keep_link = True


        this = _vector.new_Vector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

        if keep_link:
           self._link_to_data = args[0]
        if own_data:
           self.MakeDataOwner()




    def Assign(self, *args):
        """
        Assign(Vector self, double const v)
        Assign(Vector self, PyObject * param)
        """

        from numpy import ndarray, ascontiguousarray
        if len(args) == 1 and isinstance(args[0], ndarray):
                if args[0].dtype != 'float64':
                    raise ValueError('Must be float64 array')
                elif args[0].ndim != 1:
                    raise ValueError('Ndim must be one') 
                elif args[0].shape[0] != _vector.Vector_Size(self):
                    raise ValueError('Length does not match')
                else:
          	    args = (ascontiguousarray(args[0]),)


        val = _vector.Vector_Assign(self, *args)

        return self


        return val


    def Print(self, *args):
        """
        Print(Vector self, std::ostream & out, int width=8)
        Print(Vector self, std::ostream & out)
        Print(Vector self)
        Print(Vector self, char const * file)
        """
        return _vector.Vector_Print(self, *args)


    def __setitem__(self, i, v):
        """__setitem__(Vector self, int i, double const v)"""
        return _vector.Vector___setitem__(self, i, v)


    def __getitem__(self, param):
        """__getitem__(Vector self, PyObject * param) -> PyObject *"""
        return _vector.Vector___getitem__(self, param)


    def GetDataArray(self):
        """GetDataArray(Vector self) -> PyObject *"""
        return _vector.Vector_GetDataArray(self)

Vector_swigregister = _vector.Vector_swigregister
Vector_swigregister(Vector)


def IsFinite(val):
    """IsFinite(double const & val) -> bool"""
    return _vector.IsFinite(val)

def DistanceSquared(x, y, n):
    """DistanceSquared(double const * x, double const * y, int const n) -> double"""
    return _vector.DistanceSquared(x, y, n)

def Distance(x, y, n):
    """Distance(double const * x, double const * y, int const n) -> double"""
    return _vector.Distance(x, y, n)

Vector.__idiv__ = Vector.__itruediv__

# This file is compatible with both classic and new-style classes.


