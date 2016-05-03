%define module	tables

Summary: 	Hierarchical datasets in Python
Name: 	 	python-%{module}
Version: 	3.0.0
Release: 	3
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
BuildRequires:	liblzo-devel
BuildRequires:	python-cython >= 0.13
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
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

%package -n python2-%{module}
Summary:        Hierarchical datasets in Python 3
Group:          Development/Python
Requires: 	python2-numpy
Requires:	python2-numexpr
BuildRequires:	python2-numpy
BuildRequires:	python2-numpy-devel
BuildRequires:	python2-numexpr
BuildRequires:	python2-distribute
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-cython

%description -n python2-%{module}
PyTables is a Python 2 package for managing hierarchical datasets
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


%prep 
%setup -qc
mv %{module}-%{version} python2
cp -a python2 python3

find python3/utils -name 'pt*' | xargs sed -i '1s|^#!/usr/bin/env python|#!python3|'

%build
export LIBS="dl m"
pushd python2
CFLAGS="%{optflags}" python2 setup.py build
popd

pushd python3
CFLAGS="%{optflags}" python3 setup.py build
popd

%install
pushd python3
python3 setup.py install -O1 --skip-build --root %{buildroot}
popd

pushd python2
chmod -x examples/check_examples.sh
for i in utils/*; do sed -i 's|bin/env |bin/|' $i; done
python2 setup.py install -O1 --skip-build --root=%{buildroot}
mv %{buildroot}/usr/bin/pt2to3 %{buildroot}/usr/bin/pt2to32
mv %{buildroot}/usr/bin/ptdump %{buildroot}/usr/bin/ptdump2
mv %{buildroot}/usr/bin/ptrepack %{buildroot}/usr/bin/ptrepack2
popd

%check
pushd python3
libdir=`ls build/|grep lib`
export PYTHONPATH=`pwd`/build/$libdir
echo "import tables; tables.test()" > bench/check_all.py
python3 bench/check_all.py
popd

pushd python2
libdir=`ls build/|grep lib`
export PYTHONPATH=`pwd`/build/$libdir
echo "import tables; tables.test()" > bench/check_all.py
python2 bench/check_all.py
popd


%files
%doc python3/*.txt python2/LICENSES
%{_bindir}/pt2to3
%{_bindir}/ptdump
%{_bindir}/ptrepack
%{py3_platsitedir}/%{module}
%{py3_platsitedir}/%{module}-%{version}-py*.egg-info

%files doc
%doc python3/examples/
%doc python3/doc/html/

%files -n python2-%{module}
%doc python2/*.txt python3/LICENSES
%{_bindir}/pt2to32
%{_bindir}/ptdump2
%{_bindir}/ptrepack2
%{py2_platsitedir}/%{module}
%{py2_platsitedir}/%{module}-%{version}-py*.egg-info
