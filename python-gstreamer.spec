#
# Conditional build:
%bcond_without	python2		# CPython 2.x module and plugin
%bcond_with	python3		# CPython 3.x module and plugin

%define		gst_ver	1.16.3
%define		pname	gst-python
Summary:	GStreamer Python 2 bindings
Summary(pl.UTF-8):	Wiązania języka Python 2 do GStreamera
Name:		python-gstreamer
# keep 1.16.x here (1.18+ is python3-only, see python3-gstreamer.spec)
Version:	1.16.3
Release:	6
License:	LGPL v2+
Group:		Libraries/Python
Source0:	https://gstreamer.freedesktop.org/src/gst-python/%{pname}-%{version}.tar.xz
# Source0-md5:	326f4f4c23e2477bf3d5839c465a42ca
Patch0:		%{name}-nosegv.patch
URL:		https://gstreamer.freedesktop.org/modules/gst-python.html
BuildRequires:	autoconf >= 2.68
BuildRequires:	automake >= 1:1.11
BuildRequires:	gstreamer-devel >= %{gst_ver}
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig >= 1:0.9.0
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-pygobject3-devel >= 3.8
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-pygobject3-devel >= 3.8
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gstreamer >= %{gst_ver}
Requires:	python-pygobject3 >= 3.8
Obsoletes:	python-gstreamer-devel < 1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer Python 2 bindings.

%description -l pl.UTF-8
Wiązania języka Python 2 do GStreamera.

%package -n gstreamer-python
Summary:	GStreamer plugin to load plugins written in Python 2
Summary(pl.UTF-8):	Wtyczka GStreamera do wczytywania wtyczek napisanych w Pythonie 2
Group:		Libraries
Requires:	python-gstreamer = %{version}-%{release}

%description -n gstreamer-python
GStreamer plugin to load plugins written in Python 2.

%description -n gstreamer-python -l pl.UTF-8
Wtyczka GStreamera do wczytywania wtyczek napisanych w Pythonie 2.

%package -n python3-gstreamer
Summary:	GStreamer Python 3 bindings
Summary(pl.UTF-8):	Wiązania języka Python 3 do GStreamera
Group:		Libraries/Python
Requires:	gstreamer >= %{gst_ver}
Requires:	python3-pygobject3 >= 3.8

%description -n python3-gstreamer
GStreamer Python 3 bindings.

%description -n python3-gstreamer -l pl.UTF-8
Wiązania języka Python 3 do GStreamera.

%package -n gstreamer-python3
Summary:	GStreamer plugin to load plugins written in Python 3
Summary(pl.UTF-8):	Wtyczka GStreamera do wczytywania wtyczek napisanych w Pythonie 3
Group:		Libraries
Requires:	python3-gstreamer = %{version}-%{release}

%description -n gstreamer-python3
GStreamer plugin to load plugins written in Python 3.

%description -n gstreamer-python3 -l pl.UTF-8
Wtyczka GStreamera do wczytywania wtyczek napisanych w Pythonie 3.

%prep
%setup -q -n %{pname}-%{version}
%patch -P0 -p1

%build
%define configuredir ..
%if %{with python2}
install -d python2
cd python2
%configure \
	PYTHON="%{__python}" \
	--disable-silent-rules
%{__make}
cd ..
%endif

%if %{with python3}
install -d python3
cd python3
%configure \
	PYTHON="%{__python3}" \
	--disable-silent-rules
%{__make}
cd ..
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%{__make} -C python2 install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gi/overrides/*.la
%endif

%if %{with python3}
%{__make} -C python3 install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/gi/overrides/*.la
%endif

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/libgstpython.la
install -d $RPM_BUILD_ROOT%{_libdir}/gstreamer-1.0/python

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{py_sitedir}/gi/overrides/_gi_gst.so
%{py_sitedir}/gi/overrides/Gst.py[co]
%{py_sitedir}/gi/overrides/GstPbutils.py[co]

%files -n gstreamer-python
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstpython.so
%dir %{_libdir}/gstreamer-1.0/python
%endif

%if %{with python3}
%files -n python3-gstreamer
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{py3_sitedir}/gi/overrides/_gi_gst.cpython-*.so
%{py3_sitedir}/gi/overrides/Gst.py
%{py3_sitedir}/gi/overrides/GstPbutils.py
%{py3_sitedir}/gi/overrides/__pycache__/Gst.*.py[co]
%{py3_sitedir}/gi/overrides/__pycache__/GstPbutils.*.py[co]

%files -n gstreamer-python3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gstreamer-1.0/libgstpython.cpython-3*.so
%dir %{_libdir}/gstreamer-1.0/python
%endif
