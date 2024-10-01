#!/bin/bash

cd ~/.ssh/

read -p "username: " username
read -p "email: " email 

key_name="id_ed25519-$username"

ssh-keygen -t ed25519 -C "$email" -f "$key_name"
ssh-add "$key_name"
xclip -sel clip "$key_name.pub"

fstr="Host github.com-$username\n"
fstr="$fstr    HostName github.com\n"
fstr="$fstr    User git\n"
fstr="$fstr    IdentityFile ~/.ssh/$key_name\n"

echo -e "$fstr" >> ~/.ssh/config

echo "Done. The public key is now in your clipboard."
