%define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")

Summary: Ugly Plugins for the Elisa Media Center
Name: elisa-plugins-ugly
Version: 0.3.5
Release: 4%{?dist}
License: GPLv3
Group: Applications/Multimedia
URL: http://elisa.fluendo.com/
Source: http://elisa.fluendo.com/static/download/elisa/elisa-plugins-ugly-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
# For the parent directories
Requires: elisa >= 0.3.5
Requires: elisa-plugins-good >= 0.3.5
Requires: elisa-plugins-bad >= 0.3.5
# For some "ugly" formats
Requires: gstreamer-plugins-ugly
# youtube
Requires: python-gdata
# flickr (package not yet available)
#Requires: python-twill

BuildRequires: elisa >= 0.3.5
BuildRequires: python-devel
BuildArch: noarch

%description
This package contains the ugly set of plugins for the Elisa Media Center.


%prep
%setup -q


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install \
    --single-version-externally-managed \
    -O1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc PKG-INFO
%{python_sitelib}/elisa/plugins/*
# These are already provided by elisa-plugins-good, which we require.
%exclude %{python_sitelib}/elisa/plugins/__init__.py*
%{python_sitelib}/elisa_plugins_ugly-*.egg-info/
%{python_sitelib}/elisa_plugins_ugly-*-nspkg.pth


%changelog
* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.3.5-4
- rebuild for new F11 features

* Sun Oct 19 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.3.5-3
- rebuild for RPM Fusion

* Sun Mar 16 2008 Matthias Saou <http://freshrpms.net/> 0.3.5-2
- Remove pyxdg requirement from xmlmenu, as it's not in this package.

* Sun Mar 16 2008 Matthias Saou <http://freshrpms.net/> 0.3.5-1
- Initial RPM release.

