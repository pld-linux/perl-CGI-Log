%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Log
Summary:	CGI::Log perl module
Summary(pl):	Modu� perla CGI::Log
Name:		perl-CGI-Log
Version:	1.00
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Log - Perl extension for centralized logging of debug, error,
status and success messages from scripts or other modules.

%description -l pl
Modu� perla CGI::Log.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/CGI/Log.pm
%{_mandir}/man3/*
