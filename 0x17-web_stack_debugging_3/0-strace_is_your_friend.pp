# puppet file to fix apache error, replacing phpp with php in wp settings

exec {'exec':
    command  => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php;
    service apache2 restart',
    provider => shell
  }
