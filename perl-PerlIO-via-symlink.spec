%define upstream_name	 PerlIO-via-symlink
%define upstream_version 0.05

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl module that helps creating dynamic PerlIO layers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
PerlIO::via::dynamic is used for creating dynamic PerlIO layers.
It is useful when the behavior of the layer depends on variables.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc README CHANGES
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 406179
- rebuild using %%perl_convert_version

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.05-5mdv2008.1
+ Revision: 136335
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 16 2007 Thierry Vignaud <tvignaud@mandriva.com> 0.05-4mdv2008.0
+ Revision: 64193
- rebuild

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 0.05-3mdv2008.0
+ Revision: 20970
- use %%mkrel
- rebuild


* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 0.05-2mdk
- Do not ship empty dir

* Tue Mar 08 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.05-1mdk
- 0.05

* Wed Feb 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.04-1mdk
- 0.04

* Wed Nov 24 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.03-1mdk
- 0.03

* Mon Aug 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.02-1mdk
- New version 0.02. Small specfile fixes.

* Thu Aug 05 2004 Michael Scherer <misc@mandrake.org> 0.01-1mdk
- First Mandrakelinux package

