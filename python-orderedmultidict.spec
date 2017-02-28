%global         commit0 aaa4bc1144bb81c1d7d5cd6952b2e750927b8c59
%global         shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global         checkout 02812017git%{shortcommit0}
%global         sum Ordered Multivalue Dictionary
%global         uname orderedmultidict

Name:           python-orderedmultidict
Version:        0.1
Release:        1%{checkout}%{?dist}
Summary:        %{sum}

License:        MIT
URL:            https://github.com/gruns/%{uname}
Source0:        https://github.com/gruns/%{uname}/archive/%{commit0}.tar.gz

BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-nose
BuildRequires:  python-six

%description
Ordered Multivalue Dictionary

%package -n python2-orderedmultidict

Summary:        %sum
Requires:       python-six

%description -n python2-orderedmultidict
Ordered Multivalue Dictionary

%prep
%autosetup -n %{uname}-%{commit0}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
nosetests -v

%files -n python2-orderedmultidict
%{python2_sitelib}/*

%changelog
* Mon Feb 27 2017 Fabien Boucher <fboucher@redhat.com> - 0.1-102282017gitaaa4bc11
- Initial packaging
