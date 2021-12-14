#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bcc
Version  : 0.20.0
Release  : 28
URL      : https://github.com/iovisor/bcc/archive/v0.20.0/bcc-0.20.0.tar.gz
Source0  : https://github.com/iovisor/bcc/archive/v0.20.0/bcc-0.20.0.tar.gz
Source1  : https://github.com/libbpf/libbpf/archive/c5389a965bc3f19e07b1ee161092fc227e364e94/libbpf-c5389a965bc3f19e07b1ee161092fc227e364e94.tar.gz
Summary  : BPF Compiler Collection (BCC)
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause LGPL-2.1
Requires: bcc-bin = %{version}-%{release}
Requires: bcc-data = %{version}-%{release}
Requires: bcc-lib = %{version}-%{release}
Requires: bcc-license = %{version}-%{release}
Requires: bcc-python = %{version}-%{release}
Requires: bcc-python3 = %{version}-%{release}
BuildRequires : LuaJIT-dev
BuildRequires : bison-dev
BuildRequires : buildreq-cmake
BuildRequires : flex
BuildRequires : flex-dev
BuildRequires : git
BuildRequires : llvm-dev
BuildRequires : llvm-extras
BuildRequires : pkgconfig(libelf)
Patch1: 0001-Link-to-the-single-libLLVM-library.patch

%description
Python bindings for BPF Compiler Collection (BCC). Control a BPF program from
userspace.

%package bin
Summary: bin components for the bcc package.
Group: Binaries
Requires: bcc-data = %{version}-%{release}
Requires: bcc-license = %{version}-%{release}

%description bin
bin components for the bcc package.


%package data
Summary: data components for the bcc package.
Group: Data

%description data
data components for the bcc package.


%package dev
Summary: dev components for the bcc package.
Group: Development
Requires: bcc-lib = %{version}-%{release}
Requires: bcc-bin = %{version}-%{release}
Requires: bcc-data = %{version}-%{release}
Provides: bcc-devel = %{version}-%{release}
Requires: bcc = %{version}-%{release}

%description dev
dev components for the bcc package.


%package lib
Summary: lib components for the bcc package.
Group: Libraries
Requires: bcc-data = %{version}-%{release}
Requires: bcc-license = %{version}-%{release}

%description lib
lib components for the bcc package.


%package license
Summary: license components for the bcc package.
Group: Default

%description license
license components for the bcc package.


%package python
Summary: python components for the bcc package.
Group: Default
Requires: bcc-python3 = %{version}-%{release}

%description python
python components for the bcc package.


%package python3
Summary: python3 components for the bcc package.
Group: Default
Requires: python3-core

%description python3
python3 components for the bcc package.


