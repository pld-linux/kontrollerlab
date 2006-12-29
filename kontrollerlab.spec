Summary:	AVR microcontrollers IDE
Summary(pl):	IDE dla mikrokontroler�w AVR
Name:		kontrollerlab
Version:	0.7.0
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	11ffd5a8d27db4979810542b95713e20
URL:		http://www.cadmaniac.org/
BuildRequires:  kdelibs-devel
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE based IDE for AVR microcontrollers.

%description -l pl

%prep
%setup -q

%build
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applnk/Utilities/*
%{_datadir}/apps/*
%{_datadir}/mimelnk/application/x-kontrollerlab.desktop
%{_iconsdir}/*/*/apps/%{name}.png