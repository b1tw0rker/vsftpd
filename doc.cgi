#!/usr/bin/perl

#    vsftpd
#    version: 1.4
#    (C) 2003 - 2010 by NH (Nick Herrmann)
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.



use WebminCore;
do './vsftpd-lib.pl';
$|=1;
&init_config("vsftpd");

%access=&get_module_acl;


vsftpd_header();


print "<hr>\n";

print <<EOM;


<H1>VSFTPD.CONF</H1>
Section: File Formats (5)<BR>
<HR>

<A NAME="lbAB">&nbsp;</A>
<H2>NAME</H2>

vsftpd.conf - config file for vsftpd
<A NAME="lbAC">&nbsp;</A>

<H2>DESCRIPTION</H2>

vsftpd.conf may be used to control various aspects of vsftpd's behaviour. By
default, vsftpd looks for this file at the location
<B>/etc/vsftpd.conf</B>.

However, you may override this by specifying a command line argument to
vsftpd. The command line argument is the pathname of the configuration file
for vsftpd. This behaviour is useful because you may wish to use an advanced
inetd such as
<B>xinetd</B>

to launch vsftpd with different configuration files on a per virtual host
basis.
<P>
<A NAME="lbAD">&nbsp;</A>
<H2>FORMAT</H2>

The format of vsftpd.conf is very simple. Each line is either a comment or
a directive. Comment lines start with a # and are ignored. A directive line
has the format:
<P>

option=value
<P>
It is important to note that it is an error to put any space between the
option, = and value.
<P>
Each setting has a compiled in default which may be modified in the
configuration file.
<P>
<A NAME="lbAE">&nbsp;</A>
<H2>BOOLEAN OPTIONS</H2>

Below is a list of boolean options. The value for a boolean option may be set
to
<B>YES</B>

or
<B>NO</B>.


<P>
<DL COMPACT>
<DT><B>allow_anon_ssl</B>

<DD>
Only applies if
<B>ssl_enable</B>

is active. If set to YES, anonymous users will be allowed to use secured SSL
connections.
<P>
Default: NO
<DT><B>anon_mkdir_write_enable</B>

<DD>

If set to YES, anonymous users will be permitted to create new directories
under certain conditions. For this to work, the option
<B>write_enable</B>

must be activated, and the anonymous ftp user must have write permission on
the parent directory.
<P>
Default: NO
<DT><B>anon_other_write_enable</B>

<DD>
If set to YES, anonymous users will be permitted to perform write operations
other than upload and create directory, such as deletion and renaming. This
is generally not recommended but included for completeness.
<P>
Default: NO
<DT><B>anon_upload_enable</B>

<DD>
If set to YES, anonymous users will be permitted to upload files under certain
conditions. For this to work, the option
<B>write_enable</B>

must be activated, and the anonymous ftp user must have write permission on
desired upload locations. This setting is also required for virtual users to
upload; by default, virtual users are treated with anonymous (i.e. maximally
restricted) privilege.
<P>
Default: NO
<DT><B>anon_world_readable_only</B>

<DD>
When enabled, anonymous users will only be allowed to download files which
are world readable. This is recognising that the ftp user may own files,
especially in the presence of uploads.
<P>
Default: YES
<DT><B>anonymous_enable</B>

<DD>
Controls whether anonymous logins are permitted or not. If enabled,
both the usernames
<B>ftp</B>

and
<B>anonymous</B>

are recognised as anonymous logins.
<P>
Default: YES
<DT><B>ascii_download_enable</B>

<DD>

When enabled, ASCII mode data transfers will be honoured on downloads.
<P>
Default: NO
<DT><B>ascii_upload_enable</B>

<DD>
When enabled, ASCII mode data transfers will be honoured on uploads.
<P>
Default: NO
<DT><B>async_abor_enable</B>

<DD>
When enabled, a special FTP command known as &quot;async ABOR&quot; will be enabled.
Only ill advised FTP clients will use this feature. Additionally, this feature
is awkward to handle, so it is disabled by default. Unfortunately, some FTP
clients will hang when cancelling a transfer unless this feature is available,
so you may wish to enable it.

<P>
Default: NO
<DT><B>background</B>

<DD>
When enabled, and vsftpd is started in &quot;listen&quot; mode, vsftpd will background
the listener process. i.e. control will immediately be returned to the shell
which launched vsftpd.
<P>
Default: NO
<DT><B>check_shell</B>

<DD>
Note! This option only has an effect for non-PAM builds of vsftpd. If disabled,
vsftpd will not check /etc/shells for a valid user shell for local logins.

<P>
Default: YES
<DT><B>chmod_enable</B>

