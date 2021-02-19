%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%define _generic_name atlassian-confluence-java

Name:		%{_generic_name}-adoptopenjdk-11-hotspot
Version:	11
Release:	1%{?dist}
Summary:	Dummy package to handle Atlassian Confluence Java requirements

License:	GPL v2 with Classpath Exception
URL:		https://adoptopenjdk.net/installation.html#linux-pkg

BuildArch:	noarch
Requires:	adoptopenjdk-11-hotspot
Provides:	%{_generic_name}
Conflicts:	%{_generic_name}

%description
The boolean dependencies where introduced in RPM 4.13 which wasn't included in RHEL/CentOS 7 (the RPM there is version 4.11). Using this dummy packages to get the same result.

%install

%files

%changelog
* Mon Oct 5 2020 Irving Leonard <mm-irvingleonard@github.com> 11-1
- Initial RPM release
