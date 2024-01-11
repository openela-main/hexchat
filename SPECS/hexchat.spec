%global app_id io.github.Hexchat

Summary:   A popular and easy to use graphical IRC (chat) client
Name:      hexchat
Version:   2.16.0
Release:   1%{?dist}
License:   GPLv2+
URL:       https://hexchat.github.io
Source:    https://dl.hexchat.net/hexchat/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: meson
BuildRequires: hicolor-icon-theme
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
BuildRequires: pkgconfig(dbus-glib-1)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(iso-codes)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(libpci)
BuildRequires: pkgconfig(lua)
BuildRequires: perl-devel, perl-ExtUtils-Embed
BuildRequires: python3-cffi
Requires:      python3-cffi
Requires:      (enchant or enchant2)
Recommends:    sound-theme-freedesktop

%description
HexChat is an easy to use graphical IRC chat client for the X Window System.
It allows you to join multiple IRC channels (chat rooms) at the same time, 
talk publicly, private one-on-one conversations etc. Even file transfers
are possible.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the development files for %{name}.

%prep
%autosetup -p1

%build
%meson -Dwith-lua=lua
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/hexchat
%license COPYING
%doc readme.md
%dir %{_libdir}/hexchat
%dir %{_libdir}/hexchat/plugins
%{_libdir}/hexchat/plugins/checksum.so
%{_libdir}/hexchat/plugins/fishlim.so
%{_libdir}/hexchat/plugins/lua.so
%{_libdir}/hexchat/plugins/sysinfo.so
%{_libdir}/hexchat/plugins/perl.so
%{_libdir}/hexchat/plugins/python.so
%{_libdir}/hexchat/python
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/metainfo/%{app_id}.appdata.xml
%{_datadir}/dbus-1/services/org.hexchat.service.service
%{_mandir}/man1/*.gz

%files devel
%{_includedir}/hexchat-plugin.h
%{_libdir}/pkgconfig/hexchat-plugin.pc

%changelog
* Mon Dec 13 2021 Debarshi Ray <rishi@fedoraproject.org> - 2.16.0-1
- Update to 2.16.0
Resolves: #1965883

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.14.3-17
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Wed Jul 28 2021 Florian Weimer <fweimer@redhat.com> - 2.14.3-16
- Rebuild to pick up OpenSSL 3.0 Beta ABI (#1984097)

* Mon Jul 12 2021 Debarshi Ray <rishi@fedoraproject.org> - 2.14.3-15
- Avoid direct use of libproxy
Resolves: #1981509

* Wed Jun 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.14.3-14
- Rebuilt for RHEL 9 BETA for openssl 3.0
  Related: rhbz#1971065

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 2.14.3-13
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Fri Mar 12 2021 Kevin Fenzi <kevin@scrye.com> - 2.14.3-12
- Add patch to fix exception in python3 plugin.

* Sat Feb 06 2021 Mikel Olasagasti Uranga <mikel@olasagasti.info> - 2.14.3-11
- Include patch to fix underscore not being printed correctly

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 15 2021 Kevin Fenzi <kevin@scrye.com> - 2.14.3-9
- Fix typo in last commit

* Fri Jan 15 2021 Kevin Fenzi <kevin@scrye.com> - 2.14.3-8
- Add missing dependency on cffi. Fixes rhbz#1914874

* Wed Dec 30 2020 Kevin Fenzi <kevin@scrye.com> - 2.14.3-7
- Backport new python plugin from devel upstream. RHBZ#1883982

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 2.14.3-5
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.14.3-4
- Rebuilt for Python 3.9

* Fri Mar 27 2020 Kevin Fenzi <kevin@scrye.com> - 2.14.3-3
- Add patch to link better against python3.8. Fixes #1817862

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Kevin Fenzi <kevin@scrye.com> - 2.14.3-1
- Update to 2.14.3.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.14.2-6
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.14.2-4
- Perl 5.30 rebuild

* Tue Apr 30 2019 Adam Williamson <awilliam@redhat.com> - 2.14.2-3
- Apply a fix suggested by ncoghlan for the crash-on-exit bug (#1632039)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Sep 06 2018 Gwyn Ciesla <limburgher@gmail.com> - 2.14.2-1
- 2.14.2

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.14.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Petr Pisar <ppisar@redhat.com> - 2.14.1-5
- Perl 5.28 rebuild

* Mon Jul 02 2018 Kevin Fenzi <kevin@scrye.com> - 2.14.1-4
- Rebuild for python 3.7

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.14.1-3
- Perl 5.28 rebuild

* Wed Mar 21 2018 Patrick Griffis <tingping@fedoraproject.org> 2.14.1-2
- Always use lua over luajit, just more common
- Remove no longer needed snippets
- Add enchant/enchant2 to requires

* Wed Mar 14 2018 Patrick Griffis <tingping@fedoraproject.org> 2.14.1-1
- Version bump to 2.14.1

* Sat Mar 10 2018 Patrick Griffis <tingping@fedoraproject.org> 2.14.0-1
- Version bump to 2.14.0

* Thu Feb 08 2018 Patrick Griffis <tingping@fedoraproject.org> 2.12.4-11
- Add patch fixing rendering issue: https://bugzilla.redhat.com/show_bug.cgi?id=1536298

* Tue Feb  6 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2.12.4-10
- Disable luajit on aarch64 due to crashes

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 2.12.4-9
- Rebuilt for switch to libxcrypt

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 11 2017 Kevin Fenzi <kevin@scrye.com> - 2.12.4-6
- Add patch for python LC_ALL / LANGUAGES. 
- https://github.com/hexchat/hexchat/issues/2013

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.12.4-5
- Perl 5.26 rebuild

* Sun Mar 12 2017 Peter Robinson <pbrobinson@fedoraproject.org> 2.12.4-4
- Explicitly require openssl-devel so we build against 1.1

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.12.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.12.4-2
- Rebuild for Python 3.6

* Sat Dec 10 2016 Patrick Griffis <tingping@tingping.se> - 2.12.4-1
- Version bump to 2.12.4

* Sat Oct 22 2016 Patrick Griffis <tingping@tingping.se> - 2.12.3-1
- Version bump to 2.12.3
- Fix building against OpenSSL 1.1.0

* Sun Oct 9 2016 Dan Horák <dan[at]danny.cz> - 2.12.2-2
- Not all arches have luajit

* Sat Oct 8 2016 Patrick Griffis <tingping@tingping.se> - 2.12.2-1
- Version bump to 2.12.2

* Sat Oct 8 2016 Patrick Griffis <tingping@tingping.se> - 2.12.1-7
- Modernize spec file

* Mon Sep 19 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.12.1-6
- aarch64 now has LuaJIT

* Mon Aug 29 2016 Igor Gnatenko <ignatenko@redhat.com> - 2.12.1-5
- Rebuild for LuaJIT 2.1.0

* Tue Jul 5 2016 TingPing <tingping@tingping.se> - 2.12.1-4
- Fix input style theming with Adwaita

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.12.1-3
- Perl 5.24 rebuild

* Tue May  3 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.12.1-2
- Not all arches have luajit

* Sun May 1 2016 TingPing <tingping@tingping.se> - 2.12.1-1
- Version bump to 2.12.1

* Sat Mar 12 2016 TingPing <tingping@tingping.se> - 2.12.0-1
- Version bump to 2.12.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Kevin Fenzi <kevin@scrye.com> - 2.10.2-6
- Build against python 3.5 specifically.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.2-3
- Perl 5.22 rebuild

* Fri Jan 30 2015 TingPing <tingping@tingping.se> - 2.10.2-2
- Do not own icon directories owned by hicolor-icon-theme (#1171904)
- Build against python3
- Make use of license macro

* Tue Nov 25 2014 TingPing <tingping@tingping.se> - 2.10.2-1
- Version bump to 2.10.2

* Thu Aug 28 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.10.1-3
- Perl 5.20 rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 TingPing <tingping@tingping.se> - 2.10.1-1
- Version bump to 2.10.1

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 2 2014 TingPing <tingping@tingping.se> - 2.10.0-1
- Version bump to 2.10.0

* Mon Sep 16 2013 TingPing <tingping@tingping.se> - 2.9.6.1-1
- Version bump to 2.9.6.1

* Wed Sep 11 2013 TingPing <tingping@tingping.se> - 2.9.6-1
- Version bump to 2.9.6

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Aug 03 2013 Kevin Fenzi <kevin@scrye.com> 2.9.5-2
- Rebuild for new perl

* Mon Apr 1 2013 TingPing <tingping@tingping.se> - 2.9.5-1
- Version bump to 2.9.5

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 27 2012 TingPing <tingping@tingping.se> - 2.9.4-1
- Initial HexChat package
