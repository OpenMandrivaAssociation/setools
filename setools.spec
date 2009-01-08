%define gcj_support 1
%define setools_maj_ver 3.3
%define setools_min_ver 5

Name: setools
Version: %{setools_maj_ver}.%{setools_min_ver}
Release: %mkrel 2
License: GPLv2
URL: http://oss.tresys.com/projects/setools
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Source: http://oss.tresys.com/projects/setools/chrome/site/dists/setools-%{version}/setools-%{version}.tar.gz
Source1: setools.pam
Source2: apol.desktop
Source3: seaudit.desktop
Source4: sediffx.desktop
Summary: Policy analysis tools for SELinux
Group: System/Base
Requires: setools-libs = %{version}-%{release} setools-libs-tcl = %{version}-%{release} setools-gui = %{version}-%{release} setools-console = %{version}-%{release}
%if %{gcj_support}
BuildRequires: java-gcj-compat-devel
%endif

# external requirements
%define autoconf_ver 2.59
%define bwidget_ver 1.8
%define java_ver 1.2
%define gtk_ver 2.8
%define python_ver 2.3
%define sepol_ver 1.12.27
%define selinux_ver 1.30
%define sqlite_ver 3.2.0
%define swig_ver 1.3.28
%define tcltk_ver 8.4.9

%description
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This meta-package depends upon the main packages necessary to run
SETools.

%package libs
License: LGPLv2
Summary: Policy analysis support libraries for SELinux
Group: System/Libraries
Requires: selinux >= %{selinux_ver}
#Requires: libsepol >= %{sepol_ver} sqlite3 >= %{sqlite_ver}
Requires: usermode-consoleonly
BuildRequires: usermode-consoleonly
BuildRequires: flex bison pkgconfig
BuildRequires: glibc-devel libstdc++-devel gcc gcc-c++
BuildRequires: selinux-devel >= %{selinux_ver} sepol-devel >= %{sepol_ver} sepol-static-devel >= %{sepol_ver}
BuildRequires: sqlite3-devel >= %{sqlite_ver} libxml2-devel
BuildRequires: tcl-devel >= %{tcltk_ver}
BuildRequires: autoconf >= %{autoconf_ver} automake

%description libs
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following run-time libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package libs-python
License: LGPLv2
Summary: Python bindings for SELinux policy analysis
Group: Development/Python
Requires: setools-libs = %{version}-%{release}
%py_requires -d
BuildRequires: swig >= %{swig_ver}

%description libs-python
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Python bindings for the following libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package libs-java
License: LGPLv2
Summary: Java bindings for SELinux policy analysis
Group: Development/Java
Requires: setools-libs = %{version}-%{release}
BuildRequires: java-devel >= %{java_ver} swig >= %{swig_ver}
BuildRequires: java-rpmbuild jpackage-utils sharutils

%description libs-java
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Java bindings for the following libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package libs-tcl
License: LGPLv2
Summary: Tcl bindings for SELinux policy analysis
Group: Development/Other
Requires: setools-libs = %{version}-%{release}
BuildRequires: tcl-devel >= %{tcltk_ver} swig >= %{swig_ver}

%description libs-tcl
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes Tcl bindings for the following libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package devel
License: LGPLv2
Summary: Policy analysis development files for SELinux
Group: System/Libraries
Requires: selinux-devel >= %{selinux_ver} sepol-devel >= %{sepol_ver} sepol-static-devel >= %{sepol_ver} setools-libs = %{version}-%{release}
BuildRequires: sqlite3-devel >= %{sqlite_ver} libxml2-devel

%description devel
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes header files and archives for the following
libraries:

  libapol       policy analysis library
  libpoldiff    semantic policy difference library
  libqpol       library that abstracts policy internals
  libseaudit    parse and filter SELinux audit messages in log files
  libsefs       SELinux file contexts library

%package console
Summary: Policy analysis command-line tools for SELinux
Group: System/Base
License: GPLv2
Requires: setools-libs = %{version}-%{release}
Requires: selinux >= %{selinux_ver}

%description console
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following console tools:

  seaudit-report  audit log analysis tool
  sechecker       SELinux policy checking tool
  secmds          command line tools: seinfo, sesearch, findcon,
                  replcon, and indexcon
  sediff          semantic policy difference tool