<DD>
When enabled, allows use of the SITE CHMOD command. NOTE! This only applies
to local users. Anonymous users never get to use SITE CHMOD.
<P>
Default: YES
<DT><B>chown_uploads</B>

<DD>
If enabled, all anonymously uploaded files will have the ownership changed
to the user specified in the setting
<B>chown_username</B>.

This is useful from an administrative, and perhaps security, standpoint.
<P>

Default: NO
<DT><B>chroot_list_enable</B>

<DD>
If activated, you may provide a list of local users who are placed in a
chroot() jail in their home directory upon login. The meaning is slightly
different if chroot_local_user is set to YES. In this case, the list becomes
a list of users which are NOT to be placed in a chroot() jail.
By default, the file containing this list is
/etc/vsftpd.chroot_list, but you may override this with the
<B>chroot_list_file</B>

setting.
<P>
Default: NO
<DT><B>chroot_local_user</B>

<DD>
If set to YES, local users will be (by default) placed in a chroot() jail in
their home directory after login.

<B>Warning:</B>

This option has security implications, especially if the users have upload
permission, or shell access. Only enable if you know what you are doing.
Note that these security implications are not vsftpd specific. They apply to
all FTP daemons which offer to put local users in chroot() jails.
<P>
Default: NO
<DT><B>connect_from_port_20</B>

<DD>
This controls whether PORT style data connections use port 20 (ftp-data) on
the server machine. For security reasons, some clients may insist that this
is the case. Conversely, disabling this option enables vsftpd to run with
slightly less privilege.
<P>
Default: NO (but the sample config file enables it)
<DT><B>debug_ssl</B>

<DD>

If true, OpenSSL connection diagnostics are dumped to the vsftpd log file.
(Added in v2.0.6).
<P>
Default: NO
<DT><B>delete_failed_uploads</B>

<DD>
If true, any failed upload files are deleted.  (Added in v2.0.7).
<P>
Default: NO
<DT><B>deny_email_enable</B>

<DD>
If activated, you may provide a list of anonymous password e-mail responses
which cause login to be denied. By default, the file containing this list is
/etc/vsftpd.banned_emails, but you may override this with the
<B>banned_email_file</B>

setting.
<P>
Default: NO
<DT><B>dirlist_enable</B>

<DD>
If set to NO, all directory list commands will give permission denied.
<P>
Default: YES
<DT><B>dirmessage_enable</B>

<DD>
If enabled, users of the FTP server can be shown messages when they first
enter a new directory. By default, a directory is scanned for the
file .message, but that may be overridden with the configuration setting
<B>message_file</B>.


<P>
Default: NO (but the sample config file enables it)
<DT><B>download_enable</B>

<DD>
If set to NO, all download requests will give permission denied.
<P>
Default: YES
<DT><B>dual_log_enable</B>

<DD>
If enabled, two log files are generated in parallel, going by default to
<B>/var/log/xferlog</B>

and
<B>/var/log/vsftpd.log</B>.

The former is a wu-ftpd style transfer log, parseable by standard tools. The
latter is vsftpd's own style log.
<P>
Default: NO
<DT><B>force_dot_files</B>

<DD>
If activated, files and directories starting with . will be shown in directory
listings even if the &quot;a&quot; flag was not used by the client. This override
excludes the &quot;.&quot; and &quot;..&quot; entries.

<P>
Default: NO
<DT><B>force_anon_data_ssl</B>

<DD>
Only applies if
<B>ssl_enable</B>

is activated. If activated, all anonymous logins are forced to use a secure
SSL connection in order to send and receive data on data connections.
<P>
Default: NO
<DT><B>force_anon_logins_ssl</B>

<DD>

Only applies if
<B>ssl_enable</B>

is activated. If activated, all anonymous logins are forced to use a secure
SSL connection in order to send the password.
<P>
Default: NO
<DT><B>force_local_data_ssl</B>

<DD>
Only applies if
<B>ssl_enable</B>

is activated. If activated, all non-anonymous logins are forced to use a secure
SSL connection in order to send and receive data on data connections.
<P>

Default: YES
<DT><B>force_local_logins_ssl</B>

<DD>
Only applies if
<B>ssl_enable</B>

is activated. If activated, all non-anonymous logins are forced to use a secure
SSL connection in order to send the password.
<P>
Default: YES
<DT><B>guest_enable</B>

<DD>
If enabled, all non-anonymous logins are classed as &quot;guest&quot; logins. A guest
login is remapped to the user specified in the

<B>guest_username</B>

setting.
<P>
Default: NO
<DT><B>hide_ids</B>

<DD>
If enabled, all user and group information in directory listings will be
displayed as &quot;ftp&quot;.
<P>
Default: NO
<DT><B>implicit_ssl</B>

