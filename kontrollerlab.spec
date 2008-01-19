Summary:	AVR microcontrollers IDE
Summary(pl.UTF-8):	IDE dla mikrokontrolerów AVR
Name:		kontrollerlab
Version:	0.7.1
Release:	0.1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/kontrollerlab/%{name}-%{version}.tar.gz
# Source0-md5:	1caa33a26dc5069bfed58d90aeb273d7
URL:		http://www.cadmaniac.org/
BuildRequires:	kdelibs-devel >= 3
BuildRequires:	libtool
BuildRequires:	qt-devel >= 6:3.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE based IDE for AVR microcontrollers. Fully-featured editor which
includes serial terminal for debugging, uses AVR-GCC compiler, uisp
for serial downloading and avrdude programming software.

%description -l pl.UTF-8
IDE oparte o KDE dla mikrokontrolerów AVR. W pełni funkcjonalny
edytor, który zawiera terminal do uruchamiania programów, używa
kompilatora AVR-GCC, oraz uisp i avrdude do programowania.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir}/kde

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/kontrollerlab
%{_datadir}/apps/kontrollerlab
%{_datadir}/mimelnk/application/x-kontrollerlab.desktop
%{_desktopdir}/kde/kontrollerlab.desktop
%{_iconsdir}/*/*/apps/%{name}.png
%{_iconsdir}/*/*/actions/dbg*.png
