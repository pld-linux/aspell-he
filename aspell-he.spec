Summary:	Hebrew dictionary for aspell
Summary(pl.UTF-8):   Słownik hebrajski dla aspella
Name:		aspell-he
Version:	1.0
%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/he/aspell6-he-%{version}-%{subv}.tar.bz2
# Source0-md5:	71791e0299787391d2ace1c850b5b434
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Hebrew dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik hebrajski (lista słów) dla aspella.

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
