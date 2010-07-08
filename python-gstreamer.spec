%define		pname	gst-python
Summary:	GStreamer Python bindings
Summary(pl.UTF-8):	Wiązania języka Python do GStreamera
Name:		python-gstreamer
Version:	0.10.16
Release:	3
License:	LGPL v2+
Group:		Libraries/Python
Source0:	http://gstreamer.freedesktop.org/src/gst-python/%{pname}-%{version}.tar.bz2
# Source0-md5:	00cceddc81ff6cdc9838a5c40bbcf305
URL:		http://gstreamer.freedesktop.org/modules/gst-python.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	gstreamer-devel >= 0.10.16
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.16
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libtool >= 1.4
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	python-devel >= 1:2.3
BuildRequires:	python-pygobject-devel >= 2.11.2
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	glib2 >= 1:2.8.0
Requires:	gstreamer >= 0.10.16
Requires:	gstreamer-plugins-base >= 0.10.16
Requires:	python-pygobject >= 2.11.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer Python bindings.

%description -l pl.UTF-8
Wiązania języka Python do GStreamera.

%package devel
Summary:	Development files and examples for GStreamer Python bindings
Summary(pl.UTF-8):	Pliki programistyczne i przykłady dla wiązań Pythona do GStreamera
Group:		Development/Languages/Python
Requires:	%{name} = %{version}-%{release}

%description devel
Development files and examples for GStreamer Python bindings.

%description devel -l pl.UTF-8
Pliki programistyczne i przykłady dla wiązań Pythona do GStreamera.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	examplesdir=%{_examplesdir}/%{name}-%{version}

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean

rm -f $RPM_BUILD_ROOT%{_libdir}/gstreamer-*/*.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/gst-*/gst/*.la
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS RELEASE TODO
%attr(755,root,root) %{_libdir}/gstreamer-*/libgstpython.so
%dir %{py_sitedir}/gst-*
%dir %{py_sitedir}/gst-*/gst
%attr(755,root,root) %{py_sitedir}/gstoption.so
%attr(755,root,root) %{py_sitedir}/gst-*/gst/_gst.so
%attr(755,root,root) %{py_sitedir}/gst-*/gst/audio.so
%attr(755,root,root) %{py_sitedir}/gst-*/gst/tag.so
%attr(755,root,root) %{py_sitedir}/gst-*/gst/video.so
%attr(755,root,root) %{py_sitedir}/gst-*/gst/interfaces.so
%attr(755,root,root) %{py_sitedir}/gst-*/gst/pbutils.so
%{py_sitedir}/gst-*/gst/__init__.py[co]
%dir %{py_sitedir}/gst-*/gst/extend
%{py_sitedir}/gst-*/gst/extend/*.py[co]
%{py_sitedir}/pygst.pth
%{py_sitedir}/pygst.py[co]

%files devel
%defattr(644,root,root,755)
%dir %{_datadir}/gst-python
%dir %{_datadir}/gst-python/0.10
%{_datadir}/gst-python/0.10/defs
%{_pkgconfigdir}/gst-python-0.10.pc
%{_examplesdir}/%{name}-%{version}
