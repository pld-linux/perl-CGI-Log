%include	/usr/lib/rpm/macros.perl
Summary:	CGI-Log perl module
Summary(pl):	Modu³ perla CGI-Log
Name:		perl-CGI-Log
Version:	1.00
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-Log-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-Log - Perl extension for centralized logging of debug, error,
status and success messages from scripts or other modules.

%description -l pl
Modu³ perla CGI-Log.

%prep
%setup -q -n CGI-Log-%{version}

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
