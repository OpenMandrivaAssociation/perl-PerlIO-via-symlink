%define realname	PerlIO-via-symlink
%define rel 5
Name:		perl-%{realname}
Version:	0.05
Release:	%mkrel %rel
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Perl module that helps creating dynamic PerlIO layers
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}/
BuildRequires:	perl-devel
BuildArch:      noarch

%description
PerlIO::via::dynamic is used for creating dynamic PerlIO layers.
It is useful when the behavior of the layer depends on variables.

%prep
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/*

