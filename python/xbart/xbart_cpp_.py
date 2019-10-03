# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError('Python 2.7 or later required')

import _xbart_cpp_

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
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


class XBARTcppParams(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    M = property(_xbart_cpp_.XBARTcppParams_M_get, _xbart_cpp_.XBARTcppParams_M_set)
    N_sweeps = property(_xbart_cpp_.XBARTcppParams_N_sweeps_get, _xbart_cpp_.XBARTcppParams_N_sweeps_set)
    Nmin = property(_xbart_cpp_.XBARTcppParams_Nmin_get, _xbart_cpp_.XBARTcppParams_Nmin_set)
    Ncutpoints = property(_xbart_cpp_.XBARTcppParams_Ncutpoints_get, _xbart_cpp_.XBARTcppParams_Ncutpoints_set)
    burnin = property(_xbart_cpp_.XBARTcppParams_burnin_get, _xbart_cpp_.XBARTcppParams_burnin_set)
    mtry = property(_xbart_cpp_.XBARTcppParams_mtry_get, _xbart_cpp_.XBARTcppParams_mtry_set)
    max_depth_num = property(_xbart_cpp_.XBARTcppParams_max_depth_num_get, _xbart_cpp_.XBARTcppParams_max_depth_num_set)
    alpha = property(_xbart_cpp_.XBARTcppParams_alpha_get, _xbart_cpp_.XBARTcppParams_alpha_set)
    beta = property(_xbart_cpp_.XBARTcppParams_beta_get, _xbart_cpp_.XBARTcppParams_beta_set)
    tau = property(_xbart_cpp_.XBARTcppParams_tau_get, _xbart_cpp_.XBARTcppParams_tau_set)
    kap = property(_xbart_cpp_.XBARTcppParams_kap_get, _xbart_cpp_.XBARTcppParams_kap_set)
    s = property(_xbart_cpp_.XBARTcppParams_s_get, _xbart_cpp_.XBARTcppParams_s_set)
    verbose = property(_xbart_cpp_.XBARTcppParams_verbose_get, _xbart_cpp_.XBARTcppParams_verbose_set)
    parallel = property(_xbart_cpp_.XBARTcppParams_parallel_get, _xbart_cpp_.XBARTcppParams_parallel_set)
    seed = property(_xbart_cpp_.XBARTcppParams_seed_get, _xbart_cpp_.XBARTcppParams_seed_set)
    sample_weights_flag = property(_xbart_cpp_.XBARTcppParams_sample_weights_flag_get, _xbart_cpp_.XBARTcppParams_sample_weights_flag_set)

    def __init__(self):
        _xbart_cpp_.XBARTcppParams_swiginit(self, _xbart_cpp_.new_XBARTcppParams())
    __swig_destroy__ = _xbart_cpp_.delete_XBARTcppParams

# Register XBARTcppParams in _xbart_cpp_:
_xbart_cpp_.XBARTcppParams_swigregister(XBARTcppParams)

class XBARTcpp(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _xbart_cpp_.XBARTcpp_swiginit(self, _xbart_cpp_.new_XBARTcpp(*args))

    def _to_json(self) -> "std::string":
        return _xbart_cpp_.XBARTcpp__to_json(self)

    def _fit(self, n: 'int', n_y: 'int', p_cat: 'size_t') -> "void":
        return _xbart_cpp_.XBARTcpp__fit(self, n, n_y, p_cat)

    def _predict(self, n: 'int') -> "void":
        return _xbart_cpp_.XBARTcpp__predict(self, n)

    def _predict_multinomial(self, n: 'int') -> "void":
        return _xbart_cpp_.XBARTcpp__predict_multinomial(self, n)

    def get_M(self) -> "int":
        return _xbart_cpp_.XBARTcpp_get_M(self)

    def get_N_sweeps(self) -> "int":
        return _xbart_cpp_.XBARTcpp_get_N_sweeps(self)

    def get_burnin(self) -> "int":
        return _xbart_cpp_.XBARTcpp_get_burnin(self)

    def get_yhats(self, size: 'int') -> "void":
        return _xbart_cpp_.XBARTcpp_get_yhats(self, size)

    def get_yhats_test(self, size: 'int') -> "void":
        return _xbart_cpp_.XBARTcpp_get_yhats_test(self, size)

    def get_yhats_test_multinomial(self, size: 'int') -> "void":
        return _xbart_cpp_.XBARTcpp_get_yhats_test_multinomial(self, size)

    def get_sigma_draw(self, size: 'int') -> "void":
        return _xbart_cpp_.XBARTcpp_get_sigma_draw(self, size)

    def _get_importance(self, size: 'int') -> "void":
        return _xbart_cpp_.XBARTcpp__get_importance(self, size)
    __swig_destroy__ = _xbart_cpp_.delete_XBARTcpp

# Register XBARTcpp in _xbart_cpp_:
_xbart_cpp_.XBARTcpp_swigregister(XBARTcpp)



