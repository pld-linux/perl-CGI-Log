%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Log
Summary:	CGI::Log - Perl extension for centralized logging
Summary(pl):	CGI::Log - rozszerzenia Perla do scentralizowanego logowania
Name:		perl-CGI-Log
Version:	1.00
Release:	10
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	558abf0a80fcf2a068825215c46fb841
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Log Perl module acts as a central repository for debug, status
and error messages.  It instantiates itself automatically (if it needs
to) so you can access the Log object functions from anywhere in you
code including other modules/objects with a simple consistent syntax.

%description -l pl
Modu³ Perla CGI::Log dzia³a jako centralne repozytorium dla informacji
diagnostycznych, b³êdów, statusu itp. Tworzy on swoj± kopiê
automatycznie gdy potrzeba, wiêc dostêp do funkcji obiektu Log jest
mo¿liwy sk±dkolwiek, je¶li program korzystaj±cy z innych modu³ów /
obiektów ma prost± i spójn± sk³adniê.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/Log.pm
%{_mandir}/man3/*
