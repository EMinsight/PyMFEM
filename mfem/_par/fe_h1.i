%module(package="mfem._par") fe_h1
%{
#include  "mfem.hpp"
#include "fem/fe/fe_h1.hpp"
#include "mesh/hexahedron.hpp"
#include "numpy/arrayobject.h"    
%}

%init %{
import_array();
%}
%include "exception.i"
%import "fe_base.i"
%import "element.i"
%include "../common/typemap_macros.i"
%include "../common/exception.i"


%include "fem/fe/fe_h1.hpp"
