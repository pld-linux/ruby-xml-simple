Summary:	Easy XML API for Ruby
Summary(pl.UTF-8):	Proste API XML-a dla języka Ruby
Name:		ruby-xml-simple
Version:	1.0.11
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/18366/xml-simple-%{version}.gem
# Source0-md5:	73cda917a0b84f9e97cde65d4587fb18
URL:		http://xml-simple.rubyforge.org/
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	setup.rb >= 3.3.1
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
Summary:	Documentation files for XmlSimple
Summary(pl.UTF-8):	Pliki dokumentacji do klasy XmlSimple
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for XmlSimple

%description rdoc -l pl.UTF-8
Pliki dokumentacji do klasy XmlSimple.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

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
%{ruby_ridir}/XmlSimple
