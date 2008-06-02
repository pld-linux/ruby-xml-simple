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
BuildRequires:	setup.rb = 3.3.1
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class XmlSimple offers an easy API to read and write XML. It is a Ruby
translation of Grant McLean's Perl module XML::Simple.

%description -l pl.UTF-8
Klasa XmlSimple oferuje proste API do odczytu i zapisu XML-a. Jest to
tłumaczenie dla języka Ruby modułu Perla Granta McLeana XML::Simple.

%prep
%setup -q -c
tar xf %{SOURCE0} -O data.tar.gz | tar xzv-
cp %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

ruby setup.rb setup

#rdoc --op rdoc lib
#rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

#cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc rdoc
#%{ruby_ridir}/*
%{ruby_rubylibdir}/xmlsimple.rb
