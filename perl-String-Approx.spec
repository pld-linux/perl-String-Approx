%define	pdir	String
%define	pnam	Approx
%include	/usr/lib/rpm/macros.perl
Summary:	String-Approx perl module
Summary(pl):	Modu� perla String-Approx
Name:		perl-String-Approx
Version:	3.18
Release:	2

License:	GPL
Group:		Development/Languages/Perl
Group(cs):	V�vojov� prost�edky/Programovac� jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	��ȯ/����/Perl
Group(pl):	Programowanie/J�zyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	����������/�����/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String-Approx lets you match and substitute strings approximately.

%description -l pl
String-Approx pozwala na przybli�one dopasowywanie i zast�powanie
�a�cuch�w.

%prep
%setup -q -n String-Approx-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README README.apse

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitearch}/String/Approx.pm
%dir %{perl_sitearch}/auto/String/Approx
%{perl_sitearch}/auto/String/Approx/Approx.bs
%attr(755,root,root) %{perl_sitearch}/auto/String/Approx/Approx.so
%{_mandir}/man3/*
