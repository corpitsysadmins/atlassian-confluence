FROM centos:7

RUN yum -y upgrade
RUN yum -y install rpmdevtools yum-utils

WORKDIR /root
RUN rpmdev-setuptree
VOLUME ["/root/rpmbuild/SRPMS", "/root/rpmbuild/RPMS"]

COPY additional/* /root/rpmbuild/SOURCES/
COPY *.patch /root/rpmbuild/SOURCES/

WORKDIR /root/rpmbuild/SPECS/

COPY *.spec ./
RUN for spec_file in *.spec; do yum-builddep -y "$spec_file"; done
RUN for spec_file in *.spec; do spectool -g -R "$spec_file"; done

ENTRYPOINT ["rpmbuild", "-ba"]
