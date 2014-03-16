%define		pname	gst-python
Summary:	GStreamer Python bindings
Summary(pl.UTF-8):	Wiązania języka Python do GStreamera
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
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-pygobject3-devel >= 3.0
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	gstreamer >= 1.2.0
Requires:	python-pygobject3 >= 3.0
Obsoletes:	python-gstreamer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer Python bindings.

%description -l pl.UTF-8
Wiązania języka Python do GStreamera.

%prep
%setup -q -n %{pname}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I common/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean

%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gi/overrides/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{py_sitedir}/gi/overrides/_gi_gst.so
%{py_sitedir}/gi/overrides/Gst.py[co]
%{py_sitedir}/gi/overrides/GstPbutils.py[co]
