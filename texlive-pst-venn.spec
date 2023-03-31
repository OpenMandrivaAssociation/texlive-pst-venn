Name:		texlive-pst-venn
Version:	49316
Release:	2
Summary:	A PSTricks package for drawing Venn sets
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pst-venn
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-venn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-venn.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a PSTricks related package for drawing Venn diagrams
with three circles.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/pst-venn
%doc %{_texmfdistdir}/doc/generic/pst-venn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
