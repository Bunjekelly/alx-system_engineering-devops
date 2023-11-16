# Fixing the issue of high amount of requests more than its capacity

exec {'fixing':
  provider => shell,
  command => "sed -i 's/15/unlimited/' /etc/default/nginx",
  before   => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
