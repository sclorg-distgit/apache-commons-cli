%{?scl:%scl_package apache-commons-cli}
%{!?scl:%global pkg_name %{name}}

%{?scl:%thermostat_find_provides_and_requires}

%global base_name       cli
%global short_name      commons-%{base_name}

Name:             %{?scl_prefix}apache-%{short_name}
Version:          1.2
Release:          18%{?dist}
Summary:          Command Line Interface Library for Java
Group:            Development/Libraries
License:          ASL 2.0
URL:              http://commons.apache.org/%{base_name}/
Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:        noarch

BuildRequires:    java-devel >= 1:1.6.0
BuildRequires:    maven30-maven-local
BuildRequires:    maven30-apache-commons-parent >= 26-7

%description
The CLI library provides a simple and easy to use API for working with the 
command line arguments and options.

%package javadoc
Summary:          Javadoc for %{pkg_name}
Group:            Documentation

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%{?scl:scl enable maven30 %{scl} - << "EOF"}
%setup -q -n %{short_name}-%{version}-src

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :commons-cli %{short_name} %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Tue Jun 17 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1.2-18
- Only enable maven30 collection in spec file.

* Mon Jun 16 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1.2-17
- Rebuild against maven30 collection.

* Mon Jan 20 2014 Omair Majid <omajid@redhat.com> - 1.2-16
- Rebuild in order to fix osgi()-style provides.
- Resolves: RHBZ#1054813

* Wed Nov 27 2013 Severin Gehwolf <sgehwolf@redhat.com> - 1.2-15
- Properly enable SCL.

* Tue Nov 19 2013 Severin Gehwolf <sgehwolf@redhat.com> - 1.2-14
- Fix SCL package name.

* Fri Nov 15 2013 Omair Majid <omajid@redhat.com> - 1.2-13
- Find provides and requires automatically
- Remove non-scl-specific obsoletes

* Mon Nov 11 2013 Jiri Vanek <jvanek@redhat.com> - 1.2-13
- SCL-ize package.

* Fri Sep 20 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-12
- Add BuildRequires on apache-commons-parent >= 26-7

* Thu Aug 22 2013 Michal Srb <msrb@redhat.com> - 1.2-11
- Migrate away from mvn-rpmbuild (Resolves: #997473)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2-10
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Tue Feb 19 2013 Mat Booth <fedora@matbooth.co.uk> - 1.2-9
- Add missing maven-local BuildRequires

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2-5
- Build with maven 3.
- Adapt to current guidelines.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 9 2010 Chris Spike <chris.spike@arcor.de> 1.2-3
- Removed maven* BRs in favour of apache-commons-parent
- Added deprecated groupId to depmap for compatibility reasons

* Mon Oct 18 2010 Chris Spike <chris.spike@arcor.de> 1.2-2
- Removed Epoch

* Sun Oct 3 2010 Chris Spike <chris.spike@arcor.de> 1.2-1
- Rename and rebase from jakarta-commons-cli
