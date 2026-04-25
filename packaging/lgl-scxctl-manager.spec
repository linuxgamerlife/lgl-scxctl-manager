Name:           lgl-scxctl-manager
Version:        1.0.1
Release:        1%{?dist}
Summary:        Qt6 GUI for managing sched-ext BPF schedulers via scxctl

License:        MIT
URL:            https://github.com/linuxgamerlife/lgl-scxctl-manager
Source0:        https://github.com/linuxgamerlife/%{name}/archive/refs/tags/v%{version}.zip
BuildRequires:  cmake >= 3.16
BuildRequires:  unzip
BuildRequires:  gcc-c++
BuildRequires:  qt6-qtbase-devel
Requires:       qt6-qtbase
Requires:       polkit
# scx-tools is detected at runtime — the app shows a setup guide if absent
Recommends:     scx-tools
Recommends:     scx-scheds

%description
SCX Scheduler Manager is a Qt6 graphical interface for managing sched-ext
BPF schedulers through the scxctl command-line tool.

It allows starting, stopping, and switching schedulers, viewing live
scheduler status, managing scx_loader.service autostart, and browsing
per-scheduler flags and workload reference data.

If scxctl is not installed, the application opens in setup mode and
displays installation guidance without hard-failing.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir -p build
cd build
cmake .. \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build

%install
# Main binary
install -Dm755 build/lgl-scxctl-manager \
    %{buildroot}%{_bindir}/lgl-scxctl-manager

# Desktop entry
install -Dm644 lgl-scxctl-manager.desktop \
    %{buildroot}%{_datadir}/applications/lgl-scxctl-manager.desktop

# Icon
install -Dm644 packaging/lgl-scxctl-manager_icon.png \
    %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/lgl-scxctl-manager.png

# Pixmaps fallback
install -Dm644 packaging/lgl-scxctl-manager_icon.png \
    %{buildroot}%{_datadir}/pixmaps/lgl-scxctl-manager.png

# AppStream metainfo
install -Dm644 packaging/com.linuxgamerlife.lgl-scxctl-manager.metainfo.xml \
    %{buildroot}%{_datadir}/metainfo/com.linuxgamerlife.lgl-scxctl-manager.metainfo.xml

%post
if [ -x /usr/bin/gtk-update-icon-cache ]; then
    gtk-update-icon-cache -f -t %{_datadir}/icons/hicolor &>/dev/null || :
fi
if [ -x /usr/bin/update-desktop-database ]; then
    update-desktop-database -q %{_datadir}/applications &>/dev/null || :
fi
if [ -x /usr/bin/appstreamcli ]; then
    appstreamcli refresh --force &>/dev/null || :
fi
if [ -x /usr/bin/kbuildsycoca6 ]; then
    kbuildsycoca6 &>/dev/null || :
fi

%postun
if [ -x /usr/bin/gtk-update-icon-cache ]; then
    gtk-update-icon-cache -f -t %{_datadir}/icons/hicolor &>/dev/null || :
fi
if [ -x /usr/bin/update-desktop-database ]; then
    update-desktop-database -q %{_datadir}/applications &>/dev/null || :
fi
if [ -x /usr/bin/appstreamcli ]; then
    appstreamcli refresh --force &>/dev/null || :
fi

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/lgl-scxctl-manager
%{_datadir}/applications/lgl-scxctl-manager.desktop
%{_datadir}/icons/hicolor/256x256/apps/lgl-scxctl-manager.png
%{_datadir}/pixmaps/lgl-scxctl-manager.png
%{_datadir}/metainfo/com.linuxgamerlife.lgl-scxctl-manager.metainfo.xml

%changelog
* Fri Apr 25 2026 LinuxGamerLife <contact@linuxgamerlife.com> - 1.0.1-1
- Closing the main window now minimises to system tray instead of quitting

* Mon Mar 23 2026 LinuxGamerLife <contact@linuxgamerlife.com> - 1.0.0-1
- Initial release
