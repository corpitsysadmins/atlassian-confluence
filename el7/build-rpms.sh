#!/bin/bash

yum -y install rpmdevtools yum-utils && \
rpmdev-setuptree && \
mv *.spec rpmbuild/SPECS/ && \
mv *.patch rpmbuild/SOURCES/ && \
yum-builddep -y rpmbuild/SPECS/atlassian-confluence-$1.spec && \
spectool -g -R rpmbuild/SPECS/atlassian-confluence-$1.spec &&\
rpmbuild -ba rpmbuild/SPECS/atlassian-confluence-$1.spec
