function hd --wraps=sudo\ smartctl\ -H\ /dev/sda\ \&\&\ printf\ \"\\n\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\\n\\n\\n\"\ \&\&\ sudo\ smartctl\ -H\ /dev/sdb --description alias\ hd\ sudo\ smartctl\ -H\ /dev/sda\ \&\&\ printf\ \"\\n\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\#\\n\\n\\n\"\ \&\&\ sudo\ smartctl\ -H\ /dev/sdb
  sudo smartctl -H /dev/sda && printf "\n####################################\n\n\n" && sudo smartctl -H /dev/sdb $argv; 
end
