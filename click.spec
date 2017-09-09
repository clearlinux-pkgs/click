#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : click
Version  : 6.7
Release  : 2
URL      : http://pypi.debian.net/click/click-6.7.tar.gz
Source0  : http://pypi.debian.net/click/click-6.7.tar.gz
Summary  : A simple wrapper around optparse for powerful command line utilities.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: click-legacypython
Requires: click-python
Requires: click
Requires: colorama
BuildRequires : colorama
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
$ click_
Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit".  It's highly configurable but comes with
sensible defaults out of the box.

%package legacypython
Summary: legacypython components for the click package.
Group: Default

%description legacypython
legacypython components for the click package.


%package python
Summary: python components for the click package.
Group: Default
Requires: click-legacypython

%description python
python components for the click package.


%prep
%setup -q -n click-6.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1505000133
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1505000133
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)
/usr/lib/python3*/*
