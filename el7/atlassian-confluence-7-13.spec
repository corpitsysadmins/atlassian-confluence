%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%define debug_package %{nil}
%define __jar_repack 0
%define _generic_name atlassian-confluence
%define _confluence_user confluence
%define _confluence_directory /opt/%{_generic_name}
%define _confluence_home /var/confluence

Name:		%{_generic_name}-7-13
Version:	7.13.13
Release:	1%{?dist}
Summary:	Wiki system from Atlassian

License:	Atlassian End User Agreement
URL:		https://www.atlassian.com/software/confluence
Source0:	https://www.atlassian.com/software/confluence/downloads/binary/%{_generic_name}-%{version}.tar.gz
Source1:	confluence.service-7.13
Patch0:		confluence-user.patch
Patch1:		confluence-home.patch

BuildArch:	noarch
Requires:	/usr/bin/getent
Requires:	/usr/sbin/useradd
Requires:	/sbin/nologin
Requires:	/usr/sbin/userdel
Requires:	/sbin/chkconfig
Requires:	/sbin/service
Requires:	/bin/sleep
Requires:	%{_generic_name}-java
Provides:	%{_generic_name}
Conflicts:	%{_generic_name}
Obsoletes:	%{_generic_name}-7-4

%description
Create, collaborate, and organize all your work in one place. Confluence is a team workspace where knowledge and collaboration meet. Dynamic pages give your team a place to create, capture, and collaborate on any project or idea. Spaces help your team structure, organize, and share work, so every team member has visibility into institutional knowledge and access to the information they need to do their best work.

%pre
/usr/bin/getent passwd %{_confluence_user} || /usr/sbin/useradd --home %{_confluence_home} --shell /bin/bash --system --user-group %{_confluence_user}

%post
/usr/bin/systemctl daemon-reload

%preun
/usr/bin/systemctl stop confluence.service
/bin/sleep 30

%postun
/usr/bin/systemctl daemon-reload
/usr/sbin/userdel %{_confluence_user}

%prep
%setup -n %{_generic_name}-%{version}
%patch0 -p1
%patch1 -p1

%install
mkdir --parents %{buildroot}/%{_confluence_directory}
mv * %{buildroot}/%{_confluence_directory}
mkdir --parents %{buildroot}/lib/systemd/system
cp %{SOURCE1} %{buildroot}/lib/systemd/system/confluence.service
mkdir --parents %{buildroot}/%{_confluence_home}
 
%files
%attr(664, root, root) /lib/systemd/system/confluence.service
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
* Thu Feb 2 2023 Alexander Zaballa <mm-alexander@github.com> 7.13.13-1
- Update to version 7.13.13
* Tue Nov 1 2022 Alexander Zaballa <mm-alexander@github.com> 7.13.11-1
- Update to version 7.13.11
* Mon Sep 7 2022 Alexander Zaballa <mm-alexander@github.com> 7.13.9-1
- Update to version 7.13.9
* Mon Aug 15 2022 Alexander Zaballa <mm-alexander@github.com> 7.13.8-1
- Update to version 7.13.8
* Wed Nov 24 2021 Irving Leonard <mm-irvingleonard@github.com> 7.13.2-2
- Using Obsoletes to trigger updates
* Tue Nov 16 2021 Irving Leonard <mm-irvingleonard@github.com> 7.13.2-1
- Initial RPM release

