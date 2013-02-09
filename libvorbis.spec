# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.25
# 

Name:       libvorbis

# >> macros
# << macros

Summary:    The Vorbis General Audio Compression Codec
Version:    1.3.3
Release:    1
Group:      System/Libraries
License:    BSD
URL:        http://www.xiph.org/
Source0:    http://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.xz
Source100:  libvorbis.yaml
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(ogg)

%description
%{summary}.


%package devel
Summary:    Development tools for Vorbis applications
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
%{summary}.



%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING README
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
