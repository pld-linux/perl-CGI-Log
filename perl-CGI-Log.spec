%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Log
Summary:	CGI::Log perl module
Summary(pl):	Modu³ perla CGI::Log
Name:		perl-CGI-Log
Version:	1.00
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Log - Perl extension for centralized logging of debug, error,
status and success messages from scripts or other modules.

%description -l pl
Modu³ perla CGI::Log - s³u¿±cy do zcentralizowanego logowania
informacji diagnostycznych, b³êdów, statusu itp. ze skryptów i innych
modu³ów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/CGI/Log.pm
%{_mandir}/man3/*
