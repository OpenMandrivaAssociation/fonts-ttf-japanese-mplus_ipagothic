%define version	20060520
%define release	%mkrel 9
%define fontdir %_datadir/fonts/TTF/japanese-mplus_ipagothic

Name:		fonts-ttf-japanese-mplus_ipagothic
Summary:	M+ OUTLINE FONTS with IPA gothic for Japanese
Version:	%{version}
Release:	%{release}
Group:		System/Fonts/True type
License:	Distributable
URL:		http://mix-mplus-ipa.sourceforge.jp/
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
