%global underscore() %(echo %1 | sed 's/-/_/g')

%global python3_pkgversion_311 3.11

%global sum A simple python library for interacting with the ARGO Accounting Service
%global desc A simple python library for interacting with the ARGO Accounting Service


Name:           argo-acc-library
Summary:        %{sum}
Version:        0.1.0
Release:        1%{?dist}

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/ARGOeu/argo-acc-library
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch


%description
%{desc}


%package -n python%{python3_pkgversion}-%{name}
Summary: %{sum}
BuildRequires: python3-devel    python3-setuptools
Requires:      python3-requests
AutoReq: no
%description -n python%{python3_pkgversion}-%{name}
%{desc}
%{?python_provide:%python_provide python3-%{name}}

%package -n python%{python3_pkgversion_311}-%{name}
Summary: %{sum}
BuildRequires: python3.11-devel    python3.11-setuptools
Requires:      python3.11-requests
AutoReq: no
%description -n python%{python3_pkgversion_311}-%{name}
%{desc}
%{?python_provide:%python_provide python%{python3_pkgversion_311}-%{name}}

%prep
%setup -q

%build
%{py3_build}
python3.11 setup.py build

%install
rm -rf %{buildroot}
%{py3_install "--record=INSTALLED_FILES_PY3" }
python3.11 setup.py install --root=%{buildroot} --record=INSTALLED_FILES_PY3_311

%files -n python%{python3_pkgversion}-%{name} -f INSTALLED_FILES_PY3
%doc examples/ README.md
%defattr(-,root,root,-)
%{python3_sitelib}/*
%doc examples/ README.md

%files -n python%{python3_pkgversion_311}-%{name} -f INSTALLED_FILES_PY3_311
%doc examples/ README.md
%defattr(-,root,root,-)
/usr/lib/python3.11/site-packages/*
%doc examples/ README.md


%changelog
* Thu Mar 27 2025 William V. Karageorgos <wvkarageorgos@admin.grnet.gr> - 0.1.0-1%{?dist}
- Initial version
