# RHEL/CentOS 7 and compatibles

In order to build the package you need to copy all the files in this directory (including the tarballs) to a directory with enough free space in your build host (/tmp might not be big enough). Then
```
chmod +x build_rpms.sh
./build_rpms.sh <your-version>
```
where <your-version> matches an existing SPEC file. The source RPM will end up in rpmbuild/SRPMS and the binary one in rpmbuild/RPMS
