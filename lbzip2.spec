Summary:	Parallel bzip2/bunzip2 Filter
Name:		lbzip2
Version:	0.23
Release:	1
Source0:	http://lacos.web.elte.hu/pub/lbzip2/%{name}-%{version}.tar.gz
# Source0-md5:	72ab7fbfd3804e4ef1a2030f51ac3825
Patch1:		%{name}-makefile.patch
License:	GPL v2+
Group:		Applications/Archiving
URL:		http://lacos.hu/
BuildRequires:	bzip2-devel
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
%setup -q -n %{name}
%patch1

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D lbzip2 $RPM_BUILD_ROOT%{_bindir}/lbzip2
install -D lbzip2.1 $RPM_BUILD_ROOT%{_mandir}/man1/lbzip2.1

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/lbzip2
%{_mandir}/man1/lbzip2.1*
