#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	String
%define		pnam	Approx
Summary:	String::Approx Perl module
Summary(cs.UTF-8):   Modul String::Approx pro Perl
Summary(da.UTF-8):   Perlmodul String::Approx
Summary(de.UTF-8):   String::Approx Perl Modul
Summary(es.UTF-8):   Módulo de Perl String::Approx
Summary(fr.UTF-8):   Module Perl String::Approx
Summary(it.UTF-8):   Modulo di Perl String::Approx
Summary(ja.UTF-8):   String::Approx Perl モジュール
Summary(ko.UTF-8):   String::Approx 펄 모줄
Summary(nb.UTF-8):   Perlmodul String::Approx
Summary(pl.UTF-8):   Moduł Perla String::Approx
Summary(pt.UTF-8):   Módulo de Perl String::Approx
Summary(pt_BR.UTF-8):   Módulo Perl String::Approx
Summary(ru.UTF-8):   Модуль для Perl String::Approx
Summary(sv.UTF-8):   String::Approx Perlmodul
Summary(uk.UTF-8):   Модуль для Perl String::Approx
Summary(zh_CN.UTF-8):   String::Approx Perl 模块
Name:		perl-String-Approx
Version:	3.26
Release:	1
License:	LGPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fc14d72986431025125d4970dd6b7f88
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Approx lets you match and substitute strings approximately.

%description -l pl.UTF-8
String::Approx pozwala na przybliżone dopasowywanie i zastępowanie
łańcuchów.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
