Name:           kommit
Version:        1.3.1
Release:        1
Summary:        Graphical Git Client
License:        GPL-3.0-only
URL:            https://apps.kde.org/kommit
# Looks like kde source for kommit is not updated
#Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
Source0:        https://invent.kde.org/sdk/kommit/-/archive/v%{version}/kommit-v%{version}.tar.bz2

BuildRequires:  cmake(ecm)
BuildRequires:  cmake
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  pkgconfig(libgit2)

%description
Graphical Git Client

%prep
%autosetup -n %{name}-v%{version} -p1

%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang %{name} --with-man --all-name

%files -f %{name}.lang
%{_bindir}/kommit*
%{_libdir}/libkommit*
%{_libdir}/qt5/plugins/kf5/kfileitemaction/kommititemaction.so
%{_libdir}/qt5/plugins/kf5/overlayicon/kommitoverlayplugin.so
%{_datadir}/applications/org.kde.kommit.desktop
%{_datadir}/applications/org.kde.kommit.diff.desktop
%{_datadir}/applications/org.kde.kommit.merge.desktop
%{_iconsdir}/hicolor/*x*/apps/kommit.png
%{_iconsdir}/hicolor/scalable/apps/kommit.svg
%{_iconsdir}/hicolor/scalable/actions/*
%{_datadir}/metainfo/org.kde.kommit.appdata.xml
%{_datadir}/qlogging-categories5/kommit.categories
%doc %{_datadir}/doc/HTML/*/kommit/*
