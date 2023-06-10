#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.04.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		ktp-common-internals
Summary:	ktp-common-internals
Name:		ka5-%{kaname}
Version:	23.04.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	e8526ce3585d1b445ab0bf3d69f6c16e
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-knotifyconfig-devel >= %{kframever}
BuildRequires:	kf5-kpeople-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-kwallet-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	libotr-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-qt5-devel >= 0.9.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Library for KTp.

%description -l pl.UTF-8
Biblioteka dla KTp.

%package devel
Summary:	Header files for %{kaname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kaname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktp-debugger
%attr(755,root,root) %{_libdir}/libKTpCommonInternals.so.*.*.*
%ghost %{_libdir}/libKTpCommonInternals.so.9
%attr(755,root,root) %{_libdir}/libKTpLogger.so.*.*.*
%ghost %{_libdir}/libKTpLogger.so.9
%attr(755,root,root) %{_libdir}/libKTpModels.so.*.*.*
%ghost %{_libdir}/libKTpModels.so.9
%attr(755,root,root) %{_libdir}/libKTpOTR.so.*.*.*
%ghost %{_libdir}/libKTpOTR.so.9
%attr(755,root,root) %{_libdir}/libKTpWidgets.so.*.*.*
%ghost %{_libdir}/libKTpWidgets.so.9
%dir %{_libdir}/qt5/plugins/kaccounts/daemonplugins
%attr(755,root,root) %{_libdir}/qt5/plugins/kaccounts/daemonplugins/kaccounts_ktp_plugin.so
%dir %{_libdir}/qt5/plugins/kpeople/actions
%attr(755,root,root) %{_libdir}/qt5/plugins/kpeople/actions/ktp_kpeople_plugin.so
%dir %{_libdir}/qt5/plugins/kpeople/datasource
%attr(755,root,root) %{_libdir}/qt5/plugins/kpeople/datasource/im_persons_data_source_plugin.so
%dir %{_libdir}/qt5/plugins/kpeople
%dir %{_libdir}/qt5/plugins/kpeople/widgets
%attr(755,root,root) %{_libdir}/qt5/plugins/kpeople/widgets/imdetailswidgetplugin.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kpeople/widgets/kpeople_chat_plugin.so
%dir %{_libdir}/qt5/qml/org/kde/telepathy
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/telepathy/libktpqmlplugin.so
%attr(755,root,root) %{_prefix}/libexec/ktp-proxy
%{_libdir}/qt5/qml/org/kde/telepathy/qmldir
%{_iconsdir}/hicolor/128x128/apps/telepathy-kde.png
%{_iconsdir}/hicolor/16x16/actions/im-groupwise.png
%{_iconsdir}/hicolor/16x16/actions/im-irc.png
%{_iconsdir}/hicolor/16x16/actions/im-local-xmpp.png
%{_iconsdir}/hicolor/16x16/apps/telepathy-kde.png
%{_iconsdir}/hicolor/22x22/actions/im-aim.png
%{_iconsdir}/hicolor/22x22/actions/im-facebook.png
%{_iconsdir}/hicolor/22x22/actions/im-gadugadu.png
%{_iconsdir}/hicolor/22x22/actions/im-google-talk.png
%{_iconsdir}/hicolor/22x22/actions/im-groupwise.png
%{_iconsdir}/hicolor/22x22/actions/im-icq.png
%{_iconsdir}/hicolor/22x22/actions/im-jabber.png
%{_iconsdir}/hicolor/22x22/actions/im-local-xmpp.png
%{_iconsdir}/hicolor/22x22/actions/im-msn.png
%{_iconsdir}/hicolor/22x22/actions/im-qq.png
%{_iconsdir}/hicolor/22x22/actions/im-skype.png
%{_iconsdir}/hicolor/22x22/actions/im-yahoo.png
%{_iconsdir}/hicolor/22x22/actions/show-offline.png
%{_iconsdir}/hicolor/22x22/actions/sort-name.png
%{_iconsdir}/hicolor/22x22/actions/sort-presence.png
%{_iconsdir}/hicolor/22x22/apps/telepathy-kde.png
%{_iconsdir}/hicolor/32x32/actions/im-aim.png
%{_iconsdir}/hicolor/32x32/actions/im-facebook.png
%{_iconsdir}/hicolor/32x32/actions/im-gadugadu.png
%{_iconsdir}/hicolor/32x32/actions/im-google-talk.png
%{_iconsdir}/hicolor/32x32/actions/im-groupwise.png
%{_iconsdir}/hicolor/32x32/actions/im-icq.png
%{_iconsdir}/hicolor/32x32/actions/im-irc.png
%{_iconsdir}/hicolor/32x32/actions/im-jabber.png
%{_iconsdir}/hicolor/32x32/actions/im-local-xmpp.png
%{_iconsdir}/hicolor/32x32/actions/im-msn.png
%{_iconsdir}/hicolor/32x32/actions/im-qq.png
%{_iconsdir}/hicolor/32x32/actions/im-skype.png
%{_iconsdir}/hicolor/32x32/actions/im-yahoo.png
%{_iconsdir}/hicolor/32x32/apps/telepathy-kde.png
%{_iconsdir}/hicolor/48x48/actions/im-aim.png
%{_iconsdir}/hicolor/48x48/actions/im-facebook.png
%{_iconsdir}/hicolor/48x48/actions/im-gadugadu.png
%{_iconsdir}/hicolor/48x48/actions/im-google-talk.png
%{_iconsdir}/hicolor/48x48/actions/im-groupwise.png
%{_iconsdir}/hicolor/48x48/actions/im-icq.png
%{_iconsdir}/hicolor/48x48/actions/im-jabber.png
%{_iconsdir}/hicolor/48x48/actions/im-local-xmpp.png
%{_iconsdir}/hicolor/48x48/actions/im-msn.png
%{_iconsdir}/hicolor/48x48/actions/im-qq.png
%{_iconsdir}/hicolor/48x48/actions/im-skype.png
%{_iconsdir}/hicolor/48x48/actions/im-yahoo.png
%{_iconsdir}/hicolor/48x48/apps/telepathy-kde.png
%{_iconsdir}/hicolor/64x64/apps/telepathy-kde.png
%{_iconsdir}/hicolor/scalable/apps/telepathy-kde.svgz
%{_datadir}/katepart5/syntax/ktpdebugoutput.xml
%{_datadir}/knotifications5/ktelepathy.notifyrc
%{_datadir}/kservicetypes5/ktp_logger_plugin.desktop
%{_datadir}/config.kcfg/ktp-proxy-config.kcfg
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.KTp.Proxy.service
%{_datadir}/telepathy/clients/KTp.Proxy.client

%files devel
%defattr(644,root,root,755)
%{_includedir}/KTp
%{_libdir}/cmake/KTp
%{_libdir}/libKTpCommonInternals.so
%{_libdir}/libKTpLogger.so
%{_libdir}/libKTpModels.so
%{_libdir}/libKTpOTR.so
%{_libdir}/libKTpWidgets.so
