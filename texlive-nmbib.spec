Name:		texlive-nmbib
Version:	71138
Release:	1
Summary:	Multiple versions of a bibliography, with different sort orders
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nmbib
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nmbib.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nmbib.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nmbib.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is a rewrite of the multibibliography package
providing multiple bibliographies with different sorting. The
new version offers a number of citation commands, streamlines
the creation of bibliographies, ensures compatibility with the
natbib package, and provides other improvements.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/nmbib
%{_texmfdistdir}/tex/latex/nmbib
%{_texmfdistdir}/bibtex/bst/nmbib
%doc %{_texmfdistdir}/doc/latex/nmbib

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
