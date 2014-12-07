# revision 33736
# category TLCore
# catalog-ctan /systems/knuth/dist/mfware
# catalog-date 2014-02-26 23:03:13 +0100
# catalog-license knuth
# catalog-version undef
Name:		texlive-mfware
Version:	20140226
Release:	3
Summary:	Supporting tools for use with Metafont
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/systems/knuth/dist/mfware
License:	KNUTH
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfware.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mfware.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-mfware.bin

%description
A collection of programs (as web source) for processing the
output of Metafont.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/mft/base/README
%{_texmfdistdir}/mft/base/cmbase.mft
%{_texmfdistdir}/mft/base/mplain.mft
%{_texmfdistdir}/mft/base/pl.mft
%{_texmfdistdir}/mft/base/plain.mft
%doc %{_mandir}/man1/gftodvi.1*
%doc %{_texmfdistdir}/doc/man/man1/gftodvi.man1.pdf
%doc %{_mandir}/man1/gftopk.1*
%doc %{_texmfdistdir}/doc/man/man1/gftopk.man1.pdf
%doc %{_mandir}/man1/gftype.1*
%doc %{_texmfdistdir}/doc/man/man1/gftype.man1.pdf
%doc %{_mandir}/man1/mft.1*
%doc %{_texmfdistdir}/doc/man/man1/mft.man1.pdf
%doc %{_mandir}/man1/pktogf.1*
%doc %{_texmfdistdir}/doc/man/man1/pktogf.man1.pdf
%doc %{_mandir}/man1/pktype.1*
%doc %{_texmfdistdir}/doc/man/man1/pktype.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
