#!/bin/bash

if [ $# -ne 1 ]; then
  echo 1>&2 "Usage: $0 CONFLUENCE-VERSION"
  exit 3
fi

confluence_spec=rpmbuild/SPECS/atlassian-confluence-$1.spec
java_specs=rpmbuild/SPECS/atlassian-confluence-java-*.spec

yum -y install rpmdevtools yum-utils
rpmdev-setuptree

for spec_files in *.spec; do
	
	if [ -e "$spec_files" ]; then
		mv *.spec rpmbuild/SPECS/
	else
		echo "No new specs files were found"
	fi
    
    break
done

for patch_files in *.patch; do
	
	if [ -e "$patch_files" ]; then
		mv *.patch rpmbuild/SOURCES/
	else
		echo "No new patch files were found"
	fi
    
    break
done

yum-builddep -y $java_specs $confluence_spec

for spec_file in $java_specs; do
	spectool -g -R $spec_file
done
spectool -g -R $confluence_spec

rpmbuild -ba $java_specs $confluence_spec