%prep
%setup -q -n bcc-0.20.0
cd %{_builddir}
tar xf %{_sourcedir}/libbpf-c5389a965bc3f19e07b1ee161092fc227e364e94.tar.gz
cd %{_builddir}/bcc-0.20.0
mkdir -p src/cc/libbpf
cp -r %{_builddir}/libbpf-c5389a965bc3f19e07b1ee161092fc227e364e94/* %{_builddir}/bcc-0.20.0/src/cc/libbpf
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636153798
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DREVISION=%{version}
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1636153798
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bcc
cp %{_builddir}/bcc-0.20.0/LICENSE.txt %{buildroot}/usr/share/package-licenses/bcc/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/libbpf-c5389a965bc3f19e07b1ee161092fc227e364e94/LICENSE.BSD-2-Clause %{buildroot}/usr/share/package-licenses/bcc/34c5034377edef1080538bd0d4f5cf9b78e22dff
cp %{_builddir}/libbpf-c5389a965bc3f19e07b1ee161092fc227e364e94/LICENSE.LGPL-2.1 %{buildroot}/usr/share/package-licenses/bcc/91c66db733cf0ff2b3216ec4223b940daf6b26d4
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bcc-lua

%files data
%defattr(-,root,root,-)
/usr/share/bcc/examples/hello_world.py
/usr/share/bcc/examples/lua/bashreadline.c
/usr/share/bcc/examples/lua/bashreadline.lua
/usr/share/bcc/examples/lua/kprobe-latency.lua
/usr/share/bcc/examples/lua/kprobe-write.lua
/usr/share/bcc/examples/lua/memleak.lua
/usr/share/bcc/examples/lua/offcputime.lua
/usr/share/bcc/examples/lua/sock-parse-dns.lua
/usr/share/bcc/examples/lua/sock-parse-http.lua
/usr/share/bcc/examples/lua/sock-proto.lua
/usr/share/bcc/examples/lua/sock-protolen.lua
/usr/share/bcc/examples/lua/strlen_count.lua
/usr/share/bcc/examples/lua/task_switch.lua
/usr/share/bcc/examples/lua/tracepoint-offcputime.lua
/usr/share/bcc/examples/lua/uprobe-readline-perf.lua
/usr/share/bcc/examples/lua/uprobe-readline.lua
/usr/share/bcc/examples/lua/uprobe-tailkt.lua
/usr/share/bcc/examples/lua/usdt_ruby.lua
/usr/share/bcc/examples/networking/distributed_bridge/main.py
/usr/share/bcc/examples/networking/distributed_bridge/simulation.py
/usr/share/bcc/examples/networking/distributed_bridge/tunnel.c
/usr/share/bcc/examples/networking/distributed_bridge/tunnel.py
/usr/share/bcc/examples/networking/distributed_bridge/tunnel_mesh.c
/usr/share/bcc/examples/networking/distributed_bridge/tunnel_mesh.py
/usr/share/bcc/examples/networking/http_filter/README.md
/usr/share/bcc/examples/networking/http_filter/http-parse-complete.c
/usr/share/bcc/examples/networking/http_filter/http-parse-complete.py
/usr/share/bcc/examples/networking/http_filter/http-parse-simple.c
/usr/share/bcc/examples/networking/http_filter/http-parse-simple.py
/usr/share/bcc/examples/networking/neighbor_sharing/README.txt
/usr/share/bcc/examples/networking/neighbor_sharing/simulation.py
/usr/share/bcc/examples/networking/neighbor_sharing/tc_neighbor_sharing.c
/usr/share/bcc/examples/networking/neighbor_sharing/tc_neighbor_sharing.py
/usr/share/bcc/examples/networking/simple_tc.py
/usr/share/bcc/examples/networking/simulation.py
/usr/share/bcc/examples/networking/tc_perf_event.py
/usr/share/bcc/examples/networking/tunnel_monitor/README.md
/usr/share/bcc/examples/networking/tunnel_monitor/chord.png
/usr/share/bcc/examples/networking/tunnel_monitor/main.py
/usr/share/bcc/examples/networking/tunnel_monitor/monitor.c
/usr/share/bcc/examples/networking/tunnel_monitor/monitor.py
/usr/share/bcc/examples/networking/tunnel_monitor/setup.sh
/usr/share/bcc/examples/networking/tunnel_monitor/simulation.py
/usr/share/bcc/examples/networking/tunnel_monitor/traffic.sh
/usr/share/bcc/examples/networking/tunnel_monitor/vxlan.jpg
/usr/share/bcc/examples/networking/vlan_learning/README.txt
/usr/share/bcc/examples/networking/vlan_learning/simulation.py
/usr/share/bcc/examples/networking/vlan_learning/vlan_learning.c
/usr/share/bcc/examples/networking/vlan_learning/vlan_learning.py
/usr/share/bcc/examples/networking/xdp/xdp_drop_count.py
/usr/share/bcc/examples/networking/xdp/xdp_macswap_count.py
/usr/share/bcc/examples/networking/xdp/xdp_redirect_cpu.py
/usr/share/bcc/examples/networking/xdp/xdp_redirect_map.py
/usr/share/bcc/examples/tracing/CMakeLists.txt
/usr/share/bcc/examples/tracing/biolatpcts.py
/usr/share/bcc/examples/tracing/biolatpcts_example.txt
/usr/share/bcc/examples/tracing/bitehist.py
/usr/share/bcc/examples/tracing/bitehist_example.txt
/usr/share/bcc/examples/tracing/dddos.py
/usr/share/bcc/examples/tracing/dddos_example.txt
/usr/share/bcc/examples/tracing/disksnoop.py
/usr/share/bcc/examples/tracing/disksnoop_example.txt
/usr/share/bcc/examples/tracing/hello_fields.py
/usr/share/bcc/examples/tracing/hello_perf_output.py
/usr/share/bcc/examples/tracing/hello_perf_output_using_ns.py
/usr/share/bcc/examples/tracing/kvm_hypercall.py
/usr/share/bcc/examples/tracing/kvm_hypercall.txt
/usr/share/bcc/examples/tracing/mallocstacks.py
/usr/share/bcc/examples/tracing/mysqld_query.py
/usr/share/bcc/examples/tracing/mysqld_query_example.txt
/usr/share/bcc/examples/tracing/nflatency.py
/usr/share/bcc/examples/tracing/nodejs_http_server.py
/usr/share/bcc/examples/tracing/nodejs_http_server_example.txt
/usr/share/bcc/examples/tracing/stack_buildid_example.py
/usr/share/bcc/examples/tracing/stacksnoop.py
/usr/share/bcc/examples/tracing/stacksnoop_example.txt
/usr/share/bcc/examples/tracing/strlen_count.py
/usr/share/bcc/examples/tracing/strlen_hist.py
/usr/share/bcc/examples/tracing/strlen_hist_ifunc.py
/usr/share/bcc/examples/tracing/strlen_snoop.py
/usr/share/bcc/examples/tracing/sync_timing.py
/usr/share/bcc/examples/tracing/task_switch.c
/usr/share/bcc/examples/tracing/task_switch.py
/usr/share/bcc/examples/tracing/tcpv4connect.py
/usr/share/bcc/examples/tracing/tcpv4connect_example.txt
/usr/share/bcc/examples/tracing/trace_fields.py
/usr/share/bcc/examples/tracing/trace_perf_output.py
/usr/share/bcc/examples/tracing/urandomread-explicit.py
/usr/share/bcc/examples/tracing/urandomread.py
/usr/share/bcc/examples/tracing/urandomread_example.txt
/usr/share/bcc/examples/tracing/vfsreadlat.c
/usr/share/bcc/examples/tracing/vfsreadlat.py
/usr/share/bcc/examples/tracing/vfsreadlat_example.txt
/usr/share/bcc/introspection/bps
/usr/share/bcc/man/man8/argdist.8.gz
/usr/share/bcc/man/man8/bashreadline.8.gz
/usr/share/bcc/man/man8/bindsnoop.8.gz
/usr/share/bcc/man/man8/biolatency.8.gz
/usr/share/bcc/man/man8/biolatpcts.8.gz
/usr/share/bcc/man/man8/biosnoop.8.gz
/usr/share/bcc/man/man8/biotop.8.gz
/usr/share/bcc/man/man8/bitesize.8.gz
/usr/share/bcc/man/man8/bpflist.8.gz
/usr/share/bcc/man/man8/bps.8.gz
/usr/share/bcc/man/man8/btrfsdist.8.gz
/usr/share/bcc/man/man8/btrfsslower.8.gz
/usr/share/bcc/man/man8/cachestat.8.gz
/usr/share/bcc/man/man8/cachetop.8.gz
/usr/share/bcc/man/man8/capable.8.gz
/usr/share/bcc/man/man8/cobjnew.8.gz
/usr/share/bcc/man/man8/compactsnoop.8.gz
/usr/share/bcc/man/man8/cpudist.8.gz
/usr/share/bcc/man/man8/cpuunclaimed.8.gz
/usr/share/bcc/man/man8/criticalstat.8.gz
/usr/share/bcc/man/man8/cthreads.8.gz
/usr/share/bcc/man/man8/dbslower.8.gz
/usr/share/bcc/man/man8/dbstat.8.gz
/usr/share/bcc/man/man8/dcsnoop.8.gz
/usr/share/bcc/man/man8/dcstat.8.gz
/usr/share/bcc/man/man8/deadlock.8.gz
/usr/share/bcc/man/man8/dirtop.8.gz
/usr/share/bcc/man/man8/drsnoop.8.gz
/usr/share/bcc/man/man8/execsnoop.8.gz
/usr/share/bcc/man/man8/exitsnoop.8.gz
/usr/share/bcc/man/man8/ext4dist.8.gz
/usr/share/bcc/man/man8/ext4slower.8.gz
/usr/share/bcc/man/man8/filelife.8.gz
/usr/share/bcc/man/man8/fileslower.8.gz
/usr/share/bcc/man/man8/filetop.8.gz
/usr/share/bcc/man/man8/funccount.8.gz
/usr/share/bcc/man/man8/funcinterval.8.gz
/usr/share/bcc/man/man8/funclatency.8.gz
/usr/share/bcc/man/man8/funcslower.8.gz
/usr/share/bcc/man/man8/gethostlatency.8.gz
/usr/share/bcc/man/man8/hardirqs.8.gz
/usr/share/bcc/man/man8/inject.8.gz
/usr/share/bcc/man/man8/javacalls.8.gz
/usr/share/bcc/man/man8/javaflow.8.gz
/usr/share/bcc/man/man8/javagc.8.gz
/usr/share/bcc/man/man8/javaobjnew.8.gz
/usr/share/bcc/man/man8/javastat.8.gz
/usr/share/bcc/man/man8/javathreads.8.gz
/usr/share/bcc/man/man8/killsnoop.8.gz
/usr/share/bcc/man/man8/klockstat.8.gz
/usr/share/bcc/man/man8/llcstat.8.gz
/usr/share/bcc/man/man8/mdflush.8.gz
/usr/share/bcc/man/man8/memleak.8.gz
/usr/share/bcc/man/man8/mountsnoop.8.gz
/usr/share/bcc/man/man8/mysqld_qslower.8.gz
/usr/share/bcc/man/man8/netqtop.8.gz
/usr/share/bcc/man/man8/nfsdist.8.gz
/usr/share/bcc/man/man8/nfsslower.8.gz
/usr/share/bcc/man/man8/nodegc.8.gz
/usr/share/bcc/man/man8/nodestat.8.gz
/usr/share/bcc/man/man8/offcputime.8.gz
/usr/share/bcc/man/man8/offwaketime.8.gz
/usr/share/bcc/man/man8/oomkill.8.gz
/usr/share/bcc/man/man8/opensnoop.8.gz
/usr/share/bcc/man/man8/perlcalls.8.gz
/usr/share/bcc/man/man8/perlflow.8.gz
/usr/share/bcc/man/man8/perlstat.8.gz
/usr/share/bcc/man/man8/phpcalls.8.gz
/usr/share/bcc/man/man8/phpflow.8.gz
/usr/share/bcc/man/man8/phpstat.8.gz
/usr/share/bcc/man/man8/pidpersec.8.gz
/usr/share/bcc/man/man8/profile.8.gz
/usr/share/bcc/man/man8/pythoncalls.8.gz
/usr/share/bcc/man/man8/pythonflow.8.gz
/usr/share/bcc/man/man8/pythongc.8.gz
/usr/share/bcc/man/man8/pythonstat.8.gz
/usr/share/bcc/man/man8/readahead.8.gz
/usr/share/bcc/man/man8/reset-trace.8.gz
/usr/share/bcc/man/man8/rubycalls.8.gz
/usr/share/bcc/man/man8/rubyflow.8.gz
/usr/share/bcc/man/man8/rubygc.8.gz
/usr/share/bcc/man/man8/rubyobjnew.8.gz
/usr/share/bcc/man/man8/rubystat.8.gz
/usr/share/bcc/man/man8/runqlat.8.gz
/usr/share/bcc/man/man8/runqlen.8.gz
/usr/share/bcc/man/man8/runqslower.8.gz
/usr/share/bcc/man/man8/shmsnoop.8.gz
/usr/share/bcc/man/man8/slabratetop.8.gz
/usr/share/bcc/man/man8/sofdsnoop.8.gz
/usr/share/bcc/man/man8/softirqs.8.gz
/usr/share/bcc/man/man8/solisten.8.gz
/usr/share/bcc/man/man8/spfdsnoop.8.gz
/usr/share/bcc/man/man8/sslsniff.8.gz
/usr/share/bcc/man/man8/stackcount.8.gz
/usr/share/bcc/man/man8/statsnoop.8.gz
/usr/share/bcc/man/man8/swapin.8.gz
/usr/share/bcc/man/man8/syncsnoop.8.gz
/usr/share/bcc/man/man8/syscount.8.gz
/usr/share/bcc/man/man8/tclcalls.8.gz
/usr/share/bcc/man/man8/tclflow.8.gz
/usr/share/bcc/man/man8/tclobjnew.8.gz
/usr/share/bcc/man/man8/tclstat.8.gz
/usr/share/bcc/man/man8/tcpaccept.8.gz
/usr/share/bcc/man/man8/tcpconnect.8.gz
/usr/share/bcc/man/man8/tcpconnlat.8.gz
/usr/share/bcc/man/man8/tcpdrop.8.gz
/usr/share/bcc/man/man8/tcplife.8.gz
/usr/share/bcc/man/man8/tcpretrans.8.gz
/usr/share/bcc/man/man8/tcprtt.8.gz
/usr/share/bcc/man/man8/tcpstates.8.gz
/usr/share/bcc/man/man8/tcpsubnet.8.gz
/usr/share/bcc/man/man8/tcpsynbl.8.gz
/usr/share/bcc/man/man8/tcptop.8.gz
/usr/share/bcc/man/man8/tcptracer.8.gz
/usr/share/bcc/man/man8/threadsnoop.8.gz
/usr/share/bcc/man/man8/tplist.8.gz
/usr/share/bcc/man/man8/trace.8.gz
/usr/share/bcc/man/man8/ttysnoop.8.gz
/usr/share/bcc/man/man8/ucalls.8.gz
/usr/share/bcc/man/man8/uflow.8.gz
/usr/share/bcc/man/man8/ugc.8.gz
/usr/share/bcc/man/man8/uobjnew.8.gz
/usr/share/bcc/man/man8/ustat.8.gz
/usr/share/bcc/man/man8/uthreads.8.gz
/usr/share/bcc/man/man8/vfscount.8.gz
/usr/share/bcc/man/man8/vfsstat.8.gz
/usr/share/bcc/man/man8/virtiostat.8.gz
/usr/share/bcc/man/man8/wakeuptime.8.gz
/usr/share/bcc/man/man8/xfsdist.8.gz
/usr/share/bcc/man/man8/xfsslower.8.gz
/usr/share/bcc/man/man8/zfsdist.8.gz
/usr/share/bcc/man/man8/zfsslower.8.gz
/usr/share/bcc/tools/argdist
/usr/share/bcc/tools/bashreadline
/usr/share/bcc/tools/bindsnoop
/usr/share/bcc/tools/biolatency
/usr/share/bcc/tools/biolatpcts
/usr/share/bcc/tools/biosnoop
/usr/share/bcc/tools/biotop
/usr/share/bcc/tools/bitesize
/usr/share/bcc/tools/bpflist
/usr/share/bcc/tools/btrfsdist
/usr/share/bcc/tools/btrfsslower
/usr/share/bcc/tools/cachestat
/usr/share/bcc/tools/cachetop
/usr/share/bcc/tools/capable
/usr/share/bcc/tools/cobjnew
/usr/share/bcc/tools/compactsnoop
/usr/share/bcc/tools/cpudist
/usr/share/bcc/tools/cpuunclaimed
/usr/share/bcc/tools/criticalstat
/usr/share/bcc/tools/dbslower
/usr/share/bcc/tools/dbstat
/usr/share/bcc/tools/dcsnoop
/usr/share/bcc/tools/dcstat
/usr/share/bcc/tools/deadlock
/usr/share/bcc/tools/deadlock.c
/usr/share/bcc/tools/dirtop
/usr/share/bcc/tools/doc/argdist_example.txt
/usr/share/bcc/tools/doc/bashreadline_example.txt
/usr/share/bcc/tools/doc/bindsnoop_example.txt
/usr/share/bcc/tools/doc/biolatency_example.txt
/usr/share/bcc/tools/doc/biolatpcts_example.txt
/usr/share/bcc/tools/doc/biosnoop_example.txt
/usr/share/bcc/tools/doc/biotop_example.txt
/usr/share/bcc/tools/doc/bitesize_example.txt
/usr/share/bcc/tools/doc/bpflist_example.txt
/usr/share/bcc/tools/doc/btrfsdist_example.txt
/usr/share/bcc/tools/doc/btrfsslower_example.txt
/usr/share/bcc/tools/doc/cachestat_example.txt
/usr/share/bcc/tools/doc/cachetop_example.txt
/usr/share/bcc/tools/doc/capable_example.txt
/usr/share/bcc/tools/doc/cobjnew_example.txt
/usr/share/bcc/tools/doc/compactsnoop_example.txt
/usr/share/bcc/tools/doc/cpudist_example.txt
/usr/share/bcc/tools/doc/cpuunclaimed_example.txt
/usr/share/bcc/tools/doc/criticalstat_example.txt
/usr/share/bcc/tools/doc/cthreads_example.txt
/usr/share/bcc/tools/doc/dbslower_example.txt
/usr/share/bcc/tools/doc/dbstat_example.txt
/usr/share/bcc/tools/doc/dcsnoop_example.txt
/usr/share/bcc/tools/doc/dcstat_example.txt
/usr/share/bcc/tools/doc/deadlock_example.txt
/usr/share/bcc/tools/doc/dirtop_example.txt
/usr/share/bcc/tools/doc/drsnoop_example.txt
/usr/share/bcc/tools/doc/execsnoop_example.txt
/usr/share/bcc/tools/doc/exitsnoop_example.txt
/usr/share/bcc/tools/doc/ext4dist_example.txt
/usr/share/bcc/tools/doc/ext4slower_example.txt
/usr/share/bcc/tools/doc/filelife_example.txt
/usr/share/bcc/tools/doc/fileslower_example.txt
/usr/share/bcc/tools/doc/filetop_example.txt
/usr/share/bcc/tools/doc/funccount_example.txt
/usr/share/bcc/tools/doc/funcinterval_example.txt
/usr/share/bcc/tools/doc/funclatency_example.txt
/usr/share/bcc/tools/doc/funcslower_example.txt
/usr/share/bcc/tools/doc/gethostlatency_example.txt
/usr/share/bcc/tools/doc/hardirqs_example.txt
/usr/share/bcc/tools/doc/inject_example.txt
/usr/share/bcc/tools/doc/javacalls_example.txt
/usr/share/bcc/tools/doc/javaflow_example.txt
/usr/share/bcc/tools/doc/javagc_example.txt
/usr/share/bcc/tools/doc/javaobjnew_example.txt
/usr/share/bcc/tools/doc/javastat_example.txt
/usr/share/bcc/tools/doc/javathreads_example.txt
/usr/share/bcc/tools/doc/killsnoop_example.txt
/usr/share/bcc/tools/doc/klockstat_example.txt
/usr/share/bcc/tools/doc/lib/ucalls_example.txt
/usr/share/bcc/tools/doc/lib/uflow_example.txt
/usr/share/bcc/tools/doc/lib/ugc_example.txt
/usr/share/bcc/tools/doc/lib/uobjnew_example.txt
/usr/share/bcc/tools/doc/lib/ustat_example.txt
/usr/share/bcc/tools/doc/lib/uthreads_example.txt
/usr/share/bcc/tools/doc/llcstat_example.txt
/usr/share/bcc/tools/doc/mdflush_example.txt
/usr/share/bcc/tools/doc/memleak_example.txt
/usr/share/bcc/tools/doc/mountsnoop_example.txt
/usr/share/bcc/tools/doc/mysqld_qslower_example.txt
/usr/share/bcc/tools/doc/netqtop_example.txt
/usr/share/bcc/tools/doc/nfsdist_example.txt
/usr/share/bcc/tools/doc/nfsslower_example.txt
/usr/share/bcc/tools/doc/nodegc_example.txt
/usr/share/bcc/tools/doc/nodestat_example.txt
/usr/share/bcc/tools/doc/offcputime_example.txt
/usr/share/bcc/tools/doc/offwaketime_example.txt
/usr/share/bcc/tools/doc/oomkill_example.txt
/usr/share/bcc/tools/doc/opensnoop_example.txt
/usr/share/bcc/tools/doc/perlcalls_example.txt
/usr/share/bcc/tools/doc/perlflow_example.txt
/usr/share/bcc/tools/doc/perlstat_example.txt
/usr/share/bcc/tools/doc/phpcalls_example.txt
/usr/share/bcc/tools/doc/phpflow_example.txt
/usr/share/bcc/tools/doc/phpstat_example.txt
/usr/share/bcc/tools/doc/pidpersec_example.txt
/usr/share/bcc/tools/doc/profile_example.txt
/usr/share/bcc/tools/doc/pythoncalls_example.txt
/usr/share/bcc/tools/doc/pythonflow_example.txt
/usr/share/bcc/tools/doc/pythongc_example.txt
/usr/share/bcc/tools/doc/pythonstat_example.txt
/usr/share/bcc/tools/doc/readahead_example.txt
/usr/share/bcc/tools/doc/reset-trace_example.txt
/usr/share/bcc/tools/doc/rubycalls_example.txt
/usr/share/bcc/tools/doc/rubyflow_example.txt
/usr/share/bcc/tools/doc/rubygc_example.txt
/usr/share/bcc/tools/doc/rubyobjnew_example.txt
/usr/share/bcc/tools/doc/rubystat_example.txt
/usr/share/bcc/tools/doc/runqlat_example.txt
/usr/share/bcc/tools/doc/runqlen_example.txt
/usr/share/bcc/tools/doc/runqslower_example.txt
/usr/share/bcc/tools/doc/shmsnoop_example.txt
/usr/share/bcc/tools/doc/slabratetop_example.txt
/usr/share/bcc/tools/doc/sofdsnoop_example.txt
/usr/share/bcc/tools/doc/softirqs_example.txt
/usr/share/bcc/tools/doc/solisten_example.txt
/usr/share/bcc/tools/doc/sslsniff_example.txt
/usr/share/bcc/tools/doc/stackcount_example.txt
/usr/share/bcc/tools/doc/statsnoop_example.txt
/usr/share/bcc/tools/doc/swapin_example.txt
/usr/share/bcc/tools/doc/syncsnoop_example.txt
/usr/share/bcc/tools/doc/syscount_example.txt
/usr/share/bcc/tools/doc/tclcalls_example.txt
/usr/share/bcc/tools/doc/tclflow_example.txt
/usr/share/bcc/tools/doc/tclobjnew_example.txt
/usr/share/bcc/tools/doc/tclstat_example.txt
/usr/share/bcc/tools/doc/tcpaccept_example.txt
/usr/share/bcc/tools/doc/tcpconnect_example.txt
/usr/share/bcc/tools/doc/tcpconnlat_example.txt
/usr/share/bcc/tools/doc/tcpdrop_example.txt
/usr/share/bcc/tools/doc/tcplife_example.txt
/usr/share/bcc/tools/doc/tcpretrans_example.txt
/usr/share/bcc/tools/doc/tcprtt_example.txt
/usr/share/bcc/tools/doc/tcpstates_example.txt
/usr/share/bcc/tools/doc/tcpsubnet_example.txt
/usr/share/bcc/tools/doc/tcpsynbl_example.txt
/usr/share/bcc/tools/doc/tcptop_example.txt
/usr/share/bcc/tools/doc/tcptracer_example.txt
/usr/share/bcc/tools/doc/threadsnoop_example.txt
/usr/share/bcc/tools/doc/tplist_example.txt
/usr/share/bcc/tools/doc/trace_example.txt
/usr/share/bcc/tools/doc/ttysnoop_example.txt
/usr/share/bcc/tools/doc/vfscount_example.txt
/usr/share/bcc/tools/doc/vfsstat_example.txt
/usr/share/bcc/tools/doc/virtiostat_example.txt
/usr/share/bcc/tools/doc/wakeuptime_example.txt
/usr/share/bcc/tools/doc/xfsdist_example.txt
/usr/share/bcc/tools/doc/xfsslower_example.txt
/usr/share/bcc/tools/doc/zfsdist_example.txt
/usr/share/bcc/tools/doc/zfsslower_example.txt
/usr/share/bcc/tools/drsnoop
/usr/share/bcc/tools/execsnoop
/usr/share/bcc/tools/exitsnoop
/usr/share/bcc/tools/ext4dist
/usr/share/bcc/tools/ext4slower
/usr/share/bcc/tools/filelife
/usr/share/bcc/tools/fileslower
/usr/share/bcc/tools/filetop
/usr/share/bcc/tools/funccount
/usr/share/bcc/tools/funcinterval
/usr/share/bcc/tools/funclatency
/usr/share/bcc/tools/funcslower
/usr/share/bcc/tools/gethostlatency
/usr/share/bcc/tools/hardirqs
/usr/share/bcc/tools/inject
/usr/share/bcc/tools/javacalls
/usr/share/bcc/tools/javaflow
/usr/share/bcc/tools/javagc
/usr/share/bcc/tools/javaobjnew
/usr/share/bcc/tools/javastat
/usr/share/bcc/tools/javathreads
/usr/share/bcc/tools/killsnoop
/usr/share/bcc/tools/klockstat
/usr/share/bcc/tools/lib/ucalls
/usr/share/bcc/tools/lib/uflow
/usr/share/bcc/tools/lib/ugc
/usr/share/bcc/tools/lib/uobjnew
/usr/share/bcc/tools/lib/ustat
/usr/share/bcc/tools/lib/uthreads
/usr/share/bcc/tools/llcstat
/usr/share/bcc/tools/mdflush
/usr/share/bcc/tools/memleak
/usr/share/bcc/tools/mountsnoop
/usr/share/bcc/tools/mysqld_qslower
/usr/share/bcc/tools/netqtop
/usr/share/bcc/tools/netqtop.c
/usr/share/bcc/tools/nfsdist
/usr/share/bcc/tools/nfsslower
/usr/share/bcc/tools/nodegc
/usr/share/bcc/tools/nodestat
/usr/share/bcc/tools/offcputime
/usr/share/bcc/tools/offwaketime
/usr/share/bcc/tools/old/bashreadline
/usr/share/bcc/tools/old/biosnoop
/usr/share/bcc/tools/old/compactsnoop
/usr/share/bcc/tools/old/filelife
/usr/share/bcc/tools/old/gethostlatency
/usr/share/bcc/tools/old/killsnoop
/usr/share/bcc/tools/old/memleak
/usr/share/bcc/tools/old/offcputime
/usr/share/bcc/tools/old/offwaketime
/usr/share/bcc/tools/old/oomkill
/usr/share/bcc/tools/old/opensnoop
/usr/share/bcc/tools/old/profile
/usr/share/bcc/tools/old/softirqs
/usr/share/bcc/tools/old/stackcount
/usr/share/bcc/tools/old/stacksnoop
/usr/share/bcc/tools/old/statsnoop
/usr/share/bcc/tools/old/syncsnoop
/usr/share/bcc/tools/old/tcpaccept
/usr/share/bcc/tools/old/tcpconnect
/usr/share/bcc/tools/old/wakeuptime
/usr/share/bcc/tools/oomkill
/usr/share/bcc/tools/opensnoop
/usr/share/bcc/tools/perlcalls
/usr/share/bcc/tools/perlflow
/usr/share/bcc/tools/perlstat
/usr/share/bcc/tools/phpcalls
/usr/share/bcc/tools/phpflow
/usr/share/bcc/tools/phpstat
/usr/share/bcc/tools/pidpersec
/usr/share/bcc/tools/profile
/usr/share/bcc/tools/pythoncalls
/usr/share/bcc/tools/pythonflow
/usr/share/bcc/tools/pythongc
/usr/share/bcc/tools/pythonstat
/usr/share/bcc/tools/readahead
/usr/share/bcc/tools/reset-trace
/usr/share/bcc/tools/rubycalls
/usr/share/bcc/tools/rubyflow
/usr/share/bcc/tools/rubygc
/usr/share/bcc/tools/rubyobjnew
/usr/share/bcc/tools/rubystat
/usr/share/bcc/tools/runqlat
/usr/share/bcc/tools/runqlen
/usr/share/bcc/tools/runqslower
/usr/share/bcc/tools/shmsnoop
/usr/share/bcc/tools/slabratetop
/usr/share/bcc/tools/sofdsnoop
/usr/share/bcc/tools/softirqs
/usr/share/bcc/tools/solisten
/usr/share/bcc/tools/sslsniff
/usr/share/bcc/tools/stackcount
/usr/share/bcc/tools/statsnoop
/usr/share/bcc/tools/swapin
/usr/share/bcc/tools/syncsnoop
/usr/share/bcc/tools/syscount
/usr/share/bcc/tools/tclcalls
/usr/share/bcc/tools/tclflow
/usr/share/bcc/tools/tclobjnew
/usr/share/bcc/tools/tclstat
/usr/share/bcc/tools/tcpaccept
/usr/share/bcc/tools/tcpconnect
/usr/share/bcc/tools/tcpconnlat
/usr/share/bcc/tools/tcpdrop
/usr/share/bcc/tools/tcplife
/usr/share/bcc/tools/tcpretrans
/usr/share/bcc/tools/tcprtt
/usr/share/bcc/tools/tcpstates
/usr/share/bcc/tools/tcpsubnet
/usr/share/bcc/tools/tcpsynbl
/usr/share/bcc/tools/tcptop
/usr/share/bcc/tools/tcptracer
/usr/share/bcc/tools/threadsnoop
/usr/share/bcc/tools/tplist
/usr/share/bcc/tools/trace
/usr/share/bcc/tools/ttysnoop
/usr/share/bcc/tools/vfscount
/usr/share/bcc/tools/vfsstat
/usr/share/bcc/tools/virtiostat
/usr/share/bcc/tools/wakeuptime
/usr/share/bcc/tools/xfsdist
/usr/share/bcc/tools/xfsslower
/usr/share/bcc/tools/zfsdist
/usr/share/bcc/tools/zfsslower

%files dev
%defattr(-,root,root,-)
/usr/include/bcc/BPF.h
/usr/include/bcc/BPFTable.h
/usr/include/bcc/bcc_common.h
/usr/include/bcc/bcc_elf.h
/usr/include/bcc/bcc_exception.h
/usr/include/bcc/bcc_proc.h
/usr/include/bcc/bcc_syms.h
/usr/include/bcc/bcc_usdt.h
/usr/include/bcc/bcc_version.h
/usr/include/bcc/bpf_module.h
/usr/include/bcc/compat/linux/bpf.h
/usr/include/bcc/compat/linux/bpf_common.h
/usr/include/bcc/compat/linux/btf.h
/usr/include/bcc/compat/linux/if_link.h
/usr/include/bcc/compat/linux/if_xdp.h
/usr/include/bcc/compat/linux/netlink.h
/usr/include/bcc/file_desc.h
/usr/include/bcc/libbpf.h
/usr/include/bcc/perf_reader.h
/usr/include/bcc/table_desc.h
/usr/include/bcc/table_storage.h
/usr/lib64/libbcc.so
/usr/lib64/libbcc_bpf.so
/usr/lib64/pkgconfig/libbcc.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbcc.so.0
/usr/lib64/libbcc.so.0.20.0
/usr/lib64/libbcc_bpf.so.0
/usr/lib64/libbcc_bpf.so.0.20.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bcc/34c5034377edef1080538bd0d4f5cf9b78e22dff
/usr/share/package-licenses/bcc/91c66db733cf0ff2b3216ec4223b940daf6b26d4
/usr/share/package-licenses/bcc/92170cdc034b2ff819323ff670d3b7266c8bffcd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
