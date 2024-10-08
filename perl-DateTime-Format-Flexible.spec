#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v20
# autospec commit: f35655a
#
Name     : perl-DateTime-Format-Flexible
Version  : 0.35
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/T/TH/THINC/DateTime-Format-Flexible-0.35.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TH/THINC/DateTime-Format-Flexible-0.35.tar.gz
Summary  : 'DateTime::Format::Flexible - Flexibly parse strings and turn them into DateTime objects.'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-DateTime-Format-Flexible-license = %{version}-%{release}
Requires: perl-DateTime-Format-Flexible-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::Format::Builder)
BuildRequires : perl(DateTime::Format::Strptime)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(List::MoreUtils)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)
BuildRequires : perl(Test::MockTime)
BuildRequires : perl(Test::NoWarnings)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
NAME
DateTime::Format::Flexible - DateTime::Format::Flexible - Flexibly parse
strings and turn them into DateTime objects.

%package dev
Summary: dev components for the perl-DateTime-Format-Flexible package.
Group: Development
Provides: perl-DateTime-Format-Flexible-devel = %{version}-%{release}
Requires: perl-DateTime-Format-Flexible = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-Flexible package.


%package license
Summary: license components for the perl-DateTime-Format-Flexible package.
Group: Default

%description license
license components for the perl-DateTime-Format-Flexible package.


%package perl
Summary: perl components for the perl-DateTime-Format-Flexible package.
Group: Default
Requires: perl-DateTime-Format-Flexible = %{version}-%{release}

%description perl
perl components for the perl-DateTime-Format-Flexible package.


%prep
%setup -q -n DateTime-Format-Flexible-0.35
cd %{_builddir}/DateTime-Format-Flexible-0.35
pushd ..
cp -a DateTime-Format-Flexible-0.35 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Flexible
cp %{_builddir}/DateTime-Format-Flexible-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Flexible/6b487264931a742fc55971d43c27b8decdf4c8bb || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::Flexible.3
/usr/share/man/man3/DateTime::Format::Flexible::lang.3
/usr/share/man/man3/DateTime::Format::Flexible::lang::de.3
/usr/share/man/man3/DateTime::Format::Flexible::lang::en.3
/usr/share/man/man3/DateTime::Format::Flexible::lang::es.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-Flexible/6b487264931a742fc55971d43c27b8decdf4c8bb

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