<DD>
If enabled, an SSL handshake is the first thing expect on all connections
(the FTPS protocol). To support explicit SSL and/or plain text too, a
separate vsftpd listener process should be run.
<P>
Default: NO
<DT><B>listen</B>

<DD>
If enabled, vsftpd will run in standalone mode. This means that vsftpd must
not be run from an inetd of some kind. Instead, the vsftpd executable is
run once directly. vsftpd itself will then take care of listening for and
handling incoming connections.
<P>
Default: YES
<DT><B>listen_ipv6</B>

<DD>
Like the listen parameter, except vsftpd will listen on an IPv6 socket instead
of an IPv4 one. This parameter and the listen parameter are mutually
exclusive.

<P>
Default: NO
<DT><B>local_enable</B>

<DD>
Controls whether local logins are permitted or not. If enabled, normal
user accounts in /etc/passwd (or wherever your PAM config references) may be
used to log in. This must be enable for any non-anonymous login to work,
including virtual users.
<P>
Default: NO
<DT><B>lock_upload_files</B>

<DD>
When enabled, all uploads proceed with a write lock on the upload file. All
downloads proceed with a shared read lock on the download file. WARNING!
Before enabling this, be aware that malicious readers could starve a writer
wanting to e.g. append a file.
<P>
Default: YES
<DT><B>log_ftp_protocol</B>

<DD>
When enabled, all FTP requests and responses are logged, providing the option
xferlog_std_format is not enabled. Useful for debugging.
<P>
Default: NO
<DT><B>ls_recurse_enable</B>

<DD>
When enabled, this setting will allow the use of &quot;ls -R&quot;. This is a minor
security risk, because a ls -R at the top level of a large site may consume
a lot of resources.
<P>
Default: NO
<DT><B>mdtm_write</B>

<DD>
When enabled, this setting will allow MDTM to set file modification times
(subject to the usual access checks).
<P>
Default: YES
<DT><B>no_anon_password</B>

<DD>
When enabled, this prevents vsftpd from asking for an anonymous password -
the anonymous user will log straight in.
<P>
Default: NO
<DT><B>no_log_lock</B>

<DD>
When enabled, this prevents vsftpd from taking a file lock when writing to log
files. This option should generally not be enabled. It exists to workaround
operating system bugs such as the Solaris / Veritas filesystem combination
which has been observed to sometimes exhibit hangs trying to lock log files.
<P>

Default: NO
<DT><B>one_process_model</B>

<DD>
If you have a Linux 2.4 kernel, it is possible to use a different security
model which only uses one process per connection. It is a less pure security
model, but gains you performance. You really don't want to enable this unless
you know what you are doing, and your site supports huge numbers of
simultaneously connected users.
<P>
Default: NO
<DT><B>passwd_chroot_enable</B>

<DD>
If enabled, along with
<B>chroot_local_user</B>

, then a chroot() jail location may be specified on a per-user basis. Each
user's jail is derived from their home directory string in /etc/passwd. The
occurrence of /./ in the home directory string denotes that the jail is at that
particular location in the path.

<P>
Default: NO
<DT><B>pasv_addr_resolve</B>

<DD>
Set to YES if you want to use a hostname (as opposed to IP address) in the
<B>pasv_address</B>

option.
<P>
Default: NO
<DT><B>pasv_enable</B>

<DD>

Set to NO if you want to disallow the PASV method of obtaining a data
connection.
<P>
Default: YES
<DT><B>pasv_promiscuous</B>

<DD>
Set to YES if you want to disable the PASV security check that ensures the
data connection originates from the same IP address as the control connection.
Only enable if you know what you are doing! The only legitimate use for this
is in some form of secure tunnelling scheme, or perhaps to facilitate FXP
support.
<P>
Default: NO
<DT><B>port_enable</B>

<DD>
Set to NO if you want to disallow the PORT method of obtaining a data
connection.
<P>
Default: YES

<DT><B>port_promiscuous</B>

<DD>
Set to YES if you want to disable the PORT security check that ensures that
outgoing data connections can only connect to the client. Only enable if
you know what you are doing!
<P>
Default: NO
<DT><B>require_cert</B>

<DD>
If set to yes, all SSL client connections are required to present a client
certificate. The degree of validation applied to this certificate is
controlled by
<B>validate_cert</B>

(Added in v2.0.6).
<P>

Default: NO
<DT><B>require_ssl_reuse</B>

<DD>
If set to yes, all SSL data connections are required to exhibit SSL session
reuse (which proves that they know the same master secret as the control
channel). Although this is a secure default, it may break many FTP clients,
so you may want to disable it. For a discussion of the consequences, see
<A HREF="http://scarybeastsecurity.blogspot.com/2009/02/vsftpd-210-released.html">http://scarybeastsecurity.blogspot.com/2009/02/vsftpd-210-released.html</A>
(Added in v2.1.0).
<P>
Default: YES
<DT><B>run_as_launching_user</B>

