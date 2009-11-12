%define betaver RC1
%define svn    1046792

Name:          kbluetooth
Summary:       Access and control bluetooth devices in KDE4
Version:       0.4
Epoch:         1
Release:       %mkrel 1.%betaver.5
Source:        http://www.kde-apps.org/CONTENT/content-files/%name-%version.%svn.tar.bz2
URL:           http://techbase.kde.org/Kbluetooth
License:       GPLv2+
Group:         System/Configuration/Hardware
BuildRoot:     %{_tmppath}/%{name}-buildroot
BuildRequires: kdebase4-workspace-devel >= 2:4.2.0
Provides:      bluez-pin
Requires:      bluez >= 4.28 
Requires:      bluez-sdp
Obsoletes:     kbluetooth4 < 0.1-1
Provides:      kbluetooth4 = %epoch:%version-%release
Obsoletes:     kdebluetooth4 < 1:0.4-0.1023096.2
Provides:      kdebluetooth4 = %epoch:%version-%release
Obsoletes:     kdebluetooth  = 1:1.0-0.beta8.8
Provides:      kdebluetooth = %epoch:%version-%release
Obsoletes:     %{_lib}kdebluetooth0 < 1:1.0-0.beta8.9

%description
The aim of this project is a tight and easy to use integration of Bluetooth
into the KDE4 desktop. You can manage your local Bluetooth devices and services
with it, browse your Bluetooth neighbourhood with konqueror and send and
receive files with just a few clicks. And that's not all you can do with it...

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/kbluetooth
%{_kde_bindir}/kbluetooth-inputwizard
%{_kde_bindir}/kbluetooth-devicemanager
%{_kde_datadir}/applications/kde4/kbluetooth.desktop
%{_kde_iconsdir}/hicolor/*/apps/*.png

#--------------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%find_lang %name

%clean
rm -rf %buildroot
