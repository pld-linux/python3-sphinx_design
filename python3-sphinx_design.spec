%define 	module	sphinx_design
Summary:	A sphinx extension for designing beautiful web components
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do projektowania ładnych komponentów WWW
Name:		python3-%{module}
Version:	0.6.1
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx_design/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_design/%{module}-%{version}.tar.gz
# Source0-md5:	a9de747353ce75271639efb2fad2ac5c
URL:		https://github.com/executablebooks/sphinx-design
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.4
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.9
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A sphinx extension for designing beautiful, view size responsive web
components.

%description -l pl.UTF-8
Rozszerzenie Sphinksa do projektowania ładnych, reagujących na rozmiar
widoku komponentów WWW.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
