%include	/usr/lib/rpm/macros.perl
Summary:	String-Approx perl module
Summary(pl):	Modu³ perla String-Approx
Name:		perl-String-Approx
Version:	3.09
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/String/String-Approx-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String-Approx lets you match and substitute strings approximately.

%description -l pl
String-Approx pozwala na przybli¿one dopasowywanie i zastêpowanie
³añcuchów.

%prep
%setup -q -n String-Approx-%{version}

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT/%{perl_sitearch}/auto/String/Approx/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/String/Approx
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        ChangeLog README README.apse

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ChangeLog,README,README.apse}.gz

%{perl_sitearch}/String/Approx.pm

%dir %{perl_sitearch}/auto/String/Approx
%{perl_sitearch}/auto/String/Approx/.packlist
%{perl_sitearch}/auto/String/Approx/Approx.bs
%attr(755,root,root) %{perl_sitearch}/auto/String/Approx/Approx.so

%{_mandir}/man3/*
