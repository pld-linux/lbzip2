Summary:	Parallel bzip2/bunzip2 Filter
Name:		lbzip2
Version:	2.5
Release:	1
Source0:	https://github.com/kjn/lbzip2/archive/v%{version}.tar.gz
# Source0-md5:	288e404f325d9073bdc80759cae30adc
License:	GPL v2+
Group:		Applications/Archiving
URL:		http://lbzip2.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnulib
BuildRequires:	perl-base
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lbzip2 is a Pthreads-based parallel bzip2/bunzip2 filter, passable to
GNU tar with the --use-compress-program option.

It isn't restricted to regular files on input, nor output. Successful
splitting for decompression isn't guaranteed, just very likely
(failure is detected). Splitting in both modes and compression itself
occur with an approximate 900k block size.

On an Athlon-64 X2 6000+, lbzip2 was 92% faster than standard bzip2
when compressing, and 45% faster when decompressing (based on wall
clock time).

Lbzip2 strives to be portable by requiring UNIX 98 APIs only, besides
an unmodified libbz2.

%prep
%setup -q

%build
./build-aux/autogen.sh
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ALGORITHM AUTHORS ChangeLog* NEWS THANKS
%attr(755,root,root) %{_bindir}/lbzip2
%attr(755,root,root) %{_bindir}/lbunzip2
%attr(755,root,root) %{_bindir}/lbzcat
%{_mandir}/man1/lbzip2.1*
%{_mandir}/man1/lbunzip2.1*
%{_mandir}/man1/lbzcat.1*
