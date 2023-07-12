#creates a file in /tmp
file { 'school' :
  path    => '/tmp'
  content => 'I love puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data'
}
