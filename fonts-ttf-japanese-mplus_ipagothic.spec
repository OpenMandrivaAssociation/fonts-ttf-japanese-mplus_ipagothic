%define version	20060520
%define release	%mkrel 1

Name:		fonts-ttf-japanese-mplus_ipagothic
Summary:	M+ OUTLINE FONTS with IPA gothic for Japanese
Version:	%{version}
Release:	%{release}
Group:		System/Fonts/True type
License:	Distributable
URL:		http://mix-mplus-ipa.sourceforge.jp/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch

%description
M+ OUTLINE FONTS don't have Kanji,
so "M+ with IPA gothic" use IPA gothic for Kanji.


%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

install -d %{buildroot}/%{_datadir}/fonts/ttf/japanese
install -m 644 *.ttf %{buildroot}/%{_datadir}/fonts/ttf/japanese/

%clean
rm -rf $RPM_BUILD_ROOT

%post
cd %{_datadir}/fonts/ttf/japanese/
fc-cache -f .
ttmkfdir > fonts.dir
/sbin/service xfs restart

%postun
cd %{_datadir}/fonts/ttf/japanese/
fc-cache -f .
ttmkfdir > fonts.dir
/sbin/service xfs restart


%files
%defattr(-,root,root)
%doc COPYING.font.ja *.txt
%doc opfc-ModuleHP-1.1.1_withIPAFonts_and_Mplus.tar.bz2
%{_datadir}/fonts/ttf/japanese/*.ttf


