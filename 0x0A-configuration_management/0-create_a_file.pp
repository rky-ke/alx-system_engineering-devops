#creates a file in /tmp
file { 'school' :
  path    => '/tmp/school',
  ensure  => 'file',
  content => 'I love puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data'
}
