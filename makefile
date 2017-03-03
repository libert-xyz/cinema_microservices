# Microservices Project Make File

#VIRTUALENV = $(shell which virtualenv)
VIRTUALENV = $(shell which pyvenv-3.4)
clean: shutdown
	rm -fr microservices.egg-info
	#rm -fr venv


venv:
	$(VIRTUALENV) venv


install: clean venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; python setup.py develop

launch: venv shutdown
	. venv/bin/activate; python3  movie_service/movies/main.py &
	. venv/bin/activate; python3  showtime_service/showtimes/main.py &
	. venv/bin/activate; python3  booking_service/bookings/main.py &
	. venv/bin/activate; python3  user_service/user/main.py &

shutdown:
	ps -ef | grep "movie_service/movies/main.py" | grep -v grep | awk '{print $$2}' | xargs -r kill
	ps -ef | grep "showtime_service/showtimes/main.py" | grep -v grep | awk '{print $$2}' | xargs -r kill
	ps -ef | grep "booking_service/bookings/main.py" | grep -v grep | awk '{print $$2}' | xargs -r kill
	ps -ef | grep "user_service/user/main.py" | grep -v grep | awk '{print $$2}' | xargs -r kill

#wow hello again?
