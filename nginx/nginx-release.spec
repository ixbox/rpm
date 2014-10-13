Name:           nginx-release
Version:        6
Release:        1
Summary:        Nginx Packages

Group:          Web Server
License:        MIT License

URL:            http://nginx.org/packages/centos/
Source0:        http://nginx.org/keys/nginx_signing.key
Source1:        nginx.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Requires:       redhat-release >=  %{version}

%description
nginx [engine x] is an HTTP and reverse proxy server

%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build

%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/nginx_signing.key

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1}  \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*

%changelog
