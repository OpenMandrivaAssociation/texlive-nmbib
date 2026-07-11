%global tl_name nmbib
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.05
Release:	%{tl_revision}.1
Summary:	Multiple versions of a bibliography, with different sort orders
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nmbib
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nmbib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nmbib.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nmbib.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is a rewrite of the multibibliography package providing
multiple bibliographies with different sorting. The new version offers a
number of citation commands, streamlines the creation of bibliographies,
ensures compatibility with the natbib package, and provides other
improvements.

