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

%files
