%include	/usr/lib/rpm/macros.perl
Summary:	Any delimited text to HTML table converter
#Summary(pl.UTF-8):	-
Name:		t2t
Version:	6.0
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.scholnick.net/t2t/%{name}-%{version}.tar.gz
URL:		http://www.scholnick.net/t2t/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
t2t can convert any delimited text file to an HTML table. It supports
all attributes for the various table-related tags. It can read its
input either from stdin, a file, or a whole directory. when t2t is
passed in a directory, it will process all the files (except those
with either .html or .htm extension), and all the files in all the
sub-directories. It works on any system with Perl.

#description -l pl.UTF-8

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/T2t
install T2t/* $RPM_BUILD_ROOT%{perl_vendorlib}/T2t
install -D t2t.pl $RPM_BUILD_ROOT%{_bindir}/t2t
install -D t2t.1 $RPM_BUILD_ROOT%{_mandir}/man1/t2t.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.html t2t.rc
%attr(755,root,root) %{_bindir}/t2t
%dir %{perl_vendorlib}/T2t
%{perl_vendorlib}/T2t/*.pm
%{_mandir}/man1/*.1*
