#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : click
Version  : 8.0.3
Release  : 32
URL      : https://files.pythonhosted.org/packages/f4/09/ad003f1e3428017d1c3da4ccc9547591703ffea548626f47ec74509c5824/click-8.0.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/f4/09/ad003f1e3428017d1c3da4ccc9547591703ffea548626f47ec74509c5824/click-8.0.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/f4/09/ad003f1e3428017d1c3da4ccc9547591703ffea548626f47ec74509c5824/click-8.0.3.tar.gz.asc
Summary  : Composable command line interface toolkit
Group    : Development/Tools
License  : BSD-3-Clause
Requires: click-license = %{version}-%{release}
Requires: click-python = %{version}-%{release}
Requires: click-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
Click Examples
This folder contains various Click examples.  Note that
all of these are not runnable by themselves but should be
installed into a virtualenv.

%package license
Summary: license components for the click package.
Group: Default

%description license
license components for the click package.


%package python
Summary: python components for the click package.
Group: Default
Requires: click-python3 = %{version}-%{release}

%description python
python components for the click package.


%package python3
Summary: python3 components for the click package.
Group: Default
Requires: python3-core
Provides: pypi(click)

%description python3
python3 components for the click package.


%prep
%setup -q -n click-8.0.3
cd %{_builddir}/click-8.0.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633962286
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/click
cp %{_builddir}/click-8.0.3/LICENSE.rst %{buildroot}/usr/share/package-licenses/click/6fb11e02ffe0f79b74f1c6034b4ae6e7717a69f8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/click/6fb11e02ffe0f79b74f1c6034b4ae6e7717a69f8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
