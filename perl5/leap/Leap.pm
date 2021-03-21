# Declare package 'Leap'
package Leap;
use strict;
use warnings;
use Exporter qw<import>;
our @EXPORT_OK = qw<is_leap_year>;

sub is_leap_year {
  my ($year) = @_;
  my $leap_year = 0;
  if ($year % 4 ) {
    if(! $year % 100 ) {
       if (! $year % 400) {
        $leap_year = 1;
       }
    }
  }
  else {
        $leap_year = 0;
  }
  return $leap_year;
}

1;
