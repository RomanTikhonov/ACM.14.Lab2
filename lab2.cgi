#!c:/perl64/bin/perl

use strict;
use CGI;
use CGI::Carp qw(fatalsToBrowser);

use lab2::st01::st01;
use lab2::st05::st05;
use lab2::st08::st08;
use lab2::st12::st12;
use lab2::st15::st15;
use lab2::st17::st17;
use lab2::st21::st21;
use lab2::st22::st22;

my @MODULES = 
(
	\&ST01::st01,
	\&ST05::st05,
	\&ST08::st08,
	\&ST12::st12,
	\&ST15::st15,
	\&ST17::st17,
	\&ST21::st21,
	\&ST22::st22,
);

my @NAMES = 
(
	"1. Abramov A.",
	"05. Girgushkina",
	"08. Kuznetsova",
	"Kushnikov V.",
	"15. Pridachin",
	"17. Tikhonov R.",
	"21. Shilenkov",
	"22. Shishkina",
);

Lab2Main();

sub menu
{
	my ($q, $global) = @_;
	print $q->header();
	my $i = 0;
	print "<pre>\n------------------------------\n";
	foreach my $s(@NAMES)
	{
		$i++;
		print "<a href=\"$global->{selfurl}?student=$i\">$i. $s</a>\n";
	}
	print "------------------------------</pre>";
}

sub Lab2Main
{
	my $q = new CGI;
	my $st = 0+$q->param('student');
	my $global = {selfurl => $ENV{SCRIPT_NAME}, student => $st};
	if($st && defined $MODULES[$st-1])
	{
		$MODULES[$st-1]->($q, $global);
	}
	else
	{
		menu($q, $global);
	}
}
