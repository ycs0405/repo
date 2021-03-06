%global project dde-launcher
%global repo %{project}

%global _commit 67081d34b18759c82c1968a6b104173bda8c6540
%global _shortcommit %(c=%{_commit}; echo ${c:0:7})

Name:           deepin-launcher
Version:        4.0.11
Release:        1.git%{_shortcommit}%{?dist}
Summary:        Deepin desktop-environment - Launcher module
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-launcher
Source0:        %{url}/archive/%{_commit}/%{repo}-%{_shortcommit}.tar.gz

BuildRequires:  deepin-tool-kit-devel
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  gtk2-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  xcb-util-wm-devel
Requires:       deepin-menu
Requires:       deepin-daemon
Requires:       startdde
Provides:       %{repo}%{?_isa} = %{version}-%{release}

%description
Deepin desktop-environment - Launcher module

%prep
%setup -q -n %{repo}-%{_commit}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh

%build
%qmake_qt5 PREFIX=%{_prefix} WITHOUT_UNINSTALL_APP=1
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{repo}
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/*.service
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Fri May 19 2017 mosquito <sensor.wen@gmail.com> - 4.0.11-1.git67081d3
- Update to 4.0.11
* Sun Feb 26 2017 mosquito <sensor.wen@gmail.com> - 4.0.7-1.gitf2df6ea
- Update to 4.0.7
* Tue Jan 17 2017 mosquito <sensor.wen@gmail.com> - 4.0.4-1.git8b1a2dd
- Update to 4.0.4
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.3-1
- Updated to version 4.0.3
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.2-1
- Initial package build
