%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-ament-pyflakes
Version:        0.12.7
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS ament_pyflakes package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       python%{python3_pkgversion}-pyflakes
Requires:       ros-humble-ros-workspace
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%if 0%{?with_tests}
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  ros-humble-ament-pycodestyle
%endif

%description
The ability to check code using pyflakes and generate xUnit test result files.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%py3_install -- --prefix "/opt/ros/humble"

%if 0%{?with_tests}
%check
# Look for a directory with a name indicating that it contains tests
TEST_TARGET=$(ls -d * | grep -m1 "\(test\|tests\)" ||:)
if [ -n "$TEST_TARGET" ] && %__python3 -m pytest --version; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%__python3 -m pytest $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Mon Jul 17 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.7-1
- Autogenerated by Bloom

* Tue Apr 25 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.6-1
- Autogenerated by Bloom

* Thu Jan 12 2023 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.5-1
- Autogenerated by Bloom

* Mon May 09 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.4-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.3-2
- Autogenerated by Bloom

* Fri Apr 08 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.3-1
- Autogenerated by Bloom

* Mon Mar 28 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.2-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.1-1
- Autogenerated by Bloom

* Fri Feb 18 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.12.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Michael Jeronimo <michael.jeronimo@openrobotics.org> - 0.11.4-2
- Autogenerated by Bloom

