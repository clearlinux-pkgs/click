#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : click
Version  : 7.1.1
Release  : 25
URL      : https://files.pythonhosted.org/packages/4e/ab/5d6bc3b697154018ef196f5b17d958fac3854e2efbc39ea07a284d4a6a9b/click-7.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/4e/ab/5d6bc3b697154018ef196f5b17d958fac3854e2efbc39ea07a284d4a6a9b/click-7.1.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/4e/ab/5d6bc3b697154018ef196f5b17d958fac3854e2efbc39ea07a284d4a6a9b/click-7.1.1.tar.gz.asc
Summary  : Click CLI for Kubernetes
Group    : Development/Tools
License  : BSD-3-Clause
Requires: click-license = %{version}-%{release}
Requires: click-python = %{version}-%{release}
Requires: click-python3 = %{version}-%{release}
Requires: Pillow
Requires: click
Requires: colorama
BuildRequires : Pillow
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : colorama
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
$ repo_
repo is a simple example of an application that looks
and works similar to hg or git.

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
%setup -q -n click-7.1.1
cd %{_builddir}/click-7.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583845542
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/click
cp %{_builddir}/click-7.1.1/LICENSE.rst %{buildroot}/usr/share/package-licenses/click/6fb11e02ffe0f79b74f1c6034b4ae6e7717a69f8
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
