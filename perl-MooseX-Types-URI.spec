%define upstream_name    MooseX-Types-URI
%define upstream_version 0.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    L<URI> related types and coercions for Moose
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/MooseX/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(MooseX::Types)
BuildRequires: perl(MooseX::Types::Path::Class)
BuildRequires: perl(Test::use::ok)
BuildRequires: perl(URI)
BuildRequires: perl(URI::FromHash)
BuildRequires: perl(namespace::clean)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This package provides Moose types for fun with the URI manpages.

It has slightly DWIMier types than the the URI manpage classes have due to
implementation details, so the types should be more forgiving when
ducktyping will work anyway (e.g. the URI::WithBase manpage does not
inherit the URI manpage).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml
%{_mandir}/man3/*
%perl_vendorlib/*


