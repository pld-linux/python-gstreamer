%define		pname	gst-python
Summary:	GStreamer Python bindings
Summary(pl):	Wi±zania jêzyka Python do GStreamera
Name:		python-gstreamer
Version:	0.8.1
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://gstreamer.freedesktop.org/src/%{pname}/%{pname}-%{version}.tar.gz
# Source0-md5:	4666978d610b48f7f7481e41433a856c
Patch0:		%{pname}-py2pyc.patch
URL:		http://gstreamer.freedesktop.org/modules/gst-python.html
BuildRequires:	gstreamer-devel >= 0.8.0
BuildRequires:	gstreamer-plugins-devel >= 0.8.0
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-progs
BuildRequires:	python-pygtk-devel >= 2.0.0
BuildRequires:	xmlto
%pyrequires_eq	python-libs
Requires:	gstreamer >= 0.8.0
Requires:	python-pygtk-gtk >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GStreamer Python bindings.

%description -l pl
Wi±zania jêzyka Python do GStreamera.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1

%build
%{__aclocal} -I common/m4/
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-docs

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -R examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%dir %{py_sitedir}/gst
%attr(755,root,root) %{py_sitedir}/gst/*.so
%{py_sitescriptdir}/gst/*py[co]
%{_pkgconfigdir}/*.pc
%{_datadir}/%{pname}
%{_examplesdir}/*
