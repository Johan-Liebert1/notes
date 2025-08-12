#!/bin/bash

# Open fd 3 (the first free fd) as a bidirectional fd "<>"
# Then connect to google.com on port 80 using bash's /dev/tcp feature
exec 3<>/dev/tcp/google.com/80


lines=(
    'GET /ping HTTP/1.1'
    'Host: google.com'
    'Connection: Close'
    ''
)

# while writing to an fd, we need to specify '&' else it's redirected to a file named '3'
printf "%s\r\n" "${lines[@]}" >&3

# the read builtin only reads one line at a time but we need to read multiple lines
# hence the while
while read -r data <&3; do
    echo "From server: $data"
done


# Close the fd
exec 3>&-
