%{!?rpm_name: %define rpm_name intelcimframework}
%{!?build_version: %define build_version 99.99.99.9999}
%{!?build_release: %define build_release 1}
%define dname %{rpm_name}-devel

Name:           %{rpm_name}-libs
Version:		%{build_version}
Release:		%{build_release}%{?dist}
Summary:		Framework for Intel Storage CIM Binaries
License:        Proprietary
Group:          Development/Libraries
URL:			http://www.intel.com
Source:         %{rpm_name}.tar.bz2

%define  debug_package %{nil}

%description
Framework libraries for the Intel Storage CIM binaries

%package -n %dname
Summary:        Development files for %{name}
License:        Proprietary
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description -n %dname
The %{name}-devel package contains header files for
developing applications that use %{name}.

%prep
%setup -D -T -q -n %{rpm_name}

%build
make BUILDNUM=%{build_version} RELEASE=1

%install
make install RELEASE=1 RPM_ROOT=%{buildroot} LIB_DIR=%{_libdir} INCLUDE_DIR=%{_includedir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libcimframework.so.*

%files -n %dname
%defattr(-,root,root)
%{_libdir}/libcimframework.so
%{_includedir}/intel_cim_framework

%changelog
* Wed Dec 24 2015 nicholas.w.moulin@intel.com
- Initial rpm release
