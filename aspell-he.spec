Summary:	Hebrew dictionary for aspell
Summary(pl):	S³ownik hebrajski dla aspella
Name:		aspell-he
Version:	0.8
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/he/aspell6-he-%{version}-%{subv}.tar.bz2
# Source0-md5:	00b164ea82e16aff51b2cb8425292514
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.60.0
Requires:	aspell >= 0.60.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hebrew dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik hebrajski (lista s³ów) dla aspella.

%prep
%setup -q -n aspell6-he-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
