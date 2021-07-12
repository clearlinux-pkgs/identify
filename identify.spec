#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : identify
Version  : 2.2.11
Release  : 3
URL      : https://files.pythonhosted.org/packages/aa/f0/ee1620c2958b089ec9c5c53e1e8921504a3412a3c1d453b55c7533468223/identify-2.2.11.tar.gz
Source0  : https://files.pythonhosted.org/packages/aa/f0/ee1620c2958b089ec9c5c53e1e8921504a3412a3c1d453b55c7533468223/identify-2.2.11.tar.gz
Summary  : File identification library for Python
Group    : Development/Tools
License  : MIT MPL-2.0
Requires: identify-bin = %{version}-%{release}
Requires: identify-license = %{version}-%{release}
Requires: identify-python = %{version}-%{release}
Requires: identify-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
identify
========
[![Build Status](https://dev.azure.com/asottile/asottile/_apis/build/status/pre-commit.identify?branchName=master)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=67&branchName=master)
[![Azure DevOps coverage](https://img.shields.io/azure-devops/coverage/asottile/asottile/67/master.svg)](https://dev.azure.com/asottile/asottile/_build/latest?definitionId=67&branchName=master)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/pre-commit/identify/master.svg)](https://results.pre-commit.ci/latest/github/pre-commit/identify/master)
[![PyPI version](https://badge.fury.io/py/identify.svg)](https://pypi.python.org/pypi/identify)

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
%setup -q -n identify-2.2.11
cd %{_builddir}/identify-2.2.11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626102992
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/identify
cp %{_builddir}/identify-2.2.11/LICENSE %{buildroot}/usr/share/package-licenses/identify/428ea02ecbdb18e260e938e24a83f8d96b7def89
cp %{_builddir}/identify-2.2.11/identify/vendor/licenses.py %{buildroot}/usr/share/package-licenses/identify/444355b83c38f8d89113709114738ceebb15c4ec
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
/usr/share/package-licenses/identify/444355b83c38f8d89113709114738ceebb15c4ec

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
