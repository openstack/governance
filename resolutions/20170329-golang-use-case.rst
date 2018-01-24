========================================================================
 2017-03-29 Use case for the addition of Go as a supported language
========================================================================

Introduction
------------

In a previous resolution titled :doc:`20150901-programming-languages`, the TC
determined that the supported languages in OpenStack are: bash, Javascript and
Python. Furthermore, that document also recognized that it was not wise to
limit OpenStack service projects to only those three languages in the future,
but it never went as far as determining how new languages could be supported. A
new document: :doc:`Requirements for language additions to the OpenStack
Ecosystem <../reference/new-language-requirements>`, was recently introduced to
define a process in which new languages could be added as supported languages
in OpenStack; it calls for a two step process in which the first step is to
review and agree on the technical needs for a new language, and the second step
to a meet a minimum number of requirements to support the new language in the
OpenStack ecosystem.

This resolution provides the use case analysis (step 1) for the addition of Go
(aka golang) as a supported language under the OpenStack governance model based
on the requirements of the Swift object server and its data consistency engine.

Technical requirements
----------------------

In an e-mail thread last summer [1]_, Samuel Merritt provided an extensive
explanation for the challenges and limitations of previous solutions that the
Swift team has encountered regarding disk I/O performance. What follows is a
summary of what he detailed:

The Swift Object Server is responsible for handling multiple client connections
concurrently to both read and write data to disk. While Eventlet is very good at
reading/writing data to network sockets, reading/writing data to disks can be
very slow because the calling thread/process are blocked waiting for the kernel
to return.

With Eventlet, when a greenthread tries to read from a socket and the socket is
not readable, the Eventlet hub steps in, un-schedules the greenthread, finds an
un-blocked one, and lets it proceed. When a greenthread tries to read from a
file, the read() call doesn't return until the data is in the process's memory.
If the data isn't in buffer cache and the kernel has to go fetch it from a
spinning disk, it can take on average around ~7ms of seek time. Eventlet is not
able to un-schedule greenthreads that are reading from disk, so the calling
process blocks until the kernel reads the data from the disk.

For the Swift object servers that could be running on servers with 40, 60 or
even 90 disks, all these little waits drive throughput down to unacceptable
levels. To make matters worse, if one of the disks starts failing, the wait on
that one disk can go up to dozens of even hundreds of milliseconds, causing the
object server to block services to all disks.

The Swift community has tried for years to solve this problem with Python. One
attempt was to use a threadpool with a couple of I/O threads per disk, which
helped mitigate the problem with slow disks. The issue with this approach was
the threadpool overhead. It helps for systems calls that are going out to disk,
but it slowed down calls to the data that is in buffer cache, so in reality
using a threadpool brought a great cost to overall throughput, in some cases,
users saw a 25% drop in throughput.  Another solution was to separate object
server processes per disk. The solution also helped with slow disks and there's
no need for a thread pool, but for super dense servers with many dozens of disks
it meant that memory consumption spiked up, limiting the memory available for
the filesystem.

Other solutions have been talked about, but ended up being rejected. Using
Linux AIO (kernel AIO, not POSIX libaio) would let the object server have many
pending IOs cheaply, but it only works in `O_DIRECT` mode, which requires
memory buffer to be aligned, which is not possible in Python. Libuv is a new
and promising, yet unproven, solution. However, there are no Python libraries
yet that support async disk I/O calls [2]_ [3]_, plus it would still require
the Swift team to re-write the object server causing a full solution to be
years away.

Proposed solution
-----------------

The solution to this problem is being able to use non-blocking I/O calls. The
Go runtime would help mitigate the filesystem I/O because it would be able to
run blocking system calls in dedicated OS threads in a lightweight fashion,
allowing for one Go object server process to perform I/O calls to many disks
without blocking the whole process. It solves the I/O throughput problem
without causing a high spike in memory consumption.

The Rackspace cloud files team started experimenting with using Golang and from
that the Hummingbird project was born. Today, Hummingbird serves as a very good
proof of concept that we can solve all the problems that have been mentioned in
a timely manner. Yes, the Swift team will still need to re-write the Object
server, but a significant amount of that work has already been done, plus it has
been show to already work in production with excellent performance and
scalability results [4]_.

The Swift community believes the reasons stated above satisfies the first step
of the :doc:`Requirements for language additions to the OpenStack Ecosystem
<../reference/new-language-requirements>` resolution to add golang as a
supported language in the Openstack ecosystem. Furthermore, we look forward to
be able to work with the rest of the OpenStack community on the second step
once this resolution is approved.

References
==========

.. [1] http://lists.openstack.org/pipermail/openstack-dev/2016-May/094549.html

.. [2] https://github.com/MagicStack/uvloop/issues/1

.. [3] https://github.com/Tinche/aiofiles/issues/4

.. [4] https://youtu.be/Jfat_FReZIE
