Name:           kommit
Version:        1.0.2
Release:        1
Summary:        Graphical Git Client
License:        GPL-3.0-only
URL:            https://apps.kde.org/kommit
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  cmake(ecm)
BuildRequires:  cmake
BuildRequires:  cmake(KF5Crash)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5DocTools)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(Qt5Test)

%description
Graphical Git Client

%prep
%autosetup -p1

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
%{_iconsdir}/hicolor/scalable/actions/*
%{_datadir}/metainfo/org.kde.kommit.appdata.xml
%{_datadir}/qlogging-categories5/kommit.categories
%doc %{_datadir}/doc/HTML/*/kommit/*