%package gui
Summary: Policy analysis graphical tools for SELinux
Group: System/Base
Requires: tcl >= %{tcltk_ver} tk >= %{tcltk_ver} bwidget >= %{bwidget_ver}
Requires: setools-libs = %{version}-%{release} setools-libs-tcl = %{version}-%{release}
Requires: glib2 gtk2 >= %{gtk_ver} usermode-consoleonly
BuildRequires: gtk2-devel >= %{gtk_ver} libglade2-devel libxml2-devel tk-devel >= %{tcltk_ver}
BuildRequires: desktop-file-utils

%description gui
SETools is a collection of graphical tools, command-line tools, and
libraries designed to facilitate SELinux policy analysis.

This package includes the following graphical tools:

  apol          policy analysis tool
  seaudit       audit log analysis tool
  sediffx       semantic policy difference tool

%define setoolsdir %{_datadir}/setools-%{setools_maj_ver}
%define pkg_py_lib %{python_sitelib}/setools
%define pkg_py_arch %{python_sitearch}/setools
%define tcllibdir %{_libdir}/setools

%prep
%setup -q

%build
export LDFLAGS="-lpython%pyver -ltcl"
export CLASSPATH=
export JAR=%{jar}
export JAVA=%{java}
export JAVAC=%{javac}
%configure2_5x --disable-bwidget-check --disable-selinux-check --enable-swig-python --enable-swig-java --enable-swig-tcl
# work around issue with gcc 4.3 + gnu99 + swig-generated code:
sed -i -e 's:$(CC):gcc -std=gnu89:' libseaudit/swig/python/Makefile
%{__make}

%install
rm -rf ${RPM_BUILD_ROOT}
make DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p" install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/pixmaps
install -d -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d
install -p -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/pam.d/seaudit
install -d -m 755 ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps
install -p -m 644 packages/rpm/seaudit.console ${RPM_BUILD_ROOT}%{_sysconfdir}/security/console.apps/seaudit
install -d -m 755 ${RPM_BUILD_ROOT}%{_datadir}/applications
install -p -m 644 apol/apol.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/apol.png
install -p -m 644 seaudit/seaudit.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/seaudit.png
install -p -m 644 sediff/sediffx.png ${RPM_BUILD_ROOT}%{_datadir}/pixmaps/sediffx.png
desktop-file-install --dir ${RPM_BUILD_ROOT}%{_datadir}/applications %{SOURCE2} %{SOURCE3} %{SOURCE4}
ln -sf %{_bindir}/consolehelper ${RPM_BUILD_ROOT}/%{_bindir}/seaudit
# replace absolute symlinks with relative symlinks
ln -sf ../setools-%{setools_maj_ver}/qpol.jar ${RPM_BUILD_ROOT}/%{_javadir}/qpol-%{version}.jar
ln -sf ../setools-%{setools_maj_ver}/apol.jar ${RPM_BUILD_ROOT}/%{_javadir}/apol-%{version}.jar
ln -sf ../setools-%{setools_maj_ver}/poldiff.jar ${RPM_BUILD_ROOT}/%{_javadir}/poldiff-%{version}.jar
ln -sf ../setools-%{setools_maj_ver}/seaudit.jar ${RPM_BUILD_ROOT}/%{_javadir}/seaudit-%{version}.jar
ln -sf ../setools-%{setools_maj_ver}/sefs.jar ${RPM_BUILD_ROOT}/%{_javadir}/sefs-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do %{__ln_s} ${jar} `/bin/echo ${jar} | %{__sed} "s|-%{version}||g"`; done)
# remove static libs
rm -f ${RPM_BUILD_ROOT}/%{_libdir}/*.a
# ensure permissions are correct
chmod 0755 ${RPM_BUILD_ROOT}/%{_libdir}/*.so.*
chmod 0755 ${RPM_BUILD_ROOT}/%{_libdir}/%{name}/*/*.so.*
chmod 0755 ${RPM_BUILD_ROOT}/%{pkg_py_arch}/*.so.*
#chmod 0755 ${RPM_BUILD_ROOT}/%{_bindir}/*
chmod 0755 ${RPM_BUILD_ROOT}/%{_sbindir}/*
chmod 0755 ${RPM_BUILD_ROOT}/%{setoolsdir}/seaudit-report-service
chmod 0644 ${RPM_BUILD_ROOT}/%{tcllibdir}/*/pkgIndex.tcl

