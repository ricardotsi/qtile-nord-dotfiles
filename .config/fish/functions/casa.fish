function casa --wraps='nmcli connection up Uai-Fai_2.4GHz passwd-file ~/Documents/wifi' --description 'alias casa nmcli connection up Uai-Fai_2.4GHz passwd-file ~/Documents/wifi'
  nmcli connection up Uai-Fai_2.4GHz passwd-file ~/Documents/wifi $argv; 
end
