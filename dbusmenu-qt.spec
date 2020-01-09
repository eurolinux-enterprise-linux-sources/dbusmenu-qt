
Summary: A Qt implementation of the DBusMenu protocol 
Name:    dbusmenu-qt
Version: 0.9.2
Release: 7%{?dist}

Group: System Environment/Libraries
License: LGPLv2+
URL: https://launchpad.net/libdbusmenu-qt/
Source0  https://launchpad.net/libdbusmenu-qt/trunk/%{version}/+download/libdbusmenu-qt-%{version}.tar.bz2
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

## upstream patches

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: pkgconfig
BuildRequires: pkgconfig(QJson)
BuildRequires: pkgconfig(QtDBus) pkgconfig(QtGui) 
# test-suite
BuildRequires: xorg-x11-server-Xvfb dbus-x11

Provides: libdbusmenu-qt = %{version}-%{release}

%description
This library provides a Qt implementation of the DBusMenu protocol.

The DBusMenu protocol makes it possible for applications to export and import
their menus over DBus.


%package devel
Summary: Development files for %{name}
Group:   Development/Libraries
Provides: libdbusmenu-devel = %{version}-%{release}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package devel-docs
Summary: API documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description devel-docs
%{summary}.


%prep
%setup -q -n libdbusmenu-qt-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake} .. 
popd

make %{?_smp_mflags} -C %{_target_platform}


%install
rm -rf %{buildroot}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# unpackaged files
rm -rf %{buildroot}%{_docdir}/dbusmenu-qt


%check
# verify pkg-config version
export PKG_CONFIG_PATH=%{buildroot}%{_datadir}/pkgconfig:%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion dbusmenu-qt)" = "%{version}"
# test suite
xvfb-run dbus-launch make -C %{_target_platform} check ||:


%clean
rm -rf %{buildroot} 


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README
%{_libdir}/libdbusmenu-qt.so.2*

%files devel
%defattr(-,root,root,-)
%{_includedir}/dbusmenu-qt/
%{_libdir}/libdbusmenu-qt.so
%{_libdir}/pkgconfig/dbusmenu-qt.pc

%files devel-docs
%defattr(-,root,root,-)
%doc %{_target_platform}/html/

%changelog
* Tue Mar 18 2014 Lukáš Tinkl <ltinkl@redhat.com> - 0.9.2-7
- Resolves rhbz#1076410 - dbusmenu-qt has multilib conflicts

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.9.2-6
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.9.2-5
- Mass rebuild 2013-12-27

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 08 2012 Than Ngo <than@redhat.com> - 0.9.2-3
- fix url

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 30 2012 Rex Dieter <rdieter@fedoraproject.org> 0.9.2-1
- 0.9.2

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 27 2011 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-2
- fix %%check

* Sat Oct 01 2011 Rex Dieter <rdieter@fedoraproject.org> 0.9.0-1
- 0.9.0
- pkgconfig-style deps

* Thu Jun 16 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.2-2
- rebuild

* Fri May 20 2011 Rex Dieter <rdieter@fedoraproject.org> 0.8.2-1
- 0.8.2

* Fri May 20 2011 Rex Dieter <rdieter@fedoraproject.org> 0.6.6-1
- 0.6.6

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 29 2010 jkeating - 0.6.3-2
- Rebuilt for gcc bug 634757

* Tue Sep 21 2010 Rex Dieter <rdieter@fedoraproject.org> 0.6.3-1
- dbusmenu-qt-0.6.3
- include kubuntu_00_external_contributions.diff 

* Fri Aug 06 2010 Rex Dieter <rdieter@fedoraproject.org> 0.5.2-1
- dbusmenu-qt-0.5.2

* Fri May 21 2010 Rex Dieter <rdieter@fedoraproject.org> 0.3.3-1
- dbusmenu-qt-0.3.3

* Sun Apr 25 2010 Rex Dieter <rdieter@fedoraproject.org> 0.3.2-2
- pkg rename s/libdbusmenu-qt/dbusmenu-qt/
- Provides: libdbusmenu-qt(-devel)

* Sun Apr 25 2010 Rex Dieter <rdieter@fedoraproject.org> 0.3.2-1
- dbusmenu-qt-0.3.2

