# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _common_functions
else:
    import _common_functions

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

_swig_new_instance_method = _common_functions.SWIG_PyInstanceMethod_New
_swig_new_static_method = _common_functions.SWIG_PyStaticMethod_New

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


MFEM_VERSION = _common_functions.MFEM_VERSION
MFEM_VERSION_STRING = _common_functions.MFEM_VERSION_STRING
MFEM_VERSION_TYPE = _common_functions.MFEM_VERSION_TYPE
MFEM_VERSION_TYPE_RELEASE = _common_functions.MFEM_VERSION_TYPE_RELEASE
MFEM_VERSION_TYPE_DEVELOPMENT = _common_functions.MFEM_VERSION_TYPE_DEVELOPMENT
MFEM_VERSION_MAJOR = _common_functions.MFEM_VERSION_MAJOR
MFEM_VERSION_MINOR = _common_functions.MFEM_VERSION_MINOR
MFEM_VERSION_PATCH = _common_functions.MFEM_VERSION_PATCH
MFEM_SOURCE_DIR = _common_functions.MFEM_SOURCE_DIR
MFEM_INSTALL_DIR = _common_functions.MFEM_INSTALL_DIR
MFEM_GIT_STRING = _common_functions.MFEM_GIT_STRING
MFEM_TIMER_TYPE = _common_functions.MFEM_TIMER_TYPE
MFEM_HYPRE_VERSION = _common_functions.MFEM_HYPRE_VERSION
import mfem._par.array
import mfem._par.mem_manager

def Transpose(*args):
    r"""
    Transpose(mfem::Table const & A, mfem::Table & At, int _ncols_A=-1)
    Transpose(mfem::Table const & A) -> mfem::Table
    Transpose(intArray A, mfem::Table & At, int _ncols_A=-1)
    Transpose(mfem::BlockMatrix const & A) -> mfem::BlockMatrix
    Transpose(mfem::SparseMatrix const & A) -> mfem::SparseMatrix *
    """
    return _common_functions.Transpose(*args)
Transpose = _common_functions.Transpose

def Mult(*args):
    r"""
    Mult(mfem::Table const & A, mfem::Table const & B, mfem::Table & C)
    Mult(mfem::Table const & A, mfem::Table const & B) -> mfem::Table
    Mult(mfem::BlockMatrix const & A, mfem::BlockMatrix const & B) -> mfem::BlockMatrix
    Mult(mfem::DenseMatrix const & b, mfem::DenseMatrix const & c, mfem::DenseMatrix & a)
    Mult(mfem::SparseMatrix const & A, mfem::SparseMatrix const & B, mfem::SparseMatrix * OAB=None) -> mfem::SparseMatrix
    Mult(mfem::SparseMatrix const & A, mfem::DenseMatrix & B) -> mfem::DenseMatrix *
    """
    return _common_functions.Mult(*args)
Mult = _common_functions.Mult

def InnerProduct(*args):
    r"""
    InnerProduct(mfem::Vector const & x, mfem::Vector const & y) -> double
    InnerProduct(MPI_Comm comm, mfem::Vector const & x, mfem::Vector const & y) -> double
    InnerProduct(mfem::HypreParVector & x, mfem::HypreParVector & y) -> double
    InnerProduct(mfem::HypreParVector * x, mfem::HypreParVector * y) -> double
    """
    return _common_functions.InnerProduct(*args)
InnerProduct = _common_functions.InnerProduct

def Add(*args):
    r"""
    Add(mfem::DenseMatrix const & A, mfem::DenseMatrix const & B, double alpha, mfem::DenseMatrix & C)
    Add(double alpha, double const * A, double beta, double const * B, mfem::DenseMatrix & C)
    Add(double alpha, mfem::DenseMatrix const & A, double beta, mfem::DenseMatrix const & B, mfem::DenseMatrix & C)
    Add(mfem::SparseMatrix const & A, mfem::SparseMatrix const & B) -> mfem::SparseMatrix
    Add(double a, mfem::SparseMatrix const & A, double b, mfem::SparseMatrix const & B) -> mfem::SparseMatrix
    Add(mfem::Array< mfem::SparseMatrix * > & Ai) -> mfem::SparseMatrix
    Add(mfem::SparseMatrix const & A, double alpha, mfem::DenseMatrix & B)
    Add(double alpha, mfem::HypreParMatrix const & A, double beta, mfem::HypreParMatrix const & B) -> mfem::HypreParMatrix *
    """
    return _common_functions.Add(*args)
Add = _common_functions.Add

def RAP(*args):
    r"""
    RAP(mfem::SparseMatrix const & A, mfem::DenseMatrix & P) -> mfem::DenseMatrix
    RAP(mfem::DenseMatrix & A, mfem::SparseMatrix const & P) -> mfem::DenseMatrix
    RAP(mfem::SparseMatrix const & A, mfem::SparseMatrix const & R, mfem::SparseMatrix * ORAP=None) -> mfem::SparseMatrix
    RAP(mfem::SparseMatrix const & Rt, mfem::SparseMatrix const & A, mfem::SparseMatrix const & P) -> mfem::SparseMatrix
    RAP(mfem::HypreParMatrix const * A, mfem::HypreParMatrix const * P) -> mfem::HypreParMatrix
    RAP(mfem::HypreParMatrix const * Rt, mfem::HypreParMatrix const * A, mfem::HypreParMatrix const * P) -> mfem::HypreParMatrix *
    """
    return _common_functions.RAP(*args)
RAP = _common_functions.RAP

