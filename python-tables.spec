%define module	tables

Summary: 	Hierarchical datasets in Python
Name: 	 	python-%{module}
Version: 	2.4.0
Release: 	3}
Source0:	http://pypi.python.org/packages/source/t/%{module}/%{module}-%{version}.tar.gz
Patch0:		setup.py.patch
License: 	BSD
Group: 	 	Development/Python
Url: 	 	http://www.pytables.org
Requires: 	python-numpy >= 1.4.1
Requires:	python-numexpr >= 1.4.1
Provides:	python-pytables = %{version}-%{release}
Obsoletes:	python-pytables < %{version}-%{release}
BuildRequires:	python-numpy-devel >= 1.4.1
BuildRequires:	python-numexpr >= 1.4.1
BuildRequires: 	hdf5-devel >= 1.6.10, bzip2-devel, liblzo-devel
BuildRequires:	python-cython >= 0.13
BuildRequires:	python-setuptools
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(lapack)
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
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files 
%doc *.txt THANKS doc/build/html/ examples/
%_bindir/nctoh5
%_bindir/ptdump
%_bindir/ptrepack
%py_platsitedir/%{module}*


%changelog
* Fri Jul 20 2012 Lev Givon <lev@mandriva.org> 2.4.0-1
+ Revision: 810496
- Update to 2.4.0.

* Sun Oct 30 2011 Lev Givon <lev@mandriva.org> 2.3.1-1
+ Revision: 707841
- Update to 2.3.1.

* Mon Sep 26 2011 Lev Givon <lev@mandriva.org> 2.3-1
+ Revision: 701378
- Update to 2.3.

* Fri Nov 05 2010 Lev Givon <lev@mandriva.org> 2.2.1-1mdv2011.0
+ Revision: 593767
- Update to 2.2.1.

* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 2.2-2mdv2011.0
+ Revision: 590085
- rebuild for python 2.7

* Tue Jul 13 2010 Lev Givon <lev@mandriva.org> 2.2-1mdv2011.0
+ Revision: 552164
- Update to 2.2.

* Thu Sep 17 2009 Lev Givon <lev@mandriva.org> 2.1.2-1mdv2010.0
+ Revision: 444130
- Update to 2.1.2.

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.1.1-2mdv2010.0
+ Revision: 442503
- rebuild

* Tue Mar 17 2009 Lev Givon <lev@mandriva.org> 2.1.1-1mdv2009.1
+ Revision: 356703
- Update to 2.1.1.

* Fri Jan 30 2009 Lev Givon <lev@mandriva.org> 2.1-3mdv2009.1
+ Revision: 335547
- Set version of provides.

* Wed Dec 24 2008 Lev Givon <lev@mandriva.org> 2.1-1mdv2009.1
+ Revision: 318406
- Update to 2.1.
- Change name

* Thu Nov 27 2008 Lev Givon <lev@mandriva.org> 2.0.4-4mdv2009.1
+ Revision: 307304
- Bump again.
- Bump release to rebuild.
- Rebuild against newer HDF5 libraries.

* Thu Aug 07 2008 Lev Givon <lev@mandriva.org> 2.0.4-1mdv2009.0
+ Revision: 266627
- Update to 2.0.4.

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.0.3-4mdv2009.0
+ Revision: 259773
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 2.0.3-3mdv2009.0
+ Revision: 247617
- rebuild

* Mon Mar 10 2008 Lev Givon <lev@mandriva.org> 2.0.3-1mdv2008.1
+ Revision: 183824
- Update to 2.0.3.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 28 2007 Lev Givon <lev@mandriva.org> 2.0.2-1mdv2008.1
+ Revision: 113805
- Update to 2.0.2.

* Thu Nov 15 2007 Lev Givon <lev@mandriva.org> 2.0.1-1mdv2008.1
+ Revision: 108953
- import python-pytables

