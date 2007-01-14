Summary:	AVR microcontrollers IDE
Summary(pl):	IDE dla mikrokontrolerów AVR
Name:		kontrollerlab
Version:	0.7.0
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/kontrollerlab/%{name}-%{version}.tar.gz
# Source0-md5:	11ffd5a8d27db4979810542b95713e20
URL:		http://www.cadmaniac.org/
BuildRequires:	kdelibs-devel
BuildRequires:	libtool
BuildRequires:	qt-devel >= 3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE based IDE for AVR microcontrollers. Fully-featured editor which
includes serial terminal for debugging, uses AVR-GCC compiler, uisp
for serial downloading and avrdude programming software.

%description -l pl
IDE oparte o KDE dla mikrokontrolerów AVR. W pe³ni funkcjonalny
edytor, który zawiera terminal do uruchamiania programów, u¿ywa
kompilatora AVR-GCC, oraz uisp i avrdude do programowania.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/*.desktop \
	$RPM_BUILD_ROOT%{_desktopdir}/kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/*
%{_datadir}/mimelnk/application/x-kontrollerlab.desktop
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/*/*/apps/%{name}.png
