%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%define _generic_name atlassian-confluence-java

Name:		%{_generic_name}-jdk1.8
Version:	1.8
Release:	1%{?dist}
Summary:	Dummy package to handle Atlassian Confluence Java requirements

License:	Oracle Binary Code License (“BCL”)
URL:		https://www.oracle.com/java/technologies/javase/javase8u211-later-archive-downloads.html

BuildArch:	noarch
Requires:	jdk1.8
Conflicts:	jre1.8
Provides:	%{_generic_name}
Conflicts:	%{_generic_name}

%description
The boolean dependencies where introduced in RPM 4.13 which wasn't included in RHEL/CentOS 7 (the RPM there is version 4.11). Using this dummy packages to get the same result.

%install

%files

%changelog
* Wed May 17 2023 Alexander Zaballa <mm-alexander@github.com> 1.8-1
- Initial RPM release
