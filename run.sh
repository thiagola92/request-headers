firefox http://0.0.0.0:5000 &
sleep 5
kill $!

google-chrome http://0.0.0.0:5000 &
sleep 5
kill $!