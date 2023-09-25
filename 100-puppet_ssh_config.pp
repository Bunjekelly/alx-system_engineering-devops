# SSH client configuration using puppet

exec {'echo':
  command => 'echo PasswordAuthentication no"\n"IdentityFile ~/.ssh/school >> /etc/ssh/ssh_config',
  path    => '/usr/bin'
}
