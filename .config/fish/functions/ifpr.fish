function ifpr --wraps='sudo openvpn Downloads/gwcwb-UDP4-1194-infcuritiba-config.ovpn' --wraps='printf infcuritiba | sudo openvpn Downloads/gwcwb-UDP4-1194-infcuritiba-config.ovpn' --wraps=' sudo openvpn Downloads/gwcwb-UDP4-1194-infcuritiba-config.ovpn' --wraps=' sudo openvpn Documents/gwcwb-UDP4-1194-infcuritiba-config.ovpn' --description 'alias ifpr  sudo openvpn Documents/gwcwb-UDP4-1194-infcuritiba-config.ovpn'
   sudo openvpn Documents/gwcwb-UDP4-1194-infcuritiba-config.ovpn $argv; 
end
