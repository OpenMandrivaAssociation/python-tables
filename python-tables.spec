%define module	tables
%define name 	python-%{module}
%define version 2.4.0
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define release	%{rel}
%endif

Summary: 	Hierarchical datasets in Python
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0:	http://pypi.python.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz
Patch0:		setup.py.patch
License: 	BSD
Group: 	 	Development/Python
Url: 	 	http://www.pytables.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	python-numpy >= 1.4.1
Requires:	python-numexpr >= 1.4.1
Provides:	python-pytables = %{version}-%{release}
Obsoletes:	python-pytables <= 2.0.4
BuildRequires:	python-numpy-devel >= 1.4.1
BuildRequires:	python-numexpr >= 1.4.1
BuildRequires: 	hdf5-devel >= 1.6.10, bzip2-devel, liblzo-devel
BuildRequires:	python-cython >= 0.13
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx
%py_requires -d 

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

%prep 
%setup -q -n %{module}-%{version}
%patch0 -p0

%build
export LIBS="dl m"
PYTHONDONTWRITEBYTECODE= %__python setup.py build
pushd doc
export PYTHONPATH=`ls -1d ../build/lib* | head -1`
make html
popd

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc *.txt THANKS doc/build/html/ examples/
%_bindir/nctoh5
%_bindir/ptdump
%_bindir/ptrepack
%py_platsitedir/%{module}*
