import threading, time

def loop_visualize(self, event, stop):
	print("Begin of a thread")
	while not(stop.is_set()):
		event_is_set = event.wait()
		print("Running")
		time.sleep(1)
	print("End of a thread")


