while read i; do if [ "$i" = tmp ]; then break; fi; done \
   < <(inotifywait  -e create,open --format '%f' --quiet /tmp --monitor)
