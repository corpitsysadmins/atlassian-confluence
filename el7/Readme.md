# RHEL/Centos 7 and compatibles

## Building RPMs

The instructions assume that the working directory is the one containing this file.

In order to build the package you need to have a working [docker](https://www.docker.com/) environment and "prepare" the building container:

`docker build -t atlassian-confluence-packager:el7 .`

Then, to build the latest version:

`docker run --rm --volume "$PWD"/releases:/root/rpmbuild/SRPMS --volume "$PWD"/releases:/root/rpmbuild/RPMS atlassian-confluence-packager:el7 atlassian-confluence-7-4.spec`

The resulting RPMs (including source RPMs) should land in the `releases` directory. There might be some issues with permissions, so you might want to run:

```sudo chown -R `whoami` releases/*```

## Updating SPECs

Since the last parameter to the "docker run" is the name of the SPEC file one might assume that is "passing" it to the container, which is not true. Instead, that parameter is the name used to identify the file that was copied over during the "docker build" phase. That's why you need to re-build the image every time you update the SPEC files, since running the existing image will only process the old version (or fail altogether, if it's a new SPEC file).

## Java

Java dependency is a little complex in RHEL7 because of the version of `rpm` included there (4.11). In version 4.13 of `rpm` they included boolean requirements, meaning that you can ask for ```dep1 OR dep2 OR dep3```. Previous to that a `requirement` is a hard requirement, it MUST be provided or else the installation will fail.

The solution was to create a resource called `atlassian-confluence-java` that will be required by the `atlassian-confluence-X-Y` package. Such requirement can be provided by  any of the other specs included here. Each of those `atlassian-confluence-java-X` require a different JDK which would be supported by confluence:
- Oracle JRE 1.8
- AdoptOpenJDK 8
- AdoptOpenJDK 11
- Eclipse Temurin 8
- Eclipse Temurin 11
- Eclipse Temurin 17

They conflict between each other, so you can only install one of them at the same time. The idea would be to actually uninstall the JDK that was pulled when you uninstall one of these but that's not implemented yet. Keep that in mind if you're "changing between JDKs", you might want to check the default java in your environment.
