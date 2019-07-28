# sitelib for noarch packages, sitearch for others (remove the unneeded one)
%{!?__python2: %global __python2 %__python}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}

# % global setools_pre_ver beta.1.8e09d95
# % global gitver f1e5b20

%global sepol_ver 2.8-1
%global selinux_ver 2.8-1

Name:           setools
Version:        4.1.1
Release:        14%{?setools_pre_ver:.%{setools_pre_ver}}%{?dist}
Summary:        Policy analysis tools for SELinux

License:        GPLv2
URL:            https://github.com/SELinuxProject/setools/wiki
Source0:        https://github.com/SELinuxProject/setools/archive/%{version}%{?setools_pre_ver:-%{setools_pre_ver}}.tar.gz
Source1:        setools.pam
Source2:        apol.desktop
Patch1:         0001-Do-not-use-Werror-during-build.patch
Patch2:         0002-Do-not-export-use-setools.InfoFlowAnalysis-and-setoo.patch
Patch3:         0003-bswap_-macros-are-defined-in-byteswap.h.patch
Patch4:         0004-Add-support-for-SCTP-protocol.patch

Obsoletes:      setools < 4.0.0, setools-devel < 4.0.0
BuildRequires:  flex, bison
BuildRequires:  glibc-devel, gcc, git
BuildRequires:  libsepol-devel >= %{sepol_ver}
BuildRequires:	sepol-static-devel >= %{sepol_ver}
BuildRequires:  qt5-qtbase-devel
BuildRequires:  swig
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

# BuildArch:      
Requires:       python3-%{name} = %{version}-%{release}

%description
SETools is a collection of graphical tools, command-line tools, and
Python modules designed to facilitate SELinux policy analysis.

%package     console
Summary:     Policy analysis command-line tools for SELinux
License:     GPLv2
Requires:    python3-setools = %{version}-%{release}
Requires:    libselinux >= %{selinux_ver}

%description console
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following console tools:

  sediff       Compare two policies to find differences.
  seinfo       List policy components.
  sesearch     Search rules (allow, type_transition, etc.)


%package     console-analyses
Summary:     Policy analysis command-line tools for SELinux
License:     GPLv2
Requires:    python3-setools = %{version}-%{release}
Requires:    libselinux >= %{selinux_ver}
Requires:    python3-networkx

%description console-analyses
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following console tools:

  sedta        Perform domain transition analyses.
  seinfoflow   Perform information flow analyses.


%package     -n python2-setools
Summary:     Policy analysis tools for SELinux  
Provides:	python2-setools = %{EVRD}
Provides: %{name}-python = %{version}-%{release}
Obsoletes: %{name}-python < %{version}-%{release}
Requires:    python2-enum34
Requires:    python2-setuptools

%description -n python2-setools
SETools is a collection of graphical tools, command-line tools, and
Python 2 modules designed to facilitate SELinux policy analysis.

%package     -n python3-setools
Summary:     Policy analysis tools for SELinux  
Obsoletes:   setools-libs < 4.0.0
Provides:    python3-setools = %{EVRD}
Provides:    python-setools = %{EVRD}
Requires:    python3-setuptools

%description -n python3-setools
SETools is a collection of graphical tools, command-line tools, and
Python 3 modules designed to facilitate SELinux policy analysis.

%package     gui
Summary:     Policy analysis graphical tools for SELinux
Requires:    python3-setools = %{version}-%{release}
Requires:    python-qt5
Requires:    python3-networkx

%description gui
SETools is a collection of graphical tools, command-line tools, and
Python modules designed to facilitate SELinux policy analysis.

%prep
%autosetup -p 1 -S git

cp -a ../setools-%{version}%{?setools_pre_ver:-%{setools_pre_ver}} ../setools-%{version}%{?setools_pre_ver:-%{setools_pre_ver}}-python2

%build
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="%{optflags}" %{__python3} setup.py build

pushd ../setools-%{version}%{?setools_pre_ver:-%{setools_pre_ver}}-python2
# Remove CFLAGS=... for noarch packages (unneeded)
CFLAGS="%{optflags}" %{__python2} setup.py build
popd


%install
pushd ../setools-%{version}%{?setools_pre_ver:-%{setools_pre_ver}}-python2
%{__python2} setup.py install --root %{buildroot}
popd

rm -rf %{buildroot}%{_bindir}
%{__python3} setup.py install --root %{buildroot}

%check
%if %{?_with_check:1}%{!?_with_check:0}
%{__python3} setup.py test

pushd ../setools-%{version}%{?setools_pre_ver:-%{setools_pre_ver}}-python2
%{__python2} setup.py test
popd
%endif


%files

%files console
%{_bindir}/sediff
%{_bindir}/seinfo
%{_bindir}/sesearch
%{_mandir}/man1/sediff*
%{_mandir}/man1/seinfo*
%{_mandir}/man1/sesearch*

%files console-analyses
%{_bindir}/sedta
%{_bindir}/seinfoflow
%{_mandir}/man1/sedta*
%{_mandir}/man1/seinfoflow*

%files -n python2-setools
%license COPYING COPYING.GPL COPYING.LGPL
%{python2_sitearch}/*

%files -n python3-setools
%license COPYING COPYING.GPL COPYING.LGPL
%{python3_sitearch}/setools
%{python3_sitearch}/setools-*

%files gui
%{_bindir}/apol
%{python3_sitearch}/setoolsgui
%{_mandir}/man1/apol*
