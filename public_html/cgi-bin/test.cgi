#!/usr/bin/perl 

# test - a CGI script for the Twin Cities Race Walkers
#      - author: Bruce Leasure
#      - Copyright (C) 2005 by Bruce Leasure

use strict;
use CGI qw(:standard escapeHTML);

my $dir = "/home/tcrw2005/public_html";
my $script = $dir . "/cgi-bin/" . "join.cgi";
my $out = $dir . "/" . "join.txt";

my $rc = system($cmd);
print header();
print start_html('done'),h1('done'),
	"\n",p,"command = ",$cmd;

my $cmd = "/usr/bin/perl -w $script 2>&1 1>$out";

print   "\n",p,"return code = ",$rc,
        "\n",p,a({href=>"join.txt"},"join.txt"),
	"\n",end_html;
exit(0);





