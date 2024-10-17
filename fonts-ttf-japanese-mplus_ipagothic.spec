%define version	20060520
%define release	11
%define fontdir %_datadir/fonts/TTF/japanese-mplus_ipagothic

Name:		fonts-ttf-japanese-mplus_ipagothic
Summary:	M+ OUTLINE FONTS with IPA gothic for Japanese
Version:	%{version}
Release:	%{release}
Group:		System/Fonts/True type
License:	Distributable
URL:		https://mix-mplus-ipa.sourceforge.jp/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires(post): mkfontdir, mkfontscale
BuildArch:	noarch
BuildRequires: fontconfig

%description
M+ OUTLINE FONTS don't have Kanji,
so "M+ with IPA gothic" use IPA gothic for Kanji.


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d %{buildroot}/%{fontdir}
install -m 644 *.ttf %{buildroot}/%{fontdir}

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%fontdir \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-japanese-mplus_ipagothic:pri=50

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{fontdir}
mkfontdir
mkfontscale
cd -

%preun
rm -f %fontdir/fonts.{dir,scale}

%files
%defattr(-,root,root)
%doc COPYING.font.ja *.txt
%doc opfc-ModuleHP-1.1.1_withIPAFonts_and_Mplus.tar.bz2
%{fontdir}/*.ttf
%_sysconfdir/X11/fontpath.d/*


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 20060520-10mdv2011.0
+ Revision: 675573
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 20060520-9mdv2011.0
+ Revision: 610733
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 20060520-8mdv2010.1
+ Revision: 494146
- fc-cache is now called by an rpm filetrigger

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 20060520-7mdv2010.0
+ Revision: 428848
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 20060520-6mdv2009.0
+ Revision: 245261
- rebuild

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 20060520-5mdv2009.0
+ Revision: 239585
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 20060520-3mdv2008.1
+ Revision: 125136
- kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Funda Wang <fwang@mandriva.org> 20060520-3mdv2008.0
+ Revision: 68102
- Adopt to new font policy

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 20060520-2mdv2008.0
+ Revision: 67831
- rebuild


* Mon Jul 24 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20060520-1mdv2007.0
- new release

* Mon May 01 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 20060427-1mdk
- new release
- add some fonts
- change URL

* Tue Feb 21 2006 UTUMI Hirosi <utuhiro78@yahoo.co.jp> 0.0.0.10-1mdk
- first spec for Mandriva Linux
- mplus-TESTFLIGHT-010

