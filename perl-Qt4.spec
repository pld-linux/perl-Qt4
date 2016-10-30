%define         _state          stable
%define         orgname         perlqt
%define         qtver           4.8.0

# Conditional build:
%bcond_with	tests		# do not perform "make test"

%define	pdir	PerlQt
%include	/usr/lib/rpm/macros.perl
Summary:	Qt4 - A Perl module interface to Qt4
Summary(pl.UTF-8):	Qt4 - interfejs Perla do Qt4
Name:		perl-Qt4
Version:	4.14.3
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	d410c5b95680d1c56d037d22ef984479
URL:		http://www.kde.org/
BuildRequires:	QtXmlPatterns-devel
BuildRequires:	kde4-smokeqt-devel >= %{version}
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq_perl		Qt::_internal

%description
This module provides bindings to the Qt 4 libraries for Perl.

%description -l pl.UTF-8
Moduł dostarcza dowiązania do Qt 4 dla Perla.

%package devel
Summary:	Header file for  perl Qt 4
Summary(pl.UTF-8):	Plik nagłówkowe perl Qt 4
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for perl Qt 4.

%description devel -l pl.UTF-8
Plik nagłówkoww perl Qt 4.

%define		_noautoreq	'perl(Qt::_internal)'
# which package provides this?

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	-DCUSTOM_PERL_SITE_ARCH_DIR=%{perl_vendorarch} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	kde_htmldir=%{_kdedocdir} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/prcc4_bin
%attr(755,root,root) %{_bindir}/puic4
%attr(755,root,root) %{_bindir}/qdbusxml2perl
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/QtCore4
%{perl_vendorarch}/QtCore4/*.pm
%dir %{perl_vendorarch}/auto
%dir %{perl_vendorarch}/auto/*
%attr(755,root,root) %{perl_vendorarch}/auto/*/*.so
%dir %{_datadir}/perlqt
%attr(755,root,root) %{_datadir}/perlqt/doxsubpp.pl

%files devel
%defattr(644,root,root,755)
%{_includedir}/perlqt
%{_datadir}/perlqt/cmake
