function cron --wraps='export EDITOR=nvim && crontab -e' --description 'alias cron export EDITOR=nvim && crontab -e'
  export EDITOR=nvim && crontab -e $argv; 
end
