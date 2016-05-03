%define module	tables

Summary: 	Hierarchical datasets in Python
Name: 	 	python-%{module}
Version: 	3.2.2
Release: 	1
Source0: 	https://pypi.python.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz
License: 	BSD
Group: 	 	Development/Python
Url: 	 	http://www.pytables.org
Requires: 	python-numpy >= 1.4.1
Requires:	python-numexpr >= 1.4.1
BuildRequires:	python-numpy >= 1.4.1
BuildRequires:	python-numpy-devel >= 1.4.1
BuildRequires:	python-numexpr >= 1.4.1
BuildRequires: 	hdf5-devel >= 1.6.10
BuildRequires:	bzip2-devel
BuildRequires:	lzo-devel
BuildRequires:	python-cython >= 0.13
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(lapack)
%rename python-pytables
%rename	python3-tables

%description
PyTables is a Python package for managing hierarchical datasets
designed to efficiently and easily cope with extremely large amounts
of data. It is built on top of the HDF5 library and the NumPy package
(numarray and Numeric are also supported). PyTables features an
object-oriented interface and performance-critical extensions coded in
C (generated using Pyrex) that make it a fast yet extremely
easy-to-use tool for interactively processing and searching through
very large amounts of data. PyTables also optimizes memory and disk
resources so that data occupies much less space than with other
solutions such as relational or object-oriented databases (especially
when compression is used).

%package	doc
Group:		Development/Python
Summary:	Documentation for PyTables
BuildArch:	noarch

%description doc
The %{name}-doc package contains the documentation related to 
PyTables.

%prep 
%setup -qn %{module}-%{version}

find utils -name 'pt*' | xargs sed -i '1s|^#!/usr/bin/env python|#!python3|'

%build
export LIBS="dl m"
CFLAGS="%{optflags}" python3 setup.py build

%install
python3 setup.py install -O1 --skip-build --root %{buildroot}

%check
libdir=`ls build/|grep lib`
export PYTHONPATH=`pwd`/build/$libdir
echo "import tables; tables.test()" > bench/check_all.py
python3 bench/check_all.py

%files
%doc *.txt LICENSES
%{_bindir}/pt2to3
%{_bindir}/ptdump
%{_bindir}/ptrepack
%{_bindir}/pttree
%{py3_platsitedir}/%{module}
%{py3_platsitedir}/%{module}-%{version}-py*.egg-info

%files doc
%doc examples/
%doc doc/html/
