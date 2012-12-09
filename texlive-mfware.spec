# revision 26689
# category TLCore
# catalog-ctan /systems/knuth/dist/mfware
# catalog-date 2011-04-11 12:30:24 +0200
# catalog-license knuth
# catalog-version undef
Name:		texlive-mfware
Version:	20110411
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
A collection of programs for processing the output of Metafont.

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

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1


%changelog
* Wed Aug 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110411-3
+ Revision: 812586
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110411-2
+ Revision: 753977
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110411-1
+ Revision: 719014
- texlive-mfware
- texlive-mfware
- texlive-mfware
- texlive-mfware

