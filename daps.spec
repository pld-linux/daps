# TODO:
# - svg dtds ("-//W3C//DTD SVG 1.0//EN", "-//W3C//DTD SVG 1.1 Basic//EN")
# - oodraw?
Summary:	DAPS: DocBook Authoring and Publishing Suite
Summary(pl.UTF-8):	DAPS - zestaw narzędzi do tworzenia i publikowania dokumentów w DocBooku
Name:		daps
Version:	3.0.0
Release:	1
License:	GPL v2 or GPL v3
Group:		Applications/Publishing
#Source0Download: https://github.com/openSUSE/daps/releases
Source0:	https://github.com/openSUSE/daps/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	abb853ba10ecd5c3f8d8edf0dc61b65a
URL:		https://opensuse.github.io/daps/
BuildRequires:	ImageMagick
BuildRequires:	docbook-style-xsl-nons >= 1.78
BuildRequires:	docbook-style-xsl-ns >= 1.78
BuildRequires:	docbook-dtd45-xml
BuildRequires:	docbook-dtd51-xml >= 5.1-2
BuildRequires:	jing
BuildRequires:	libxml2-progs
BuildRequires:	python3 >= 1:3.4
BuildRequires:	python3-lxml >= 3.4.0
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	ruby-asciidoctor
BuildRequires:	sed >= 4.0
BuildRequires:	sgml-common
BuildRequires:	xmlstarlet
Requires:	ImageMagick
Requires:	docbook-style-xsl-nons >= 1.78
Requires:	docbook-style-xsl-ns >= 1.78
Requires:	docbook-dtd45-xml
Requires:	docbook-dtd51-xml >= 5.1-2
Requires:	ghostscript
Requires:	jing
Requires:	jpackage-utils
Requires:	libxslt-progs
Requires:	make
Requires:	python3 >= 1:3.4
Requires:	python3-lxml >= 3.4.0
Requires:	sgml-common
Requires:	xmlstarlet
Requires:	zip
Suggests:	dia
Suggests:	fop >= 1.0
Suggests:	inkscape
#Suggests:	oodraw
Suggests:	optipng
Suggests:	perl-Image-ExifTool
Suggests:	poppler-progs
Suggests:	saxon
Suggests:	xfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A complete environment to build HTML, PDF, EPUB and other formats from
DocBook XML. Documentation is available at
<https://opensuse.github.io/daps/doc/index.html>.

%description -l pl.UTF-8
Pełne środowisko do budowania dokumentów w formatach HTML, PDF, EPUB i
innych z formatu DocBook XML. Dokumentacja jest dostępna pod
<https://opensuse.github.io/daps/doc/index.html>.

%package -n bash-completion-daps
Summary:	Bash completion for daps command
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów polecenia daps
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-daps
Bash completion for daps command.

%description -n bash-completion-daps -l pl.UTF-8
Bashowe dopełnianie parametrów polecenia daps.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' libexec/daps-xmlwellformed

%build
%configure \
	DIA=/usr/bin/dia \
	EXIFTOOL=/usr/bin/exiftool \
	GS=/usr/bin/gs \
	INKSCAPE=/usr/bin/inkscape \
	OPTIPNG=/usr/bin/optipng \
	PDFFONTS=/usr/bin/pdffonts \
	XFIG=/usr/bin/xfig \
	--disable-edit-rootcatalog
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/daps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING ChangeLog README.adoc README.quickstart.adoc TODO TROUBLESHOOTING doc/build/{daps-asciidoc/single-html/daps-asciidoc,daps-quick/single-html/daps-quick,daps-user/single-html/daps-user}
%attr(755,root,root) %{_bindir}/ccecho
%attr(755,root,root) %{_bindir}/daps
%attr(755,root,root) %{_bindir}/daps-auto.pl
%attr(755,root,root) %{_bindir}/daps-autobuild
%attr(755,root,root) %{_bindir}/daps-check-deps
%attr(755,root,root) %{_bindir}/daps-init
%attr(755,root,root) %{_bindir}/daps-xmlformat
%dir %{_sysconfdir}/daps
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daps/CatalogManager.properties
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daps/config
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daps/docbook-xmlformat.conf
%dir %{_sysconfdir}/daps/fop
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daps/fop/fop-daps.xml
%dir %{_sysconfdir}/daps/xep
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/daps/xep/xep-daps.xml
%dir %{_sysconfdir}/daps/xep/hyphen
%{_sysconfdir}/daps/xep/hyphen/czhyphen.il2
%{_sysconfdir}/daps/xep/hyphen/dehyph_rx.tex
%{_sysconfdir}/daps/xep/hyphen/dkcommon.tex
%{_sysconfdir}/daps/xep/hyphen/eshyph_rx.tex
%{_sysconfdir}/daps/xep/hyphen/huhyph_rx.tex
%{_sysconfdir}/daps/xep/hyphen/hyphen_rx.tex
%{_sysconfdir}/daps/xep/hyphen/ithyph_rx.tex
%{_sysconfdir}/daps/xep/hyphen/plhyph_rx.tex
%{_sysconfdir}/daps/xep/hyphen/ruhyphal.tex
# TODO: add catalog.d support to PLD
#%{_sysconfdir}/xml/catalog.d/daps.xml
%dir %{_datadir}/daps
%{_datadir}/daps/daps-xslt
%{_datadir}/daps/init_templates
%{_datadir}/daps/lib
%dir %{_datadir}/daps/libexec
%attr(755,root,root) %{_datadir}/daps/libexec/daps-fop
%attr(755,root,root) %{_datadir}/daps/libexec/daps-jing
%attr(755,root,root) %{_datadir}/daps/libexec/daps-migrate
%attr(755,root,root) %{_datadir}/daps/libexec/daps-xep
%attr(755,root,root) %{_datadir}/daps/libexec/daps-xmlwellformed
%attr(755,root,root) %{_datadir}/daps/libexec/daps-xslt
%attr(755,root,root) %{_datadir}/daps/libexec/entities-exchange.sh
%attr(755,root,root) %{_datadir}/daps/libexec/getentityname.py
%attr(755,root,root) %{_datadir}/daps/libexec/webhelpindexer
%attr(755,root,root) %{_datadir}/daps/libexec/xml_cat_resolver
%{_datadir}/daps/libexec/daps-xmlwellformed-xinclude.xsl
%{_datadir}/daps/make
%{_datadir}/xml/daps
%{_mandir}/man1/ccecho.1*
%{_mandir}/man1/daps.1*
%{_mandir}/man1/daps-autobuild.1*
%{_mandir}/man1/daps-init.1*

%files -n bash-completion-daps
%defattr(644,root,root,755)
%{bash_compdir}/daps

# -n emacs-docbook?
#%{_datadir}/emacs/site-lisp/docbook_macros.el