<DD>
Set to YES if you want vsftpd to run as the user which launched vsftpd. This is
useful where root access is not available. MASSIVE WARNING! Do NOT enable this
option unless you totally know what you are doing, as naive use of this option
can create massive security problems. Specifically, vsftpd does not / cannot
use chroot technology to restrict file access when this option is set (even if
launched by root). A poor substitute could be to use a
<B>deny_file</B>

setting such as {/*,*..*}, but the reliability of this cannot compare to
chroot, and should not be relied on.
If using this option, many restrictions on other options
apply. For example, options requiring privilege such as non-anonymous logins,
upload ownership changing, connecting from port 20 and listen ports less than
1024 are not expected to work. Other options may be impacted.
<P>
Default: NO
<DT><B>secure_email_list_enable</B>

<DD>
Set to YES if you want only a specified list of e-mail passwords for anonymous
logins to be accepted. This is useful as a low-hassle way of restricting
access to low-security content without needing virtual users. When enabled,
anonymous logins are prevented unless the password provided is listed in the
file specified by the
<B>email_password_file</B>

setting. The file format is one password per line, no extra whitespace. The
default filename is /etc/vsftpd.email_passwords.
<P>
Default: NO
<DT><B>session_support</B>

<DD>
This controls whether vsftpd attempts to maintain sessions for logins. If
vsftpd is maintaining sessions, it will try and update utmp and wtmp. It
will also open a pam_session if using PAM to authenticate, and only close
this upon logout. You may wish to disable this if you do not need session
logging, and you wish to give vsftpd more opportunity to run with less
processes and / or less privilege. NOTE - utmp and wtmp support is only
provided with PAM enabled builds.
<P>
Default: NO
<DT><B>setproctitle_enable</B>

<DD>
If enabled, vsftpd will try and show session status information in the system
process listing. In other words, the reported name of the process will change
to reflect what a vsftpd session is doing (idle, downloading etc). You
probably want to leave this off for security purposes.
<P>
Default: NO
<DT><B>ssl_enable</B>

<DD>
If enabled, and vsftpd was compiled against OpenSSL, vsftpd will support secure
connections via SSL. This applies to the control connection (including login)
and also data connections. You'll need a client with SSL support too. NOTE!!
Beware enabling this option. Only enable it if you need it. vsftpd can make no
guarantees about the security of the OpenSSL libraries. By enabling this
option, you are declaring that you trust the security of your installed
OpenSSL library.

<P>
Default: NO
<DT><B>ssl_request_cert</B>

<DD>
If enabled, vsftpd will request (but not necessarily require; see
<B>require_cert)</B>a<B>certificate</B>on<B>incoming</B>SSL<B>connections.</B>Normally<B>this</B>

should not cause any trouble at all, but IBM zOS seems to have issues.
(New in v2.0.7).
<P>
Default: YES
<DT><B>ssl_sslv2</B>

<DD>
Only applies if
<B>ssl_enable</B>

is activated. If enabled, this option will permit SSL v2 protocol connections.
TLS v1 connections are preferred.
<P>
Default: NO
<DT><B>ssl_sslv3</B>

<DD>
Only applies if
<B>ssl_enable</B>

is activated. If enabled, this option will permit SSL v3 protocol connections.
TLS v1 connections are preferred.
<P>
Default: NO
<DT><B>ssl_tlsv1</B>

<DD>
Only applies if
<B>ssl_enable</B>

is activated. If enabled, this option will permit TLS v1 protocol connections.
TLS v1 connections are preferred.
<P>
Default: YES
<DT><B>strict_ssl_read_eof</B>

<DD>
If enabled, SSL data uploads are required to terminate via SSL, not an
EOF on the socket. This option is required to be sure that an attacker did
not terminate an upload prematurely with a faked TCP FIN. Unfortunately, it
is not enabled by default because so few clients get it right. (New in v2.0.7).
<P>
Default: NO
<DT><B>strict_ssl_write_shutdown</B>

<DD>
If enabled, SSL data downloads are required to terminate via SSL, not an
EOF on the socket. This is off by default as I was unable to find a single
FTP client that does this. It is minor. All it affects is our ability to tell
whether the client confirmed full receipt of the file. Even without this option,
the client is able to check the integrity of the download. (New in v2.0.7).
<P>
Default: NO

<DT><B>syslog_enable</B>

<DD>
If enabled, then any log output which would have gone to /var/log/vsftpd.log
goes to the system log instead. Logging is done under the FTPD facility.
<P>
Default: NO
<DT><B>tcp_wrappers</B>

<DD>
If enabled, and vsftpd was compiled with tcp_wrappers support, incoming
connections will be fed through tcp_wrappers access control. Furthermore,
there is a mechanism for per-IP based configuration. If tcp_wrappers sets
the VSFTPD_LOAD_CONF environment variable, then the vsftpd session will try
and load the vsftpd configuration file specified in this variable. 
<P>
Default: NO
<DT><B>text_userdb_names</B>

<DD>
By default, numeric IDs are shown in the user and group fields of directory
listings. You can get textual names by enabling this parameter. It is off
by default for performance reasons.
<P>
Default: NO
<DT><B>tilde_user_enable</B>

<DD>
If enabled, vsftpd will try and resolve pathnames such as ~chris/pics, i.e. a
tilde followed by a username. Note that vsftpd will always resolve the
pathnames ~ and ~/something (in this case the ~ resolves to the initial
login directory). Note that ~user paths will only resolve if the file
<B>/etc/passwd</B>

may be found within the _current_ chroot() jail.
<P>
Default: NO
<DT><B>use_localtime</B>

<DD>
If enabled, vsftpd will display directory listings with the time in your
local time zone. The default is to display GMT. The times returned by the
MDTM FTP command are also affected by this option.
<P>
Default: NO
<DT><B>use_sendfile</B>

<DD>
An internal setting used for testing the relative benefit of using the
sendfile() system call on your platform.
<P>
Default: YES
<DT><B>userlist_deny</B>

<DD>
This option is examined if

<B>userlist_enable</B>

is activated. If you set this setting to NO, then users will be denied login
unless they are explicitly listed in the file specified by
<B>userlist_file</B>.

When login is denied, the denial is issued before the user is asked for a
password.
<P>
Default: YES
<DT><B>userlist_enable</B>

<DD>
If enabled, vsftpd will load a list of usernames, from the filename given by
<B>userlist_file</B>.

If a user tries to log in using a name in this file, they will be denied
before they are asked for a password. This may be useful in preventing
cleartext passwords being transmitted. See also
<B>userlist_deny</B>.


<P>
Default: NO
<DT><B>validate_cert</B>

<DD>
If set to yes, all SSL client certificates received must validate OK.
Self-signed certs do not constitute OK validation. (New in v2.0.6).
<P>
Default: NO
<DT><B>virtual_use_local_privs</B>

<DD>
If enabled, virtual users will use the same privileges as local users. By
default, virtual users will use the same privileges as anonymous users, which
tends to be more restrictive (especially in terms of write access).
<P>
Default: NO
<DT><B>write_enable</B>

<DD>
This controls whether any FTP commands which change the filesystem are allowed
or not. These commands are: STOR, DELE, RNFR, RNTO, MKD, RMD, APPE and SITE.
<P>
Default: NO
<DT><B>xferlog_enable</B>

<DD>
If enabled, a log file will be maintained detailling uploads and downloads.
By default, this file will be placed at /var/log/vsftpd.log, but this location
may be overridden using the configuration setting
<B>vsftpd_log_file</B>.

<P>
Default: NO (but the sample config file enables it)
<DT><B>xferlog_std_format</B>

<DD>
If enabled, the transfer log file will be written in standard xferlog format,
as used by wu-ftpd. This is useful because you can reuse existing transfer
statistics generators. The default format is more readable, however. The
default location for this style of log file is /var/log/xferlog, but you may
change it with the setting
<B>xferlog_file</B>.

<P>
Default: NO
<P>
</DL>
<A NAME="lbAF">&nbsp;</A>
<H2>NUMERIC OPTIONS</H2>

Below is a list of numeric options. A numeric option must be set to a non
negative integer. Octal numbers are supported, for convenience of the umask
options. To specify an octal number, use 0 as the first digit of the number.
<P>
<DL COMPACT>
<DT><B>accept_timeout</B>

<DD>
The timeout, in seconds, for a remote client to establish connection with
a PASV style data connection.
<P>
Default: 60
<DT><B>anon_max_rate</B>

<DD>
The maximum data transfer rate permitted, in bytes per second, for anonymous
clients.
<P>
Default: 0 (unlimited)
<DT><B>anon_umask</B>

<DD>
The value that the umask for file creation is set to for anonymous users. NOTE! If you want to specify octal values, remember the &quot;0&quot; prefix otherwise the
value will be treated as a base 10 integer!

<P>
Default: 077
<DT><B>chown_upload_mode</B>

<DD>
The file mode to force for chown()ed anonymous uploads. (Added in v2.0.6).
<P>
Default: 0600
<DT><B>connect_timeout</B>

<DD>
The timeout, in seconds, for a remote client to respond to our PORT style
data connection.
<P>
Default: 60
<DT><B>data_connection_timeout</B>

<DD>
The timeout, in seconds, which is roughly the maximum time we permit data
transfers to stall for with no progress. If the timeout triggers, the remote
client is kicked off.
<P>
Default: 300
<DT><B>delay_failed_login</B>

<DD>
The number of seconds to pause prior to reporting a failed login.
<P>
Default: 1
<DT><B>delay_successful_login</B>

<DD>
The number of seconds to pause prior to allowing a successful login.

<P>
Default: 0
<DT><B>file_open_mode</B>

<DD>
The permissions with which uploaded files are created. Umasks are applied
on top of this value. You may wish to change to 0777 if you want uploaded
files to be executable.
<P>
Default: 0666
<DT><B>ftp_data_port</B>

<DD>
The port from which PORT style connections originate (as long as the poorly
named
<B>connect_from_port_20</B>

is enabled).
<P>
Default: 20
<DT><B>idle_session_timeout</B>

<DD>
The timeout, in seconds, which is the maximum time a remote client may spend
between FTP commands. If the timeout triggers, the remote client is kicked
off.
<P>
Default: 300
<DT><B>listen_port</B>

<DD>
If vsftpd is in standalone mode, this is the port it will listen on for
incoming FTP connections.
<P>
Default: 21

<DT><B>local_max_rate</B>

<DD>
The maximum data transfer rate permitted, in bytes per second, for local
authenticated users.
<P>
Default: 0 (unlimited)
<DT><B>local_umask</B>

<DD>
The value that the umask for file creation is set to for local users. NOTE! If
you want to specify octal values, remember the &quot;0&quot; prefix otherwise the value
will be treated as a base 10 integer!
<P>
Default: 077

<DT><B>max_clients</B>

<DD>
If vsftpd is in standalone mode, this is the maximum number of clients which
may be connected. Any additional clients connecting will get an error message.
<P>
Default: 0 (unlimited)
<DT><B>max_login_fails</B>

<DD>
After this many login failures, the session is killed.
<P>
Default: 3
<DT><B>max_per_ip</B>

<DD>
If vsftpd is in standalone mode, this is the maximum number of clients which
may be connected from the same source internet address. A client will get an
error message if they go over this limit.
<P>
Default: 0 (unlimited)
<DT><B>pasv_max_port</B>

<DD>
The maximum port to allocate for PASV style data connections. Can be used to
specify a narrow port range to assist firewalling.
<P>
Default: 0 (use any port)
<DT><B>pasv_min_port</B>

<DD>
The minimum port to allocate for PASV style data connections. Can be used to
specify a narrow port range to assist firewalling.
<P>

Default: 0 (use any port)
<DT><B>trans_chunk_size</B>

<DD>
You probably don't want to change this, but try setting it to something like
8192 for a much smoother bandwidth limiter.
<P>
Default: 0 (let vsftpd pick a sensible setting)
<P>
</DL>
<A NAME="lbAG">&nbsp;</A>
<H2>STRING OPTIONS</H2>

Below is a list of string options.
<P>
<DL COMPACT>

<DT><B>anon_root</B>

<DD>
This option represents a directory which vsftpd will try to change into
after an anonymous login. Failure is silently ignored.
<P>
Default: (none)
<DT><B>banned_email_file</B>

<DD>
This option is the name of a file containing a list of anonymous e-mail
passwords which are not permitted. This file is consulted if the option
<B>deny_email_enable</B>

is enabled.
<P>

Default: /etc/vsftpd.banned_emails
<DT><B>banner_file</B>

<DD>
This option is the name of a file containing text to display when someone
connects to the server. If set, it overrides the banner string provided by
the
<B>ftpd_banner</B>

option.
<P>
Default: (none)
<DT><B>ca_certs_file</B>

<DD>
This option is the name of a file to load Certificate Authority certs from, for
the purpose of validating client certs. Regrettably, the default SSL CA cert
paths are not used, because of vsftpd's use of restricted filesystem spaces
(chroot). (Added in v2.0.6).

<P>
Default: (none)
<DT><B>chown_username</B>

<DD>
This is the name of the user who is given ownership of anonymously uploaded
files. This option is only relevant if another option,
<B>chown_uploads</B>,

is set.
<P>
Default: root
<DT><B>chroot_list_file</B>

<DD>
The option is the name of a file containing a list of local users which
will be placed in a chroot() jail in their home directory. This option is
only relevant if the option
<B>chroot_list_enable</B>

is enabled. If the option
<B>chroot_local_user</B>

is enabled, then the list file becomes a list of users to NOT place in a
chroot() jail.
<P>
Default: /etc/vsftpd.chroot_list
<DT><B>cmds_allowed</B>

<DD>
This options specifies a comma separated list of allowed FTP commands (post
login. USER, PASS and QUIT and others are always allowed pre-login). Other
commands are rejected. This is a powerful method of really locking down an
FTP server. Example: cmds_allowed=PASV,RETR,QUIT
<P>
Default: (none)
<DT><B>cmds_denied</B>

<DD>
This options specifies a comma separated list of denied FTP commands (post
login. USER, PASS, QUIT and others are always allowed pre-login). If a command
appears on both this and
<B>cmds_allowed</B>

then the denial takes precedence. (Added in v2.1.0).
<P>
Default: (none)
<DT><B>deny_file</B>

<DD>
This option can be used to set a pattern for filenames (and directory names
etc.) which should not be accessible in any way. The affected items are not
hidden, but any attempt to do anything to them (download, change into
directory, affect something within directory etc.) will be denied. This option
is very simple, and should not be used for serious access control - the
filesystem's permissions should be used in preference. However, this option
may be useful in certain virtual user setups. In particular aware that if
a filename is accessible by a variety of names (perhaps due to symbolic
links or hard links), then care must be taken to deny access to all the names.
Access will be denied to items if their name contains the string given by
hide_file, or if they match the regular expression specified by hide_file.
Note that vsftpd's regular expression matching code is a simple implementation
which is a subset of full regular expression functionality. Because of this,
you will need to carefully and exhaustively test any application of this
option. And you are recommended to use filesystem permissions for any
important security policies due to their greater reliability. Supported
regex syntax is any number of *, ? and unnested {,} operators. Regex
matching is only supported on the last component of a path, e.g. a/b/? is
supported but a/?/c is not.
Example: deny_file={*.mp3,*.mov,.private}
<P>
Default: (none)
<DT><B>dsa_cert_file</B>

<DD>
This option specifies the location of the DSA certificate to use for SSL
encrypted connections.
<P>
Default: (none - an RSA certificate suffices)
<DT><B>dsa_private_key_file</B>

<DD>
This option specifies the location of the DSA private key to use for SSL
encrypted connections. If this option is not set, the private key is expected
to be in the same file as the certificate.
<P>
Default: (none)
<DT><B>email_password_file</B>

<DD>
This option can be used to provide an alternate file for usage by the

<B>secure_email_list_enable</B>

setting.
<P>
Default: /etc/vsftpd.email_passwords
<DT><B>ftp_username</B>

<DD>
This is the name of the user we use for handling anonymous FTP. The home
directory of this user is the root of the anonymous FTP area.
<P>
Default: ftp
<DT><B>ftpd_banner</B>

<DD>

This string option allows you to override the greeting banner displayed
by vsftpd when a connection first comes in.
<P>
Default: (none - default vsftpd banner is displayed)
<DT><B>guest_username</B>

<DD>
See the boolean setting
<B>guest_enable</B>

for a description of what constitutes a guest login. This setting is the
real username which guest users are mapped to.
<P>
Default: ftp
<DT><B>hide_file</B>

<DD>
This option can be used to set a pattern for filenames (and directory names
etc.) which should be hidden from directory listings. Despite being hidden,
the files / directories etc. are fully accessible to clients who know what
names to actually use. Items will be hidden if their names contain the string
given by hide_file, or if they match the regular expression specified by
hide_file. Note that vsftpd's regular expression matching code is a simple
implementation which is a subset of full regular expression functionality.
See
<B>deny_file</B>

for details of exactly what regex syntax is supported.
Example: hide_file={*.mp3,.hidden,hide*,h?}
<P>

Default: (none)
<DT><B>listen_address</B>

<DD>
If vsftpd is in standalone mode, the default listen address (of all local
interfaces) may be overridden by this setting. Provide a numeric IP address.
<P>
Default: (none)
<DT><B>listen_address6</B>

<DD>
Like listen_address, but specifies a default listen address for the IPv6
listener (which is used if listen_ipv6 is set). Format is standard IPv6
address format.
<P>
Default: (none)
<DT><B>local_root</B>

<DD>
This option represents a directory which vsftpd will try to change into
after a local (i.e. non-anonymous) login. Failure is silently ignored.
<P>
Default: (none)
<DT><B>message_file</B>

<DD>
This option is the name of the file we look for when a new directory is
entered. The contents are displayed to the remote user. This option is
only relevant if the option

<B>dirmessage_enable</B>

is enabled.
<P>
Default: .message
<DT><B>nopriv_user</B>

<DD>
This is the name of the user that is used by vsftpd when it wants to be
totally unprivileged. Note that this should be a dedicated user, rather
than nobody. The user nobody tends to be used for rather a lot of important
things on most machines.
<P>
Default: nobody
<DT><B>pam_service_name</B>

<DD>

This string is the name of the PAM service vsftpd will use.
<P>
Default: ftp
<DT><B>pasv_address</B>

<DD>
Use this option to override the IP address that vsftpd will advertise in
response to the PASV command. Provide a numeric IP address, unless
<B>pasv_addr_resolve</B>

is enabled, in which case you can provide a hostname which will be DNS
resolved for you at startup.
<P>
Default: (none - the address is taken from the incoming connected socket)
<DT><B>rsa_cert_file</B>

<DD>
This option specifies the location of the RSA certificate to use for SSL
encrypted connections.
<P>
Default: /usr/share/ssl/certs/vsftpd.pem
<DT><B>rsa_private_key_file</B>

<DD>
This option specifies the location of the RSA private key to use for SSL
encrypted connections. If this option is not set, the private key is expected
to be in the same file as the certificate.
<P>
Default: (none)
<DT><B>secure_chroot_dir</B>

<DD>
This option should be the name of a directory which is empty. Also, the
directory should not be writable by the ftp user. This directory is used
as a secure chroot() jail at times vsftpd does not require filesystem access.
<P>

Default: /usr/share/empty
<DT><B>ssl_ciphers</B>

<DD>
This option can be used to select which SSL ciphers vsftpd will allow for
encrypted SSL connections. See the
<B>ciphers</B>

man page for further details. Note that restricting ciphers can be a useful
security precaution as it prevents malicious remote parties forcing a cipher
which they have found problems with.
<P>
Default: DES-CBC3-SHA
<DT><B>user_config_dir</B>

<DD>
This powerful option allows the override of any config option specified in
the manual page, on a per-user basis. Usage is simple, and is best illustrated
with an example. If you set

<B>user_config_dir</B>

to be
<B>/etc/vsftpd_user_conf</B>

and then log on as the user &quot;chris&quot;, then vsftpd will apply the settings in
the file
<B>/etc/vsftpd_user_conf/chris</B>

for the duration of the session. The format of this file is as detailed in
this manual page! PLEASE NOTE that not all settings are effective on a
per-user basis. For example, many settings only prior to the user's session
being started. Examples of settings which will not affect any behviour on
a per-user basis include listen_address, banner_file, max_per_ip, max_clients,
xferlog_file, etc.
<P>
Default: (none)
<DT><B>user_sub_token</B>

<DD>
This option is useful is conjunction with virtual users. It is used to
automatically generate a home directory for each virtual user, based on a
template. For example, if the home directory of the real user specified via
<B>guest_username</B>

is
<B>/home/virtual/$USER</B>,

and
<B>user_sub_token</B>

is set to
<B>$USER</B>,

then when virtual user fred logs in, he will end up (usually chroot()'ed) in
the directory
<B>/home/virtual/fred</B>.

This option also takes affect if

<B>local_root</B>

contains
<B>user_sub_token</B>.

<P>
Default: (none)
<DT><B>userlist_file</B>

<DD>
This option is the name of the file loaded when the
<B>userlist_enable</B>

option is active.

<P>
Default: /etc/vsftpd.user_list
<DT><B>vsftpd_log_file</B>

<DD>
This option is the name of the file to which we write the vsftpd style
log file. This log is only written if the option
<B>xferlog_enable</B>

is set, and
<B>xferlog_std_format</B>

is NOT set. Alternatively, it is written if you have set the option
<B>dual_log_enable</B>.

One further complication - if you have set

<B>syslog_enable</B>,

then this file is not written and output is sent to the system log instead.
<P>
Default: /var/log/vsftpd.log
<DT><B>xferlog_file</B>

<DD>
This option is the name of the file to which we write the wu-ftpd style
transfer log. The transfer log is only written if the option
<B>xferlog_enable</B>

is set, along with
<B>xferlog_std_format</B>.

Alternatively, it is written if you have set the option
<B>dual_log_enable</B>.


<P>
Default: /var/log/xferlog
<P>
</DL>
<A NAME="lbAH">&nbsp;</A>
<H2>AUTHOR</H2>

<A HREF="mailto:scarybeasts@gmail.com">scarybeasts@gmail.com</A>
<P>
<P>

<HR>
<A NAME="index">&nbsp;</A><H2>Index</H2>
<DL>

<DT><A HREF="#lbAB">NAME</A><DD>
<DT><A HREF="#lbAC">DESCRIPTION</A><DD>
<DT><A HREF="#lbAD">FORMAT</A><DD>
<DT><A HREF="#lbAE">BOOLEAN OPTIONS</A><DD>
<DT><A HREF="#lbAF">NUMERIC OPTIONS</A><DD>
<DT><A HREF="#lbAG">STRING OPTIONS</A><DD>
<DT><A HREF="#lbAH">AUTHOR</A><DD>
</DL>
<HR>


EOM

print "<br>\n";

&footer("index.cgi", "vsftpd");
