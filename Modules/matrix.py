import math


class Matrix:
	"""
	Matrix is a class who can help you you work with Matrix in yours projects
	  
	  it take 2 parameters
		you can instancing Matrix like
			* A = Matrix(list) with list = a matrix list of interger or float value 
			* A = Matrix(row,col) row and col are interger who describe the Matrix row length and column length
			* A = Matrix(int) it same with Matrix([[int]])
			* A = Matrix(Matrix.Dim(row,col)) you define the Matrix row and column by the subclass Dim of Matrix
	"""
	class Dim:
		def __init__(self,row,col):
			self.row = row
			self.col = col
		def __repr__(self):
			return "{}×{}".format(self.row,self.col)
	
	
	def __init__(self, row, col=0):
		self.__Matrix = None
		self.square = False
		if col==0 and type(row)==int:
			self.__Matrix = [[row]]
		elif col != 0 and type(row)==type(col)==int:
			self.__Matrix = []
			for row in range(row):
				self.__Matrix.append([])
				for i in range(col):
					self.__Matrix[row].append(0)
		elif type(row) == list and col == 0:
			for row_ in row:
				if type(row_) != list:
					raise ValueError("All Matrix row must be 'list' type")
				for col_ in row_:
					if type(col_) not in [int,float]:
						raise ValueError("All Matrix value must be an interger or float")
			for row_ in row:
				if len(row[0]) != len(row_):
					raise TypeError("All Matrix row would have same length")
			self.__Matrix = row
		elif type(row)==self.Dim:
			self.__Matrix = Matrix(row.row,row.col).getMatrix()
		
		self.DIM = self.Dim(len(self.__Matrix),len(self.__Matrix[0]))
		self.square = True if self.DIM.col == self.DIM.row else False

	def __repr__(self):
			matrix = ""
			strMatrix = []
			for row in range(self.DIM.row):
				strMatrix.append([])
				for col in range(self.DIM.col):
					strMatrix[row].append(str(round(self.__Matrix[row][col],2)).center(5))
			for i,row in enumerate(strMatrix):
				srow = "|"+"  ".join(row)+"|"
				size = len(srow)-2
				matrix += srow
				if i != len(strMatrix)-1:
					matrix += "\n|"+(" "*size)+"|\n"
			start = "\n|``"+(" "*(size-4))+"``|\n"
			end = "\n|,,"+(" "*(size-4))+",,|\n"
			if str(self.DIM) == "1×1":
				return "\n"+"[{}]".format(strMatrix[0][0]).center(50)+"\n"
			return start+matrix+end
	
	def getMatrix(self):
		return self.__Matrix
	
	def __add__(self, matrix):
		if type(matrix) != Matrix or str(self.DIM) != str(matrix.DIM) :
			raise TypeError("we can add only matrix of same Dimensions !")
		A = self.getMatrix()
		B = matrix.getMatrix()
		T = Matrix(self.DIM).getMatrix()
		
		for row in range(self.DIM.row):
			for col in range(self.DIM.col):
				T[row][col] = A[row][col] + B[row][col]
		
		return Matrix(T)
	
	def __sub__(self, matrix):
		if type(matrix) != Matrix or str(self.DIM) != str(matrix.DIM) :
			raise TypeError("we can subtract only matrix of same Dimensions !")
		A = self.getMatrix()
		B = matrix.getMatrix()
		T = Matrix(self.DIM).getMatrix()
		
		for row in range(self.DIM.row):
			for col in range(self.DIM.col):
				T[row][col] = A[row][col] - B[row][col]
		
		return Matrix(T)
	
	def transpose(self):
		A = self.getMatrix()
		T = Matrix(self.DIM.col,self.DIM.row).getMatrix()
		for row in range(self.DIM.row):
			for col in range(self.DIM.col):
				T[col][row] = A[row][col]
		return Matrix(T)

	def __mul__(self, other):
		A = self.getMatrix()
		
		if type(other) in (float,int):
			T = Matrix(self.DIM).getMatrix()
			for row in range(self.DIM.row):
				for col in range(self.DIM.col):
					T[row][col] = A[row][col] * other
		elif type(other) == Matrix:
			if self.DIM.col != other.DIM.row:
				raise TypeError("we can not multiply {} Matrix by {} Matrix". format (self.DIM,other.DIM))
			else:
				B = other.getMatrix()
				T = Matrix(self.DIM.row,other.DIM.col).getMatrix()
				for row in range(self.DIM.row):
					for col in range(other.DIM.col):
						k = 0
						while k < other.DIM.row:
							T[row][col] += A[row][k] * B[k][col]
							k += 1
		else:
			raise TypeError("we can only multiply Matrix with Matrix , int and float")
		return Matrix(T)

	def __rmul__(self,other):
		return self.__mul__(other)
	
	def __truediv__(self, other):
		A = self.getMatrix()
		
		if type(other) in (float,int):
			T = Matrix(self.DIM).getMatrix()
			for row in range(self.DIM.row):
				for col in range(self.DIM.col):
					T[row][col] = A[row][col] / other
		elif type(other) == Matrix:
			if str(self.DIM) != str(other.DIM):
				raise TypeError("we can divide only matrix of same Dimensions !")
			A = self.getMatrix()
			B = other.getMatrix()
			T = Matrix(self.DIM).getMatrix()
			for row in range(self.DIM.row):
				for col in range(self.DIM.col):
					T[row][col] = A[row][col] / B[row][col]
		else:
			raise TypeError("we can only divide Matrix with Matrix , int and float")
		return Matrix(T)
	
	def __rtruediv__(self,other):
		A = self.getMatrix()
		
		if type(other) in (float,int):
			T = Matrix(self.DIM).getMatrix()
			for row in range(self.DIM.row):
				for col in range(self.DIM.col):
					T[row][col] = other / A[row][col]
		else:
			raise TypeError("we can only divide Matrix with Matrix , int and float")
		return Matrix(T)
	
	def __floordiv__(self, other):
		A = self.getMatrix()
		
		if type(other) in (float,int):
			T = Matrix(self.DIM).getMatrix()
			for row in range(self.DIM.row):
				for col in range(self.DIM.col):
					T[row][col] = A[row][col] // other
		elif type(other) == Matrix:
			if str(self.DIM) != str(other.DIM):
				raise TypeError("we can divide only matrix of same Dimensions !")
			A = self.getMatrix()
			B = other.getMatrix()
			T = Matrix(self.DIM).getMatrix()
			for row in range(self.DIM.row):
				for col in range(self.DIM.col):
					T[row][col] = A[row][col] // B[row][col]
		else:
			raise TypeError("we can only divide Matrix with Matrix , int and float")
		return Matrix(T)
	
	def __rfloordiv__(self,other):
		A = self.getMatrix()
		
		if type(other) in (float,int):
			T = Matrix(self.DIM).getMatrix()
			for row in range(self.DIM.row):
				for col in range(self.DIM.col):
					T[row][col] = other // A[row][col]
		else:
			raise TypeError("we can only divide Matrix with Matrix , int and float")
		return Matrix(T)
	
	def __mod__(self, other):
		A = self.getMatrix()
		
		if type(other) in (float,int):
			T = Matrix(self.DIM).getMatrix()
			for row in range(self.DIM.row):
				for col in range(self.DIM.col):
					T[row][col] = A[row][col] % other
		elif type(other) == Matrix:
			if str(self.DIM) != str(other.DIM):
				raise TypeError("we can divide only matrix of same Dimensions !")
			A = self.getMatrix()
			B = other.getMatrix()
			T = Matrix(self.DIM).getMatrix()
			for row in range(self.DIM.row):
				for col in range(self.DIM.col):
					T[row][col] = A[row][col] % B[row][col]
		else:
			raise TypeError("we can only divide Matrix with Matrix , int and float")
		return Matrix(T)

	def __rmod__(self,other):
		A = self.getMatrix()
		
		if type(other) in (float,int):
			T = Matrix(self.DIM).getMatrix()
			for row in range(self.DIM.row):
				for col in range(self.DIM.col):
					T[row][col] = other % A[row][col]
		else:
			raise TypeError("we can only divide Matrix with Matrix , int and float")
		return Matrix(T)
	
	def __pow__(self,interger):
		T = Matrix(self.getMatrix())
		
		if type(interger) == int:
			for i in range(interger-1):
				T = T.__mul__(self)
		else:
			raise TypeError("we can only pow Matrix with int")
		return T

	def cofactor(self, row, col):
		if not self.square:
			raise TypeError("Sorry I can only find the cofactor of square Matrix")
		
		A = self.getMatrix()
		T = list()
		
		if self.DIM.row == 1:
			return Matrix(A[0][0])
			
		for row_ in range(self.DIM.row):
			if row_ == row :
				continue
			TempRow = list()
			for col_ in range(self.DIM.col):
				if col_ == col :
					continue
				else:
					TempRow.append(A[row_][col_])
			T.append(TempRow)
		
		return Matrix(T)

	def det(self):
		if not self.square:
			raise TypeError("Sorry I can only find the determinant of square Matrix")
		
		A = self.getMatrix()
		Det = 0
		row = 0
		if self.DIM.row == 1:
			return A[0][0]
		for col in range (self.DIM.col):
			Det += A[row][col]*math.pow(-1,row + col)*self.cofactor(row, col).det()
		return int(Det)

	def adjoint(self):
		if not self.square:
			raise TypeError("Sorry I can only find the adjoint of square Matrix")
		A = self.getMatrix()
		T = list()
		if self.DIM.row == 1:
			return Matrix([[1]])
		for row in range(self.DIM.row):
			TempRow = list()
			for col in range(self.DIM.col):
				TempRow.append(self.cofactor(row,col).det()*math.pow(-1, row + col))
			T.append(TempRow)
		return Matrix(T).transpose()
	
	def invert(self):
		return self.adjoint().__truediv__(self.det())