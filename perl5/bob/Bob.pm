# Declare package 'Bob'
package Bob;
use strict;
use warnings;
use Exporter 'import';
our @EXPORT_OK = qw(hey);

sub hey {
  my ($msg) = @_;

#  =begin comment
#  Bob is a lackadaisical teenager. In conversation, his responses are very limited.
#  Bob answers 'Sure.' if you ask him a question, such as "How are you?".
#  He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
#  He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
#  He says 'Fine. Be that way!' if you address him without actually saying anything.
#  He answers 'Whatever.' to anything else.
#  =end comment

  if ($msg =~ /.*\?$/) {
    return 'Sure.';
  }
  if ($msg =~ /[A-Za-z0-9]$/) {
    return 'Whoa, chill out!';
  }
  if ($msg =~ /[A-Z]\?/) {
    return  "'Calm down, I know what I'm doing!";
  }
  if (!$msg) {
    return 'Fine. Be that way'
  }
  return 'Whatever.'; ## if nonsense supplied
}

1;
