%define		pname	gst-python
Summary:	GStreamer Python bindings
Summary(pl):	Wi±zania jêzyka Python do GStreamera
Name:		python-gstreamer
Version:	0.10.4
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://gstreamer.freedesktop.org/src/gst-python/%{pname}-%{version}.tar.bz2
# Source0-md5:	73e1ebc4a84a6fae999da83fd625e833
Patch0:		%{pname}-py2pyc.patch
URL:		http://gstreamer.freedesktop.org/modules/gst-python.html
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gstreamer-devel >= 0.10.2
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.0.2
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libtool >= 1.4
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	python-pygtk-devel >= 2.6.3
BuildRequires:	python-devel >= 1:2.3
%pyrequires_eq	python-libs
Requires:	gstreamer >= 0.10.2
Requires:	gstreamer-plugins-base >= 0.10.0.2
Requires:	python-pygtk-gtk >= 2.6.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer Python bindings.

%description -l pl
Wi±zania jêzyka Python do GStreamera.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1

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
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean

cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
rm -f $RPM_BUILD_ROOT%{py_sitedir}/gst-*/gst/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS RELEASE TODO
%dir %{py_sitedir}/gst-*
%dir %{py_sitedir}/gst-*/gst
%attr(755,root,root) %{py_sitedir}/gst-*/gst/*.so
%{py_sitedir}/gst-*/gst/*.py[co]
%dir %{py_sitedir}/gst-*/gst/extend
%{py_sitedir}/gst-*/gst/extend/*.py[co]
%{py_sitedir}/pygst.pth
%{py_sitedir}/pygst.py[co]
%{_datadir}/gst-python
%{_pkgconfigdir}/gst-python-*.pc
%{_examplesdir}/%{name}-%{version}
