# The following Perl program prints a list of all installed DBI drivers.

use strict;
use warnings;

use DBI;

print map "$_\n", DBI->available_drivers;
