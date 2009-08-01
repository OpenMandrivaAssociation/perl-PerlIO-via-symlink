%define upstream_name	 PerlIO-via-symlink
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Perl module that helps creating dynamic PerlIO layers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:  noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
PerlIO::via::dynamic is used for creating dynamic PerlIO layers.
It is useful when the behavior of the layer depends on variables.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
