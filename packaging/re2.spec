#
# spec file for package python-compizconfig
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           re2
%define lname	libre2-0
Version:        20130115
Release:        1
License:        BSD-3-Clause
Summary:        An efficient, principled regular expression library
Url:            http://code.google.com/p/re2/
Group:          Development/Libraries/C and C++
Source:         re2-%{version}.tgz
BuildRequires:  gcc-c++

%description
RE2 is a fast, safe, thread-friendly alternative to backtracking
regular expression engines like those used in PCRE, Perl, and
Python. It is a C++ library.


%package -n %lname
License:        BSD-3-Clause
Summary:        An efficient, principled regular expression library
Group:          Development/Libraries/C and C++

%description -n %lname
RE2 is a fast, safe, thread-friendly alternative to backtracking
regular expression engines like those used in PCRE, Perl, and
Python. It is a C++ library.


%package devel
License:        BSD-3-Clause
Summary:        An efficient, principled regular expression library
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
RE2 is a fast, safe, thread-friendly alternative to backtracking
regular expression engines like those used in PCRE, Perl, and
Python. It is a C++ library.


%prep
%setup -q -n re2

%build
make %{?_smp_mflags} CXXFLAGS="$RPM_OPT_FLAGS -Wall -pthread" libdir=%{_libdir} prefix=%{_prefix}

make DESTDIR=$RPM_BUILD_ROOT libdir=%{_libdir} prefix=%{_prefix} install
rm $RPM_BUILD_ROOT%{_libdir}/libre2.a


%post   -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig


%files -n %lname
%defattr(-, root, root, -)
%doc AUTHORS LICENSE README
%{_libdir}/libre2.so.0
%{_libdir}/libre2.so.0.0.0


%files devel
%defattr(-, root, root, -)
%{_includedir}/re2
%{_libdir}/libre2.so