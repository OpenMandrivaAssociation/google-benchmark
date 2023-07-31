%define libname	%mklibname benchmark
%define devname	%mklibname benchmark -d

%define api	1

Name:		  google-benchmark
Version:	1.8.2
Release:	1
Summary:	A microbenchmark support library
Group:    System/Libraries
License:	ASL 2.0
URL:		  https://github.com/google/benchmark
Source0:	https://github.com/google/benchmark/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	pkgconfig(gmock)
BuildRequires:	pkgconfig(gtest)

%description
A library to support the benchmarking of functions, similar to unit-tests.

%package -n	%{libname}
Summary:	A microbenchmark support library
Group:		System/Libraries
Provides: google-benchmark

%description -n	%{libname}
A library to support the benchmarking of functions, similar to unit-tests.

%package -n	%{devname}
Summary:	Development files for %{name}
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	benchmark-devel = %{EVRD}

%description -n	%{devname}
Development headers and files for %{name} libraries.


%prep
%autosetup -n benchmark-%{version} -p1

sed -i 's@lib/@%{_lib}/@g' src/CMakeLists.txt

%build
%cmake -G Ninja \
       -DBENCHMARK_ENABLE_TESTING:BOOL=OFF
%make_build

%install
%make_install -C build

%files -n %{libname}
%doc AUTHORS CONTRIBUTORS CONTRIBUTING* README*
%license LICENSE
%{_libdir}/libbenchmark*.so.%{api}{,.*}

%files -n %{devname}
%doc %{_datadir}/doc/benchmark/
%{_libdir}/libbenchmark*.so
%{_includedir}/benchmark/
%{_libdir}/cmake/benchmark/
%{_libdir}/pkgconfig/benchmark.pc
