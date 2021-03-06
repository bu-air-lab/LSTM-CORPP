import csv
import numpy as np
import random
from keras.models import load_model

class Learning:
	def __init__(self, path,filenamex,filenamey):

		self.path=path
		self.xdata = np.genfromtxt(path+filenamex, delimiter=',')
		self.ydata = np.genfromtxt(path+filenamey, delimiter=',')
		self.mymodel=load_model('./iter9.h5')
		self.newarray=None

	def get_traj(self,intention):
		(m,n)=self.xdata.shape
		if intention == 'interested':
			randrow=random.randint(0,63)
		else:
			randrow=random.randint(64,m-1)
		randrow_label=self.xdata[randrow,n-1]
		extractx=self.xdata[randrow, n-1-30:n-1]
		label= self.xdata[randrow, n-1]
		extracty=self.ydata[randrow, n-1-30:n-1]
		extractx=extractx.reshape(1,-1)
		extracty=extracty.reshape(1,-1)
		#print 'LABEL: ', label

		#self.ydata = np.genfromtxt(path+filenamey, delimiter=',')
		(p,q)=self.ydata.shape

		
		self.newarray=np.empty([1,2*extractx.shape[1]])
		for i in range(extractx.shape[1]):
					self.newarray[0,2*i]=extractx[0,i]
					self.newarray[0,2*i+1]=extracty[0,i]
		#print 'new_array shape',self.newarray.shape
		self.newarray=self.newarray.reshape(self.newarray.shape[0],int((self.newarray.shape[1]/2)),2)
		return label

	def	predict(self):
		predictions = self.mymodel.predict(self.newarray, verbose=1)
		print 'Classifier output:'
		print predictions
		return predictions

def main():

	a=Learning('./','interposx.csv','interposy.csv')



if __name__=='__main__':
	main()
