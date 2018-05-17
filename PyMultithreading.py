#Laura Davis 28 June 2017

#Lesson and source code from YouTube user Trevor Payne
#This program demonstrates the usefulness of multithreading
#in Python script. 
#Multithreading means running multiple tasks in parallel on the cpu.
#Each core in a cpu can run multiple threads at once. It is useful
#for running many tasks that are independent of each other. All threads
#communicate with the main thread. WARNING: Don't let two threads access
#the same data at once. This can lead to data corruption and crashes. 

import threading, time, random, sys

#a simple example of multithreading
#these run very quickly and must sometimes be stalled
def Splitter(words):
	myList = words.split()
	newList = []
	while (myList):
		newList.append(myList.pop(random.randrange(0, len(myList))))
	print (' '.join(newList))
	
if __name__ == '__main__':
	sentence = "Coding is the best."
	numOfThreads = 5
	threadList = []
	
	print ("STARTING....\n")
	for i in range(numOfThreads):
		t = threading.Thread(target = Splitter, args = (sentence,))
		t.start()
		threadList.append(t)
	
	print ("\nThread Count: " + str(threading.activeCount()))
	print ("EXITING...\n")

#A more complex example of multithreading
#This bit of code allows program to run on Python 2.6 and 3.3	
try:
	import Queue
except: 
	import queue as Queue
	
class Producer:
	def __init__(self):
		self.food = ["ham", "soup", "salad"]
		self.nextTime = 0
	def run(self):
		global q
		while (time.clock() < 10):
			if (self.nextTime < time.clock()):
				f = self.food[random.randrange(len(self.food))]
				q.put(f)
				print ("Adding" + f)
				self.nextTime += random.random()
		
class Consumer:
	def __init__(self):
		self.nextTime = 0
	def run(self):
		global q 
		while (time.clock() < 10):
			if (self.nextTime < time.clock() and not q.empty()):
				f = q.get()
				print("Removing" + f)
				self.nextTime += random.random() * 2
	
#calls main, creates classes	
if __name__ == '__main__':
	q = Queue.Queue(10)
	
	p = Producer()
	c = Consumer()
	pt = threading.Thread(target = p.run, args=())
	ct = threading.Thread(target = c.run, args=())
	pt.start()
	ct.start()
	
sys.exit(1)
				

