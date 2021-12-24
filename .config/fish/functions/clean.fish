function clean --wraps='yay -Yc && paccache -rk1 && sudo pacman -Qtdq | sudo pacman -Rns -' --description 'alias clean yay -Yc && paccache -rk1 && sudo pacman -Qtdq | sudo pacman -Rns -'
  yay -Yc && paccache -rk1 && sudo pacman -Qtdq | sudo pacman -Rns - $argv; 
end
