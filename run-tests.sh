sudo /etc/init.d/xvfb start

# Now we have to set the DISPLAY env variable so Firefox and Chrome know where to open the browser.
export DISPLAY=:99

grunt test

cp -avr src /usr/share/nginx/www/src
cp -avr libs /usr/share/nginx/www/libs
cp -avr jsx /usr/share/nginx/www/jsx

cd func_tests
./runtests.py