if echo $USER | grep -i "t8.corp"; then
  # ENV
  fstab_line="//{{ srv_name_lower }}{{ share_name_modded }} $HOME/ShareDocs/{{ dst_share_name }}    cifs    sec=krb5,noauto,user    0 0"

  # SHARES
  ## //{{ srv_name_lower }}{{ share_name_modded }}
  if !  grep -Fxq "${fstab_line}" /etc/fstab; then
    echo "" | sudo tee -a /etc/fstab &> /dev/null
    echo "# $USER //{{ srv_name_lower }}{{ share_name_modded }}" | sudo tee -a /etc/fstab &> /dev/null
    echo "${fstab_line}" | sudo tee -a /etc/fstab &> /dev/null
  fi

  # MOUNTS
  smbclient //{{ srv_name_lower }}{{ share_name_modded }} --kerberos -c quit &> /dev/null
  if [ $? -eq 0 ]; then
    mkdir -p $HOME/ShareDocs/{{ dst_share_name }} &> /dev/null
    mount $HOME/ShareDocs/{{ dst_share_name }} &> /dev/null
  fi
fi