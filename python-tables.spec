%define module	tables
%define name 	python-%{module}
%define version 2.1.1
%define release %mkrel 1

Summary: 	Hierarchical datasets in Python
Name: 	 	%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{module}-%{version}.tar.gz
Patch0:		setup.py.patch
License: 	BSD
Group: 	 	Development/Python
Url: 	 	http://www.pytables.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: 	python-numpy >= 1.2
Provides:	python-pytables = %{version}-%{release}
Obsoletes:	python-pytables <= 2.0.4
BuildRequires:	python-numpy >= 1.2, python-numpy-devel >= 1.2
BuildRequires: 	hdf5-devel >= 1.6.7, bzip2-devel, liblzo-devel
BuildRequires:	python-setuptools
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
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc *.txt doc/*.pdf LICENSES examples
