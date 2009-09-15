%define        svn   1023096
%define        oname kbluetooth4

Name:          kbluetooth
Summary:       Access and control bluetooth devices in KDE4
Version:       0.4
Epoch:         1
Release:       %mkrel 0.%svn.2
Source:        http://downloads.sourceforge.net/kde-bluetooth/%{name}-%{version}.%svn.tar.bz2
URL:           http://bluetooth.kmobiletools.org/
License:       GPLv2+
Group:         System/Configuration/Hardware
BuildRoot:     %{_tmppath}/%{name}-buildroot
BuildRequires: kdebase4-workspace-devel >= 2:4.2.0
Provides:      bluez-pin
Requires:      bluez >= 4.28 
Requires:      bluez-sdp
Obsoletes:     kbluetooth4 < 0.1-1
Obsoletes:     kdebluetooth4 < 0.4-0.1023096.2
Obsoletes:     %{_lib}kdebluetooth0 < 1:1.0-0.beta8.9

%description
The aim of this project is a tight and easy to use integration of Bluetooth
into the KDE4 desktop. You can manage your local Bluetooth devices and services
with it, browse your Bluetooth neighbourhood with konqueror and send and
receive files with just a few clicks. And that's not all you can do with it...

%files
%defattr(-,root,root)
%{_kde_bindir}/kbluetooth
%{_kde_bindir}/kbluetooth-inputwizard
%{_kde_bindir}/kbluetooth-devicemanager
%{_kde_datadir}/applications/kde4/kbluetooth.desktop
%{_kde_iconsdir}/hicolor/*/apps/*.png

#--------------------------------------------------------------------------

%prep
%setup -q -n %oname

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %buildroot
