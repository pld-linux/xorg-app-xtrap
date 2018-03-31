Summary:	Sample clients for XTrap X Server Extension
Summary(pl.UTF-8):	Przykładowe programy klienckie do rozszerzenia serwera X XTrap
Name:		xorg-app-xtrap
Version:	1.0.3
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xtrap-%{version}.tar.bz2
# Source0-md5:	ad434adab17ebc9d0a5ece33bbc55beb
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXTrap-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These commands are sample clients provided with the XTrap X Server
Extension, Version 3.3.

XTrap is an X Server extension which facilitates the capturing of
server protocol and synthesizing core input events.

%description -l pl.UTF-8
Polecenia z tego pakietu to przykładowe programy klienckie
udostępnione wraz z rozszerzeniem serwera X XTrap w wersji 3.3.

XTrap to rozszerzenie serwera X ułatwiające przechwytywanie protokołu
serwera i sztuczne wytwarzanie zdarzeń wejściowych.

%prep
%setup -q -n xtrap-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_bindir}/xtrap*
%{_mandir}/man1/xtrap*.1*
