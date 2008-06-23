%include	/usr/lib/rpm/macros.perl
Summary:	Any delimited text to HTML table converter
Summary(pl.UTF-8):	Konwerter dowolnego tekstu z separatorami na tabele HTML
Name:		t2t
Version:	6.0
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.scholnick.net/t2t/%{name}-%{version}.tar.gz
# Source0-md5:	720651be6a59f637b43337283f7637f3
URL:		http://www.scholnick.net/t2t/
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
t2t can convert any delimited text file to an HTML table. It supports
all attributes for the various table-related tags. It can read its
input either from stdin, a file, or a whole directory. When t2t is
passed in a directory, it will process all the files (except those
with either .html or .htm extension), and all the files in all the
sub-directories. It works on any system with Perl.

%description -l pl.UTF-8
t2t konwertuje dowolne pliki tekstowe z separatorami na tabele HTML.
Obsługuje wszystkie atrybuty dla różnych znaczników związanych z
tabelami. Może czytać ze standardowego wejścia, z pliku lub całego
katalogu. W tym ostatnim przypadku przetwarza wszystkie pliki (poza
mającymi już rozszerzenie .html lub .htm) oraz wszystkie pliki z
podkatalogów. Działa na dowolnym systemie z interpreterem Perla.

%prep
%setup -q

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
