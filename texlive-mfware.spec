# revision 23089
# category TLCore
# catalog-ctan /systems/knuth/dist/mfware
# catalog-date 2011-04-11 12:30:24 +0200
# catalog-license knuth
# catalog-version undef
Name:		texlive-mfware
Version:	20110411
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A collection of programs for processing the output of Metafont.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/mft/base/README
%{_texmfdistdir}/mft/base/cmbase.mft
%{_texmfdistdir}/mft/base/e.mft
%{_texmfdistdir}/mft/base/mplain.mft
%{_texmfdistdir}/mft/base/pl.mft
%{_texmfdistdir}/mft/base/plain.mft
%doc %{_mandir}/man1/gftodvi.1*
%doc %{_texmfdir}/doc/man/man1/gftodvi.man1.pdf
%doc %{_mandir}/man1/gftopk.1*
%doc %{_texmfdir}/doc/man/man1/gftopk.man1.pdf
%doc %{_mandir}/man1/gftype.1*
%doc %{_texmfdir}/doc/man/man1/gftype.man1.pdf
%doc %{_mandir}/man1/mft.1*
%doc %{_texmfdir}/doc/man/man1/mft.man1.pdf
%doc %{_mandir}/man1/pktogf.1*
%doc %{_texmfdir}/doc/man/man1/pktogf.man1.pdf
%doc %{_mandir}/man1/pktype.1*
%doc %{_texmfdir}/doc/man/man1/pktype.man1.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
