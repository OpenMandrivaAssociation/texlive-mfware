%global tl_name mfware
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Supporting tools for Metafont: gftodvi, gftopk, gftype, mft
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/systems/knuth/dist/mfware
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfware.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mfware.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(mfware.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A collection of programs (as web source) for processing the output of
Metafont. They include: gftodvi (for making proof sheets of letters);
gftopk (translate gf bitmap files to pk bitmaps); gftype (human-readable
dump of gf files); mft (prettyprint Metafont source).

