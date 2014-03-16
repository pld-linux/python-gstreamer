#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		pname	gst-python
Summary:	GStreamer Python 2 bindings
Summary(pl.UTF-8):	Wiązania języka Python 2 do GStreamera
Name:		python-gstreamer
Version:	1.2.0
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
Source0:	http://gstreamer.freedesktop.org/src/gst-python/%{pname}-%{version}.tar.bz2
# Source0-md5:	da9a33cccdb7d094f243e4b469cfbc76
URL:		http://gstreamer.freedesktop.org/modules/gst-python.html
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake >= 1:1.10
BuildRequires:	gstreamer-devel >= 1.2.0
BuildRequires:	libtool >= 1.4
BuildRequires:	pkgconfig >= 1:0.9.0
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-pygobject3-devel >= 3.0
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 3.3
BuildRequires:	python3-pygobject3-devel >= 3.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.612
Requires:	gstreamer >= 1.2.0
Requires:	python-pygobject3 >= 3.0
Obsoletes:	python-gstreamer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer Python 2 bindings.

%description -l pl.UTF-8
Wiązania języka Python 2 do GStreamera.

%package -n python3-gstreamer
Summary:	GStreamer Python 3 bindings
Summary(pl.UTF-8):	Wiązania języka Python 3 do GStreamera
Group:		Libraries/Python
Requires:	gstreamer >= 1.2.0
Requires:	python3-pygobject3 >= 3.0

%description -n python3-gstreamer
GStreamer Python 3 bindings.

%description -n python3-gstreamer -l pl.UTF-8
Wiązania języka Python 3 do GStreamera.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}

%if %{with python2}
install -d python2
cd python2
../%configure \
	PYTHON="%{__python}" \
	--disable-silent-rules
%{__make}
cd ..
%endif

%if %{with python3}
install -d python3
cd python3
../%configure \
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

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{py_sitedir}/gi/overrides/_gi_gst.so
%{py_sitedir}/gi/overrides/Gst.py[co]
%{py_sitedir}/gi/overrides/GstPbutils.py[co]
%endif

%if %{with python3}
%files -n python3-gstreamer
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{py3_sitedir}/gi/overrides/_gi_gst.so
%{py3_sitedir}/gi/overrides/Gst.py
%{py3_sitedir}/gi/overrides/GstPbutils.py
%{py3_sitedir}/gi/overrides/__pycache__/Gst.*.py[co]
%{py3_sitedir}/gi/overrides/__pycache__/GstPbutils.*.py[co]
%endif
