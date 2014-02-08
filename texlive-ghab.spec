# revision 24578
# category Package
# catalog-ctan /macros/latex/contrib/ghab
# catalog-date 2011-11-11 07:02:55 +0100
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-ghab
Version:	0.4
Release:	3
Summary:	Typeset ghab boxes in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ghab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ghab.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ghab.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a command \darghab that will typeset its
argument in a box with a decorated frame. The width of the box
may be set using an optional argument.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/ghab/ghab.mf
%{_texmfdistdir}/tex/latex/ghab/ghab.sty
%doc %{_texmfdistdir}/doc/latex/ghab/README
%doc %{_texmfdistdir}/doc/latex/ghab/ghab-doc.pdf
%doc %{_texmfdistdir}/doc/latex/ghab/ghab-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.4-2
+ Revision: 752313
- Rebuild to reduce used resources

* Tue Nov 22 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.4-1
+ Revision: 732519
- texlive-ghab

* Thu Nov 10 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.3-1
+ Revision: 729659
- texlive-ghab

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 718554
- texlive-ghab
- texlive-ghab
- texlive-ghab
- texlive-ghab

