#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	String
%define	pnam	Approx
Summary:	String::Approx Perl module
Summary(cs):	Modul String::Approx pro Perl
Summary(da):	Perlmodul String::Approx
Summary(de):	String::Approx Perl Modul
Summary(es):	Módulo de Perl String::Approx
Summary(fr):	Module Perl String::Approx
Summary(it):	Modulo di Perl String::Approx
Summary(ja):	String::Approx Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	String::Approx ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul String::Approx
Summary(pl):	Modu³ Perla String::Approx
Summary(pt):	Módulo de Perl String::Approx
Summary(pt_BR):	Módulo Perl String::Approx
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl String::Approx
Summary(sv):	String::Approx Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl String::Approx
Summary(zh_CN):	String::Approx Perl Ä£¿é
Name:		perl-String-Approx
Version:	3.19
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e39c231b07ae3f7fa1f53d89aeb2fea4
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Approx lets you match and substitute strings approximately.

%description -l pl
String::Approx pozwala na przybli¿one dopasowywanie i zastêpowanie
³añcuchów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.apse
%{perl_vendorarch}/String/Approx.pm
%dir %{perl_vendorarch}/auto/String/Approx
%{perl_vendorarch}/auto/String/Approx/Approx.bs
%attr(755,root,root) %{perl_vendorarch}/auto/String/Approx/Approx.so
%{_mandir}/man3/*