%if %{gcj_support}
%{_bindir}/aot-compile-rpm
%endif

%clean
rm -rf ${RPM_BUILD_ROOT}

%if %{gcj_support}
%post libs-java
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{update_gcjdb}

%postun libs-java
%if %mdkversion < 200900
/sbin/ldconfig
%endif
%{clean_gcjdb}
%endif

%if %mdkversion < 200900
%post libs -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun libs -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%post libs-tcl -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun libs-tcl -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root,-)

%files libs
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING COPYING.GPL COPYING.LGPL KNOWN-BUGS NEWS README
%{_libdir}/libqpol.so.*
%{_libdir}/libapol.so.*
%{_libdir}/libpoldiff.so.*
%{_libdir}/libsefs.so.*
%{_libdir}/libseaudit.so.*
%dir %{setoolsdir}

%files libs-python
%defattr(-,root,root,-)
%{pkg_py_lib}/
%ifarch x86_64 ppc64
%{pkg_py_arch}/
%endif

%files libs-java
%defattr(-,root,root,-)
%{_libdir}/libjqpol.so.*
%{_libdir}/libjapol.so.*
%{_libdir}/libjpoldiff.so.*
%{_libdir}/libjseaudit.so.*
%{_libdir}/libjsefs.so.*
%{setoolsdir}/*.jar
%{_javadir}/*.jar
%if %{gcj_support}
%dir %{_libdir}/gcj/%{name}
%attr(-,root,root) %{_libdir}/gcj/%{name}/*
%endif

%files libs-tcl
%defattr(-,root,root,-)
%{tcllibdir}/qpol/
%{tcllibdir}/apol/
%{tcllibdir}/poldiff/
%{tcllibdir}/seaudit/
%{tcllibdir}/sefs/

%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_includedir}/qpol/
%{_includedir}/apol/
%{_includedir}/poldiff/
%{_includedir}/seaudit/
%{_includedir}/sefs/

%files console
%defattr(-,root,root,-)
%{_bindir}/seinfo
%{_bindir}/sesearch
%{_bindir}/indexcon
%{_bindir}/findcon
%{_bindir}/replcon
%{_bindir}/sechecker
%{_bindir}/sediff
%{_bindir}/seaudit-report
%{setoolsdir}/sechecker-profiles/
%{setoolsdir}/sechecker_help.txt
%{setoolsdir}/seaudit-report-service
%{setoolsdir}/seaudit-report.conf
%{setoolsdir}/seaudit-report.css
%{_mandir}/man1/findcon.1*
%{_mandir}/man1/indexcon.1*
%{_mandir}/man1/replcon.1*
%{_mandir}/man1/sechecker.1*
%{_mandir}/man1/sediff.1*
%{_mandir}/man1/seinfo.1*
%{_mandir}/man1/sesearch.1*
%{_mandir}/man8/seaudit-report.8*

%files gui
%defattr(-,root,root,-)
%{_bindir}/seaudit
%{_bindir}/sediffx
%{_bindir}/apol
%{tcllibdir}/apol_tcl/
%{setoolsdir}/sediff_help.txt
%{setoolsdir}/apol_help.txt
%{setoolsdir}/domaintrans_help.txt
%{setoolsdir}/file_relabel_help.txt
%{setoolsdir}/infoflow_help.txt
%{setoolsdir}/types_relation_help.txt
%{setoolsdir}/apol_perm_mapping_*
%{setoolsdir}/seaudit_help.txt
%{setoolsdir}/*.glade
%{setoolsdir}/*.png
%{setoolsdir}/apol.gif
%{setoolsdir}/dot_seaudit
%{_mandir}/man1/apol.1*
%{_mandir}/man1/sediffx.1*
%{_mandir}/man8/seaudit.8*
%{_sbindir}/seaudit
%config(noreplace) %{_sysconfdir}/pam.d/seaudit
%config(noreplace) %{_sysconfdir}/security/console.apps/seaudit
%{_datadir}/applications/*
%attr(0644,root,root) %{_datadir}/pixmaps/*.png
