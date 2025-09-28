#
# Conditional build:
%bcond_with	tests	# unit tests (require DISPLAY, some failing)
#
%define		pdir	Tk
%define		pnam	Zinc
Summary:	Tk::Zinc - another Canvas which proposes many new functions, some based on OpenGL
Summary(pl.UTF-8):	Tk::Zinc - kolejna klasa Canvas z wieloma nowymi funkcjami, niektórymi opartymi na OpenGL
Name:		perl-Tk-Zinc
Version:	3.306
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Tk/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3c3e646795e7ab3d45bdeada4566aa09
URL:		https://metacpan.org/dist/Tk-Zinc
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.98
BuildRequires:	perl-Tk-devel >= 800.004
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
%if %{with tests}
BuildRequires:	perl-Test-Simple >= 0.98
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Zinc widget is very similar to Tk Canvas in that it supports
structured graphics. Like the Canvas, Tk::Zinc implements items used
to display graphical entities. Those items can be manipulated and
bindings can be associated with them to implement interaction
behaviors. But unlike the Canvas, TkZinc can structure the items in a
hierarchy (with the use of group items), has support for affine 2D
transforms (i.e. translation, scaling, and rotation), clipping can be
set for sub-trees of the item hierarchy, the item set is quite more
powerful including field specific items for Air Traffic systems and
new rendering techniques such as transparency and gradients.

%description -l pl.UTF-8
Widżet Zinc jest bardzo podobny do Tk Canvas o tyle, że obsługuje
strukturową grafikę. Podobnie do Canvas implementuje elementy służące
do wyświetlania figur graficznych. Można nimi operować i powiązać z
interakcją. Ale w przeciwieństwie do Canvas, Tk::Zinc potrafi
ustrukturyzować elementy w hierarchię (z użyciem elementów
grupujących), ma obsługę przekształceń afinicznych 2D (przesunięć,
skalowania i obrotów), obcinania dla poddrzew hierarchii elementów, a
zbiór elementów ma większe możliwości, w tym elementy dla systemów
ruchu lotniczego czy nowe techniki renderowania, takie jak
przezroczystość czy gradienty.

%package demos
Summary:	Demonstration programs for Tk::Zinc widget functionality
Summary(pl.UTF-8):	Programy demonstrujące funkcjonalność widżetów Tk::Zinc
Group:		Development/Languages/Perl
Requires:	%{name} = %{version}-%{release}

%description demos
Demonstration programs for Tk::Zinc widget functionality.

%description demos -l pl.UTF-8
Programy demonstrujące funkcjonalność widżetów Tk::Zinc.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{perl_vendorarch}/Tk/Zinc.pm
%{perl_vendorarch}/Tk/Zinc
%dir %{perl_vendorarch}/auto/Tk/Zinc
%attr(755,root,root) %{perl_vendorarch}/auto/Tk/Zinc/Zinc.so
%{_mandir}/man3/Tk::Zinc.3pm*
%{_mandir}/man3/Tk::Zinc::*.3pm*

%files demos
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/zinc-demos
# script uses `Tk->findINC('demos/widget_lib')`, so don't change location
%dir %{perl_vendorarch}/Tk/demos
%{perl_vendorarch}/Tk/demos/zinc_contrib_lib
%{perl_vendorarch}/Tk/demos/zinc_data
%dir %{perl_vendorarch}/Tk/demos/zinc_lib
%attr(755,root,root) %{perl_vendorarch}/Tk/demos/zinc_lib/*.pl
%{perl_vendorarch}/Tk/demos/zinc_pm
%{_mandir}/man1/zinc-demos.1p*
