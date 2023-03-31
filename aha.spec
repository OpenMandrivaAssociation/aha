Summary: Convert terminal output to HTML
Name: aha
License: MPLv1.1 or LGPLv2+
Version: 0.5.1
Release: 2
Group: Text tools
URL: https://github.com/theZiz/aha
Source0: %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

# Fix a null pointer dereference when interpreting
# invalid 24-bit color code escape sequences.
#
# Submitted upstream: https://github.com/theZiz/aha/pull/97
Patch0: 0000-fix-null-pointer-dereference.patch

%description
%{name} parses output from other programs,
recognizes ANSI terminal escape sequences
and produces an HTML rendition of the original text.

%prep
%autosetup -p1
# Extract license header from source code
cat aha.c | awk '1;/\*\//{exit}' > LICENSE

%build
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%{_bindir}/%{name}
%doc %{_mandir}/man1/%{name}.*
