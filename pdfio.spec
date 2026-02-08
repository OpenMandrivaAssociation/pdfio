%define major 1
%define libname %mklibname pdfio
%define devname %mklibname pdfio -d

Name:		pdfio
Version:	1.6.1
Release:	1
Source0:	https://github.com/michaelrsweet/pdfio/releases/download/v%{version}/pdfio-%{version}.tar.gz
Summary:	Simple C library for reading and writing PDF files
URL:		https://github.com/michaelrsweet/pdfio
License:	Apache-2.0
Group:		System/Libraries
BuildRequires:	autoconf automake slibtool make
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng)

%description
PDFio is a simple C library for reading and writing PDF files. The primary
goals of PDFio are:

Read and write any version of PDF file
Provide access to pages, objects, and streams within a PDF file
Support reading and writing of encrypted PDF files
Extract or embed useful metadata (author, creator, page information, etc.)
"Filter" PDF files, for example to extract a range of pages or to embed fonts
that are missing from a PDF
Provide access to objects used for each page
PDFio is not concerned with rendering or viewing a PDF file, although a PDF
RIP or viewer could be written using it.

%package -n %{libname}
Summary:	Simple C library for reading and writing PDF files
Group:		System/Libraries

%description -n %{libname}
PDFio is a simple C library for reading and writing PDF files. The primary
goals of PDFio are:

Read and write any version of PDF file
Provide access to pages, objects, and streams within a PDF file
Support reading and writing of encrypted PDF files
Extract or embed useful metadata (author, creator, page information, etc.)
"Filter" PDF files, for example to extract a range of pages or to embed fonts
that are missing from a PDF
Provide access to objects used for each page
PDFio is not concerned with rendering or viewing a PDF file, although a PDF
RIP or viewer could be written using it.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

PDFio is a simple C library for reading and writing PDF files. The primary
goals of PDFio are:

Read and write any version of PDF file
Provide access to pages, objects, and streams within a PDF file
Support reading and writing of encrypted PDF files
Extract or embed useful metadata (author, creator, page information, etc.)
"Filter" PDF files, for example to extract a range of pages or to embed fonts
that are missing from a PDF
Provide access to objects used for each page
PDFio is not concerned with rendering or viewing a PDF file, although a PDF
RIP or viewer could be written using it.

%prep
%autosetup -p1
slibtoolize --force

%conf
%configure \
	--enable-shared

%build
%make_build LIBTOOL=rclibtool

%install
# Yes, no DESTDIR -- pdfio Makefiles see "$RPM_BUILD_ROOT"
# and act on it. specifying both results in
# a /%{buildroot}/%{buildroot} directory structure.
make install

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%doc %{_docdir}/pdfio
%{_mandir}/man3/pdfio.3*
