%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: Ugly Plugins for the Elisa Media Center
Name: elisa-plugins-ugly
Version: 0.5.35
Release: 1%{?dist}
License: GPLv3
Group: Applications/Multimedia
URL: http://elisa.fluendo.com/
Source: http://elisa.fluendo.com/static/download/elisa/elisa-plugins-ugly-%{version}.tar.gz
Patch0: elisa-plugins-ugly-0.5.2-install.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# For the parent directories
Requires: elisa >= %{version}
# For some "ugly" formats
Requires: gstreamer-plugins-ugly

# Plugin requirements, in order, only once each
# flickr
Requires: python-twill
Requires: python-twisted-web2
# lirc
# shoutcast
#Requires: python-twisted-web2
# youtube
#Requires: python-twisted-web2

BuildRequires: elisa-base = %{version}
BuildRequires: python-devel
BuildArch: noarch

%description
This package contains the ugly set of plugins for the Elisa Media Center,
plugins which might present licensing or other similar issues.


%prep
%setup -q
%patch0 -p1


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{python_sitelib}/elisa/plugins/flickr/
%{python_sitelib}/elisa/plugins/lirc/
%{python_sitelib}/elisa/plugins/shoutcast/
%{python_sitelib}/elisa/plugins/youtube/
%{python_sitelib}/elisa_plugin_*


%changelog
* Wed Apr 15 2009 Matthias Saou <http://freshrpms.net/> 0.5.35-1
- Update to 0.5.35.
- Drop the useless --single-version-externally-managed option.

* Tue Mar  3 2009 Matthias Saou <http://freshrpms.net/> 0.5.30-1
- Update to 0.5.30.

* Sat Feb 28 2009 Matthias Saou <http://freshrpms.net/> 0.5.29-1
- Update to 0.5.29.

* Tue Feb 17 2009 Matthias Saou <http://freshrpms.net/> 0.5.28-1
- Update to 0.5.28.

* Fri Feb 13 2009 Matthias Saou <http://freshrpms.net/> 0.5.27-1
- Update to 0.5.27.

* Sat Feb  7 2009 Matthias Saou <http://freshrpms.net/> 0.5.26-1
- Update to 0.5.26.

* Mon Jan 26 2009 Matthias Saou <http://freshrpms.net/> 0.5.24.1-1
- Update to 0.5.24.1.

* Mon Jan 12 2009 Matthias Saou <http://freshrpms.net/> 0.5.23-1
- Update to 0.5.23.

* Thu Dec 18 2008 Matthias Saou <http://freshrpms.net/> 0.5.22-1
- Update to 0.5.22.

* Mon Dec  1 2008 Matthias Saou <http://freshrpms.net/> 0.5.20-1
- Update to 0.5.20.

* Mon Nov 24 2008 Matthias Saou <http://freshrpms.net/> 0.5.19-1
- Update to 0.5.19.

* Mon Nov 17 2008 Matthias Saou <http://freshrpms.net/> 0.5.18-1
- Update to 0.5.18.

* Tue Nov  4 2008 Matthias Saou <http://freshrpms.net/> 0.5.17-1
- Update to 0.5.17.

* Mon Oct 27 2008 Matthias Saou <http://freshrpms.net/> 0.5.16-1
- Update to 0.5.16.

* Tue Oct 21 2008 Matthias Saou <http://freshrpms.net/> 0.5.15-1
- Update to 0.5.15.
- Add new python-twill requirement for the flickr plugin.

* Mon Oct 13 2008 Matthias Saou <http://freshrpms.net/> 0.5.14-1
- Update to 0.5.14.

* Fri Oct 10 2008 Matthias Saou <http://freshrpms.net/> 0.5.13-2
- Build require elisa-base from now on.
- Update description to explain what "ugly" plugins are.

* Tue Oct  7 2008 Matthias Saou <http://freshrpms.net/> 0.5.13-1
- Update to 0.5.13.

* Tue Sep 30 2008 Matthias Saou <http://freshrpms.net/> 0.5.12-1
- Update to 0.5.12.

* Tue Sep 23 2008 Matthias Saou <http://freshrpms.net/> 0.5.11-1
- Update to 0.5.11.

* Tue Sep 16 2008 Matthias Saou <http://freshrpms.net/> 0.5.10-1
- Update to 0.5.10.

* Tue Sep  9 2008 Matthias Saou <http://freshrpms.net/> 0.5.9-1
- Update to 0.5.9.

* Mon Sep  2 2008 Matthias Saou <http://freshrpms.net/> 0.5.8-1
- Update to 0.5.8.

* Tue Aug 26 2008 Matthias Saou <http://freshrpms.net/> 0.5.7-1
- Update to 0.5.7.

* Tue Aug 19 2008 Matthias Saou <http://freshrpms.net/> 0.5.6-1
- Update to 0.5.6.
- Require the exact same elisa version, as elisa and all plugins are always
  released all at once and should always match.

* Mon Aug 11 2008 Matthias Saou <http://freshrpms.net/> 0.5.5-1
- Update to 0.5.5.

* Fri Aug  8 2008 Matthias Saou <http://freshrpms.net/> 0.5.4-1
- Update to 0.5.4.

* Tue Jul 29 2008 Matthias Saou <http://freshrpms.net/> 0.5.3-1
- Update to 0.5.3.

* Wed Jul 23 2008 Matthias Saou <http://freshrpms.net/> 0.5.2-3
- Update to 0.5.2.
- Update the build patch which is still required.
- Now build require the elisa-devel package.
- Update requirements.

* Tue Jul 15 2008 Matthias Saou <http://freshrpms.net/> 0.5.1-1
- Update to 0.5.1.

* Sun Mar 16 2008 Matthias Saou <http://freshrpms.net/> 0.3.5-2
- Remove pyxdg requirement from xmlmenu, as it's not in this package.

* Sun Mar 16 2008 Matthias Saou <http://freshrpms.net/> 0.3.5-1
- Initial RPM release.

