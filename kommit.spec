Name:           kommit
Version:        1.3.1
Release:        1
Summary:        Graphical Git Client
License:        GPL-3.0-only
URL:            https://apps.kde.org/kommit
# Looks like kde source for kommit is not updated
#Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source0:        https://invent.kde.org/sdk/kommit/-/archive/v%{version}/kommit-v%{version}.tar.bz2

BuildRequires:  appstream
BuildRequires:  cmake(Qt6)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(ecm)
BuildRequires:  cmake
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(DolphinVcs) >= 24.01.80
BuildRequires:  pkgconfig(libgit2)
BuildRequires:	qt6-qtbase-theme-gtk3

%description
Graphical Git Client

%prep
%autosetup -n %{name}-v%{version} -p1

%cmake \
        -DBUILD_WITH_QT6:BOOL=ON \
        -G Ninja

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%{_bindir}/kommit*
%{_libdir}/libkommit*
%{_datadir}/applications/org.kde.kommit.desktop
%{_datadir}/applications/org.kde.kommit.diff.desktop
%{_datadir}/applications/org.kde.kommit.merge.desktop
%{_iconsdir}/hicolor/*x*/apps/kommit.png
%{_iconsdir}/hicolor/scalable/apps/kommit.svg
%{_iconsdir}/hicolor/scalable/actions/*
%{_datadir}/metainfo/org.kde.kommit.appdata.xml
%{_libdir}/lib64/plugins/dolphin/vcs/kommitdolphinplugin.so
%{_datadir}/qlogging-categories6/kommit.categories
%doc %{_datadir}/doc/HTML/*/kommit/*
