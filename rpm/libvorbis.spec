Name:       libvorbis
Summary:    The Vorbis General Audio Compression Codec
Version:    1.3.6
Release:    1
Group:      System/Libraries
License:    BSD
URL:        http://www.xiph.org/
Source0:    http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.xz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(ogg)
BuildRequires:  libtool

%description
%{summary}.


%package devel
Summary:    Development tools for Vorbis applications
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.


%package doc
Summary:   Documentation for %{name}
Group:     Documentation
Requires:  %{name} = %{version}-%{release}

%description doc
%{summary}.


%prep
%setup -q -n %{name}-%{version}/upstream


%build
%autogen
%configure --disable-static
make %{_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
install -m0644 -t %{buildroot}/%{_docdir}/%{name}-*/ AUTHORS README.md

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%license COPYING
%{_libdir}/libvorbis.so.*
%{_libdir}/libvorbisfile.so.*
%{_libdir}/libvorbisenc.so.*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/vorbis
%{_libdir}/libvorbis.so
%{_libdir}/libvorbisfile.so
%{_libdir}/libvorbisenc.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/vorbis.m4
# << files devel

%files doc
%defattr(-, root, root)
%doc %{_docdir}/%{name}-*/*
