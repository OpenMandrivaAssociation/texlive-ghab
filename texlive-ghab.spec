# revision 24412
# category Package
# catalog-ctan /macros/latex/contrib/ghab
# catalog-date 2011-10-27 14:58:36 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-ghab
Version:	0.2
Release:	1
Summary:	Typeset ghab boxes in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ghab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ghab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ghab.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package defines a command \darghab that will typeset its
argument in a box with a decorated frame. The width of the box
may be set using an optional argument.

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
%{_texmfdistdir}/fonts/source/public/ghab/ghab.mf
%{_texmfdistdir}/tex/latex/ghab/ghab.sty
%doc %{_texmfdistdir}/doc/latex/ghab/README
%doc %{_texmfdistdir}/doc/latex/ghab/ghab-doc.pdf
%doc %{_texmfdistdir}/doc/latex/ghab/ghab-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
