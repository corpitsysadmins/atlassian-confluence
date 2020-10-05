# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%define debug_package %{nil}
%define __jar_repack 0
%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%define _generic_name atlassian-confluence
%define _confluence_user confluence
%define _confluence_directory /opt/%{_generic_name}
%define _confluence_home /var/confluence

Name:		%{_generic_name}-7-4
Version:	7.4.3
Release:	2%{?dist}
Summary:	Wiki system from Atlassian

License:	Atlassian End User Agreement
URL:		https://www.atlassian.com/software/confluence
Source0:	https://www.atlassian.com/software/confluence/downloads/binary/%{_generic_name}-%{version}.tar.gz
Source1:	https://raw.githubusercontent.com/corpitsysadmins/%{_generic_name}/master/el7/additional/sysvinit-7.4.3
Patch0:		confluence-user.patch
Patch1:		confluence-home.patch

Requires:	/usr/bin/getent
Requires:	/usr/sbin/useradd
Requires:	/sbin/nologin
Requires:	/usr/sbin/userdel
Requires:	/sbin/chkconfig
Requires:	/sbin/service
Requires:	/bin/sleep
Requires:	adoptopenjdk-11-hotspot, adoptopenjdk-8-hotspot, jre1.8
Conflicts:	jre1.8 = 1.8.0_25, jre1.8 = 1.8.0_31, jre1.8 = 1.8.0_45
Provides:	%{_generic_name}
Conflicts:	%{_generic_name}

%description
Create, collaborate, and organize all your work in one place. Confluence is a team workspace where knowledge and collaboration meet. Dynamic pages give your team a place to create, capture, and collaborate on any project or idea. Spaces help your team structure, organize, and share work, so every team member has visibility into institutional knowledge and access to the information they need to do their best work.

%pre
/usr/bin/getent passwd %{_confluence_user} || /usr/sbin/useradd --home %{_confluence_home} --shell /bin/bash --system --user-group %{_confluence_user}

%post
/sbin/chkconfig --add confluence

%preun
/sbin/service confluence stop
/bin/sleep 30

%postun
/usr/sbin/userdel %{_confluence_user}

%prep
%setup -n %{_generic_name}-%{version}
%patch0 -p1
%patch1 -p1

%install
mkdir --parents %{buildroot}/%{_confluence_directory}
mv * %{buildroot}/%{_confluence_directory}
mkdir --parents %{buildroot}/etc/init.d
cp %{SOURCE1} %{buildroot}/etc/init.d/confluence
mkdir --parents %{buildroot}/%{_confluence_home}
 
%files
%attr(755, root, root) /etc/init.d/confluence
%attr(-, %{_confluence_user}, %{_confluence_user}) %{_confluence_directory}/bin
%attr(-, %{_confluence_user}, %{_confluence_user}) %config %{_confluence_directory}/conf
%attr(-, %{_confluence_user}, %{_confluence_user}) %{_confluence_directory}/confluence
%attr(-, %{_confluence_user}, %{_confluence_user}) %{_confluence_directory}/lib
%attr(-, %{_confluence_user}, %{_confluence_user}) %doc %{_confluence_directory}/licenses
%attr(-, %{_confluence_user}, %{_confluence_user}) %dir %{_confluence_directory}/logs
%attr(-, %{_confluence_user}, %{_confluence_user}) %{_confluence_directory}/synchrony-proxy
%attr(-, %{_confluence_user}, %{_confluence_user}) %{_confluence_directory}/temp
%attr(-, %{_confluence_user}, %{_confluence_user}) %dir %{_confluence_directory}/webapps
%attr(-, %{_confluence_user}, %{_confluence_user}) %dir %{_confluence_directory}/work
%attr(-, %{_confluence_user}, %{_confluence_user}) %doc %{_confluence_directory}/*.html
%attr(-, %{_confluence_user}, %{_confluence_user}) %doc %{_confluence_directory}/*.md
%attr(-, %{_confluence_user}, %{_confluence_user}) %doc %{_confluence_directory}/*.txt
%attr(-, %{_confluence_user}, %{_confluence_user}) %doc %{_confluence_directory}/LICENSE
%attr(-, %{_confluence_user}, %{_confluence_user}) %doc %{_confluence_directory}/NOTICE
%attr(-, %{_confluence_user}, %{_confluence_user}) %doc %{_confluence_directory}/RELEASE-NOTES
%attr(750, %{_confluence_user}, %{_confluence_user}) %dir %{_confluence_home}

%changelog
* Mon Oct 5 2020 Irving Leonard <mm-irvingleonard@github.com> 7.4.3-2
- Adding OpenJDK support
* Fri Aug 28 2020 Irving Leonard <mm-irvingleonard@github.com> 7.4.3-1
- Initial RPM release
