%define pkgname xml-simple
Summary:	Easy XML API for Ruby
Summary(pl.UTF-8):	Proste API XML-a dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.0.12
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	bd526c32d7dd49ce329f2dbc6d3f47c9
URL:		http://xml-simple.rubyforge.org/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
Requires:	ruby-modules >= 1:1.8
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarc only because of ruby packaging
%define		_enable_debug_packages	0

%description
Class XmlSimple offers an easy API to read and write XML. It is a Ruby
translation of Grant McLean's Perl module XML::Simple.

%description -l pl.UTF-8
Klasa XmlSimple oferuje proste API do odczytu i zapisu XML-a. Jest to
tłumaczenie dla języka Ruby modułu Perla Granta McLeana XML::Simple.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer lib/xmlsimple.rb -o -print | xargs touch --reference %{SOURCE0}

%build
rdoc --op rdoc lib
rdoc --ri --op ri lib
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/xmlsimple.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/XmlSimple
