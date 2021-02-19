%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%define _generic_name atlassian-confluence-java

Name:		%{_generic_name}-jre1.8
Version:	1.8
Release:	1%{?dist}
Summary:	Dummy package to handle Atlassian Confluence Java requirements

License:	Oracle Binary Code License (“BCL”)
URL:		https://www.oracle.com/java/technologies/javase/javase8-archive-downloads.html

BuildArch:	noarch
Requires:	jre1.8
Conflicts:	jre1.8 = 1.8.0_25, jre1.8 = 1.8.0_31, jre1.8 = 1.8.0_45
Provides:	%{_generic_name}
Conflicts:	%{_generic_name}

%description
The boolean dependencies where introduced in RPM 4.13 which wasn't included in RHEL/CentOS 7 (the RPM there is version 4.11). Using this dummy packages to get the same result.

%install

%files

%changelog
* Mon Oct 5 2020 Irving Leonard <mm-irvingleonard@github.com> 1.8-1
- Initial RPM release
