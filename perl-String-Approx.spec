#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	String
%define		pnam	Approx
Summary:	String::Approx - Perl module for approximate matching (fuzzy matching)
Summary(pl.UTF-8):	String::Approx - moduł Perlado dopasowywania przybliżonego (rozmytego)
Name:		perl-String-Approx
Version:	3.28
Release:	4
License:	LGPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/String/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ad98d17213344302ef7edf745a030390
URL:		http://search.cpan.org/dist/String-Approx/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String::Approx lets you match and substitute strings approximately.
With this you can emulate errors: typing errorrs, speling errors,
closely related vocabularies (colour color), genetic mutations (GAG
ACT), abbreviations (McScot, MacScot).

%description -l pl.UTF-8
String::Approx pozwala na przybliżone dopasowywanie i zastępowanie
łańcuchów. Przy jego użyciu można emulować błędy: literrówki, błendy
ortograficzne, bliskie sobie słowniki (colour/color), mutacje
genetyczne (GAG ACT), skróty (McScot, MacScot).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/String/Approx/Approx.so
%{_mandir}/man3/*
