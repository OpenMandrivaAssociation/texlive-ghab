Name:		texlive-ghab
Version:	29803
Release:	2
Summary:	Typeset ghab boxes in LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ghab
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ghab.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ghab.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
