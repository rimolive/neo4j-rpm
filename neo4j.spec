Name:           neo4j-server
Version:        3.4.0
Release:        1%{?dist}
Summary:        Graphs for Everyone

Group:          Applications/Databases
License:        GPLv3
URL:            https://neo4j.com/
Source0:        https://github.com/neo4j/neo4j/archive/3.4.0.tar.gz

BuildRequires:  java-1.8.0-openjdk-devel
Requires:       java-1.8.0-openjdk

%description
Neo4j is the world’s leading Graph Database. It is a high performance graph 
store with all the features expected of a mature and robust database, like 
a friendly query language and ACID transactions. The programmer works with 
a flexible network structure of nodes and relationships rather than static 
tables — yet enjoys all the benefits of enterprise-quality database. For 
many applications, Neo4j offers orders of magnitude performance benefits 
compared to relational DBs.

%prep
%setup -q


%build
%configure
mvn clean install


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc

%changelog
* Fri May 18 2018 Ricardo Martinelli de oliveira <rmartine@redhat.com> - 1.0.0-1
- Initial release.