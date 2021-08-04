#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : identify
Version  : 2.2.12
Release  : 5
URL      : https://files.pythonhosted.org/packages/fa/ae/b2361177e92bcea99d5dded37bfa03f7f48d8a1dca9c14906d3d4b0d0a65/identify-2.2.12.tar.gz
Source0  : https://files.pythonhosted.org/packages/fa/ae/b2361177e92bcea99d5dded37bfa03f7f48d8a1dca9c14906d3d4b0d0a65/identify-2.2.12.tar.gz
Summary  : File identification library for Python
Group    : Development/Tools
License  : MIT
Requires: identify-bin = %{version}-%{release}
Requires: identify-license = %{version}-%{release}
Requires: identify-python = %{version}-%{release}
Requires: identify-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
========

%package bin
Summary: bin components for the identify package.
Group: Binaries
Requires: identify-license = %{version}-%{release}

%description bin
bin components for the identify package.


%package license
Summary: license components for the identify package.
Group: Default

%description license
license components for the identify package.


%package python
Summary: python components for the identify package.
Group: Default
Requires: identify-python3 = %{version}-%{release}

%description python
python components for the identify package.


%package python3
Summary: python3 components for the identify package.
Group: Default
Requires: python3-core
Provides: pypi(identify)

%description python3
python3 components for the identify package.


%prep
%setup -q -n identify-2.2.12
cd %{_builddir}/identify-2.2.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1628090054
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/identify
cp %{_builddir}/identify-2.2.12/LICENSE %{buildroot}/usr/share/package-licenses/identify/428ea02ecbdb18e260e938e24a83f8d96b7def89
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/identify-cli

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/identify/428ea02ecbdb18e260e938e24a83f8d96b7def89

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
