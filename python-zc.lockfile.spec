Name:		python-zc.lockfile
Version:	1.0.0
Release:	%mkrel 2
Group:		Development/Python
License:	Zope Public License
Summary:	Basic inter-process locks
#md5=6cf83766ef9935c33e240b0904c7a45e
Source:		http://pypi.python.org/packages/source/z/zc.lockfile/zc.lockfile-1.0.0.tar.gz
URL:		http://pypi.python.org/pypi/zc.lockfile/1.0.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:	python-devel
BuildRequires:	python-setuptools

%description
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically
to lock files, but to simply provide locks with an implementation based
on file-locking primitives. Of course, these locks could be used to mediate
access to other files. For example, the ZODB file storage implementation uses
file locks to mediate access to file-storage database files. The database files
and lock file files are separate files.

%prep
%setup -q -n zc.lockfile-%{version}

%build

%install
PYTHONDONTWRITEBYTECODE= \
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
