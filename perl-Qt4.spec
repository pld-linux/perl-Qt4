
%define         _state          stable
%define         orgname         perlqt
%define         qtver           4.7.4

# Conditional build:
%bcond_with	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	PerlQt
Summary:	Qt4 - A Perl module interface to Qt4
Summary(pl.UTF-8):	Qt4 - interfejs Perla do Qt4
Name:		perl-Qt4
Version:	4.7.3
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.bz2
# Source0-md5:	cd13db20c7d3c93d837430a0370b30f1
URL:		http://www.kde.org/
BuildRequires:	smokeqt-devel >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides bindings to the Qt 4 libraries for Perl.

%description -l pl.UTF-8
Moduł dostarcza dowiązania do Qt 4 dla Perla.

# which package provides this?
%define		_noautoreq	'perl(Qt::_internal)'

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

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/prcc4_bin
%attr(755,root,root) %{_bindir}/puic4
%attr(755,root,root) %{_bindir}/qdbusxml2perl
%{_includedir}/perlqt
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/QtCore4
%{perl_vendorarch}/QtCore4/*.pm
%dir %{perl_vendorarch}/auto
%dir %{perl_vendorarch}/auto/*
%attr(755,root,root) %{perl_vendorarch}/auto/*/*.so
%dir %{_datadir}/perlqt
%{_datadir}/perlqt/cmake
%attr(755,root,root) %{_datadir}/perlqt/doxsubpp.pl
