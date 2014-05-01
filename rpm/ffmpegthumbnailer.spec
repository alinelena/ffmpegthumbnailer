Summary:       Lightweight video thumbnailer
Name:          ffmpegthumbnailer
Version:       0
Release:       0
License:       GPL
Group:         Applications/Graphics
Source:        http://ffmpegthumbnailer.googlecode.com/files/%{name}-%{version}.tar.gz
URL:           http://code.google.com/p/ffmpegthumbnailer/
BuildRequires: libav1-devel
BuildRequires: libjpeg-devel
BuildRequires: libtool

%description
ffmpegthumbnailer can be used by file managers to create thumbnails
for your video files. It uses ffmpeg to decode frames from the video
files.

%package devel
Summary: Header files for libffmpegthumbnailer library
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Header files for libffmpegthumbnailer library.

%package tools
Summary: libffmpegthumbnailer binary thumbnailer
Group: Applications/Graphics
Requires: %{name} = %{version}-%{release}

%description tools
libffmpegthumbnailer binary thumbnailer

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
# Not sure why but autogen.sh will fail without creating m4
mkdir m4
./autogen.sh
%configure \
    --enable-thumbnailer=no \
    --enable-png=no \
    --enable-gio=no \
    --enable-jpeg \
    --enable-shared \
    --disable-static

make %{?_smp_mflags}

%install
%make_install

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name '*.a' -exec rm -f {} ';'

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libffmpegthumbnailer.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libffmpegthumbnailer.so
%{_includedir}/libffmpegthumbnailer
%{_libdir}/pkgconfig/libffmpegthumbnailer.pc

%files tools
%defattr(-,root,root,-)
%{_bindir}/ffmpegthumbnailer
%{_mandir}/man1/ffmpegthumbnailer.1*
