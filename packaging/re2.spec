#
# spec file for package python-compizconfig
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Intel Corporation.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           re2
Version:        20130115
Release:        1
License:        BSD-3-Clause
Summary:        An efficient, principled regular expression library
Url:            http://code.google.com/p/re2/
Group:          System/Libraries
Source:         re2-%{version}.tgz
BuildRequires:  gcc-c++

%description
RE2 is a fast, safe, thread-friendly alternative to backtracking
regular expression engines like those used in PCRE, Perl, and
Python. It is a C++ library.


%package -n libre2
License:        BSD-3-Clause
Summary:        An efficient, principled regular expression library
Group:          System/Libraries

%description -n libre2
RE2 is a fast, safe, thread-friendly alternative to backtracking
regular expression engines like those used in PCRE, Perl, and
Python. It is a C++ library.


%package devel
License:        BSD-3-Clause
Summary:        An efficient, principled regular expression library
Group:          System/Libraries
Requires:       libre2 = %{version}

%description devel
RE2 is a fast, safe, thread-friendly alternative to backtracking
regular expression engines like those used in PCRE, Perl, and
Python. It is a C++ library.


%prep
%setup -q -n re2

%build
make %{?_smp_mflags} CXXFLAGS="$RPM_OPT_FLAGS -Wall -pthread" libdir=%{_libdir} prefix=%{_prefix}

%install
make DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir} prefix=%{_prefix} install
rm $RPM_BUILD_ROOT%{_libdir}/libre2.a


%post   -n libre2 -p /sbin/ldconfig

%postun -n libre2 -p /sbin/ldconfig


%files -n libre2
%defattr(-, root, root, -)
%license LICENSE
%doc AUTHORS README
%{_libdir}/libre2.so.0
%{_libdir}/libre2.so.0.0.0


%files devel
%defattr(-, root, root, -)
%{_includedir}/re2
%{_libdir}/libre2.so