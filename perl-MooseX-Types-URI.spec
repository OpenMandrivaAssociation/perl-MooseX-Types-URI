%define upstream_name    MooseX-Types-URI
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	L<URI> related types and coercions for Moose
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MooseX/MooseX-Types-URI-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(MooseX::Types)
BuildRequires:	perl(MooseX::Types::Path::Class)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(URI)
BuildRequires:	perl(URI::FromHash)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
This package provides Moose types for fun with the URI manpages.

It has slightly DWIMier types than the the URI manpage classes have due to
implementation details, so the types should be more forgiving when
ducktyping will work anyway (e.g. the URI::WithBase manpage does not
inherit the URI manpage).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 0.20.0-2mdv2011.0
+ Revision: 653606
- rebuild for updated spec-helper

* Tue Aug 24 2010 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2011.0
+ Revision: 572868
- import perl-MooseX-Types-URI


