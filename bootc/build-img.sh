/var/bootc image copy-to-storage

cat <<EOF > Containerfile
FROM localhost/bootc
RUN echo "hi" > /usr/hi
EOF

podman build -t "bootc-switch" . 
/var/bootc switch --transport containers-storage localhost/bootc-switch
