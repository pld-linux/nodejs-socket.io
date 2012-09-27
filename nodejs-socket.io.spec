%define		pkg	socket.io
Summary:	Real-time apps made cross-browser & easy with a WebSocket-like API
Name:		nodejs-%{pkg}
Version:	0.9.10
Release:	0.3
License:	MIT
Group:		Development/Libraries
URL:		http://socket.io
Source0:	http://registry.npmjs.org/socket.io/-/%{pkg}-%{version}.tgz
# Source0-md5:	bdd39abd0df0d8f79151e310525b3da7
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
Requires:	nodejs
Requires:	nodejs-socket.io-client >= 0.9.10
#    "policyfile": "0.0.4",
#    "redis": "0.7.2"
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Real-time apps made cross-browser & easy with a WebSocket-like API.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -a index.js package.json lib $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.md History.md
%{nodejs_libdir}/%{pkg}
