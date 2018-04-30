import random
import noise

class TestGenerator(object):

	random.seed(3)
	max_n = 1000
	max_m = 1000
	min_altitude = 0
	max_altitude = pow(10, 6)
	output_file_no = 0

	def __init__(self):

		# SAMPLE CASES

		# sample_test_1 = [[1, 2, 3, 4], [1, 1, 1, 8]]
		# sample_test_2 = [[0, 3], [4, 0]]
		# sample_test_3 = [[1], [2], [3], [4], [5], [4], [3], [2], [1]]

		# self.output_to_file( sample_test_1 )
		# self.output_to_file( sample_test_2 )
		# self.output_to_file( sample_test_3 )

		# AUTOMATICALLY GENERATED CASES

		# Generate small gradient terrain with small max altitude.
		self.output_to_file( self.generate_gradient_terrain(30, 30, max_altitude = pow(10, 1), frequency=64) )
		self.output_to_file( self.generate_gradient_terrain(30, 30, max_altitude = pow(10, 1), frequency=16) )
		self.output_to_file( self.generate_gradient_terrain(30, 30, max_altitude = pow(10, 1), frequency=4) )

		# Generate small gradient terrain with large max altitude.
		self.output_to_file( self.generate_gradient_terrain(30, 30, max_altitude = pow(10, 4), frequency=64) )
		self.output_to_file( self.generate_gradient_terrain(30, 30, max_altitude = pow(10, 4), frequency=16) )
		self.output_to_file( self.generate_gradient_terrain(30, 30, max_altitude = pow(10, 4), frequency=4) )

		# Generate medium gradient terrain with small max altitude.
		self.output_to_file( self.generate_gradient_terrain(100, 100, max_altitude = pow(10, 2), frequency=64) )
		self.output_to_file( self.generate_gradient_terrain(100, 100, max_altitude = pow(10, 2), frequency=16) )
		self.output_to_file( self.generate_gradient_terrain(100, 100, max_altitude = pow(10, 2), frequency=4) )

		# Generate medium gradient terrain with large max altitude.
		self.output_to_file( self.generate_gradient_terrain(100, 100, max_altitude = pow(10, 5), frequency=64) )
		self.output_to_file( self.generate_gradient_terrain(100, 100, max_altitude = pow(10, 5), frequency=16) )
		self.output_to_file( self.generate_gradient_terrain(100, 100, max_altitude = pow(10, 5), frequency=4) )


		# Generate large gradient terrain with small max altitude.
		self.output_to_file( self.generate_gradient_terrain(1000, 1000, max_altitude = pow(10, 3), frequency=64) )
		self.output_to_file( self.generate_gradient_terrain(1000, 1000, max_altitude = pow(10, 3), frequency=16) )
		self.output_to_file( self.generate_gradient_terrain(1000, 1000, max_altitude = pow(10, 3), frequency=4) )

		# Generate large gradient terrain with large max altitude.
		self.output_to_file( self.generate_gradient_terrain(1000, 1000, max_altitude = pow(10, 6), frequency=64) )
		self.output_to_file( self.generate_gradient_terrain(1000, 1000, max_altitude = pow(10, 6), frequency=16) )
		self.output_to_file( self.generate_gradient_terrain(1000, 1000, max_altitude = pow(10, 6), frequency=4) )

		# Generate random extra-small square and rectangle terrains.
		self.output_to_file( self.generate_random_terrain(1, 1) )
		self.output_to_file( self.generate_random_terrain(2, 2) )
		self.output_to_file( self.generate_random_terrain(3, 3) )
		self.output_to_file( self.generate_random_terrain(2, 1) )
		self.output_to_file( self.generate_random_terrain(1, 2) )
		self.output_to_file( self.generate_random_terrain(10, 1) )
		self.output_to_file( self.generate_random_terrain(1, 10) )
		self.output_to_file( self.generate_random_terrain(2, 10) )
		self.output_to_file( self.generate_random_terrain(10, 2) )

		# Generate random small square terrain.
		self.output_to_file( self.generate_random_terrain(30, 30) )

		# Generate random medium square terrain.
		self.output_to_file( self.generate_random_terrain(100, 100) )

		# Generate random large square terrain.
		self.output_to_file( self.generate_random_terrain(1000, 1000) )

		# Generate small spiral terrain (always increasing).
		self.output_to_file( self.generate_spiral_terrain(30, 30) )

		# Generate large spiral terrain (always increasing -- answer should print 1,000,000 characters!)
		self.output_to_file( self.generate_spiral_terrain(1000, 1000) )

		# Generate small flat terrain
		self.output_to_file( self.generate_flat_terrain( 30, 30 ) )

		# Generate large flat terrain
		self.output_to_file( self.generate_flat_terrain( 1000, 1000 ) )

		# Generate large terrain with all same length longest paths.
		self.output_to_file( self.generate_flat_slope_terrain( 1000, 1000 ) )

		# Generate small snail terrain from center.
		self.output_to_file( self.generate_snail_terrain(31, 31))

		# Generate large snail terrain from center.
		self.output_to_file( self.generate_snail_terrain(999, 999))

		# MANUALLY CONSTRUCTED CASES

		# Generate large gradient terrain with manually constructed longest path.
		self.output_to_file( self.generate_custom_terrain_1() )

		# Custom inputs
		self.output_to_file( self.generate_custom_terrain_2() )
		self.output_to_file( self.generate_custom_terrain_3() )
		self.output_to_file( self.generate_custom_terrain_4() )
		self.output_to_file( self.generate_custom_terrain_5() )
		self.output_to_file( self.generate_custom_terrain_6() )
		self.output_to_file( self.generate_custom_terrain_7() )
		self.output_to_file( self.generate_custom_terrain_8() )
		self.output_to_file( self.generate_custom_terrain_9() )
		self.output_to_file( self.generate_custom_terrain_10() )
		
	# Output to file.
	def output_to_file(self, grid):
		n = len(grid)
		m = len(grid[0])

		with open( str(self.output_file_no) + ".in", 'w', newline='\n') as f:
			f.write( str(n) + " " + str(m) + "\n" )
			for i in range(n):
				for j in range(m):
					f.write( str( grid[i][j] ) + (" " if j < m - 1 else "") )
				f.write( "\n" )

		self.output_file_no += 1

	# Generates a gradient terrain (noise)
	def generate_gradient_terrain(self, n, m, max_altitude = pow(10, 6), frequency = 16.0):
		random.seed()
		octaves = random.random()
		freq = frequency * octaves
		output = []
		for y in range(n):
			output.append([])
			for x in range(m):
				n = int(noise.pnoise2(x/freq, y / freq, 1) * max_altitude + max_altitude * 0.7)
				if n < 0: n = 0
				if n > max_altitude: n = max_altitude
				output[y].append(n)
		return output

	# Generates a flat terrain (no descent)
	def generate_flat_terrain(self, n, m):
		r =  random.randint( 0, self.max_altitude)
		output = []
		for y in range(n):
			output.append([])
			for x in range(m):
				output[y].append( r )
		return output

	# Generates a random terrain
	def generate_random_terrain(self, n, m):
		output = []
		for y in range(n):
			output.append([])
			for x in range(m):
				output[y].append( random.randint( 0, self.max_altitude ) )
		return output

	# Generates a spirally increasing terrain
	def generate_spiral_terrain(self, n, m):
		output = []
		for y in range(n):
			output.append([])
			for x in range(m):
				if (y % 2 == 0):
					output[y].append( n * y + x )
				else:
					output[y].append( n * (y + 1) - x - 1 )
		return output

	# Generates a flat sloped terrain
	def generate_flat_slope_terrain(self, n, m):
		output = []
		for y in range(n):
			output.append([])
			for x in range(m):
				output[y].append( x )
		return output

	# Generate a snail terrain
	def generate_snail_terrain(self, X, Y):
		x = y = 0
		dx = 0
		dy = -1
		midX = int(X / 2)
		midY = int(Y / 2)
		count = 0;

		output = []
		for row in range(Y):
			output.append([])
			for col in range(X):
				output[row].append( 0 )

		for i in range(max(X, Y)**2):
			if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
				#print (midX + x, midY - y)
				output[midY - y][midX + x] = count
			if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
				dx, dy = -dy, dx
			x, y = x+dx, y+dy
			count += 1

		return output

	# Generate a custom case 1
	def generate_custom_terrain_1(self):
		grid = self.generate_gradient_terrain(1000, 1000)
		for x in range(len(grid[40])):
			grid[40][x] = x
		return grid

	# Generate a custom case 2-5
	def generate_custom_terrain_2(self):
		return [[1, 2, 3, 4, 5], [1, 1, 1, 1, 1], [5, 4, 3, 2, 1]]

	def generate_custom_terrain_3(self):
		return [[1, 1, 4, 1, 4, 1, 1], [1, 1, 5, 1, 5, 1, 1], [10, 9, 8, 1, 6, 7, 10], [1, 1, 3, 1, 4, 1, 1], [1, 1, 2, 1, 2, 1, 1]]

	def generate_custom_terrain_4(self):
		return [[1, 1, 3], [9, 1, 2], [1, 1, 1]]

	def generate_custom_terrain_5(self):
		return [[5, 0, 0], [4, 0, 0], [3, 4, 5], [4, 0, 0], [5, 0, 0]]

	def generate_custom_terrain_6(self):
		return [[3, 4, 5], [2, 0, 6], [9, 8, 7]]

	def generate_custom_terrain_7(self):
		return [[6, 0, 7, 0], [0, 0, 0, 0], [8, 0, 0, 0], [0, 0, 0, 9]]

	def generate_custom_terrain_8(self):
		return [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]

	def generate_custom_terrain_9(self):
		return [[0, 0, 0, 0, 0], [1, 0, 0, 0, 1]]

	def generate_custom_terrain_10(self):
		return [[1, 1, 3, 1, 1], [1, 1, 4, 1, 1], [3, 4, 5, 4, 3], [1, 1, 4, 1, 1], [1, 1, 3, 1, 1]]

class NaiveSolver(object):
	def __init__(self):
		pass

if __name__ == "__main__":

	gen = TestGenerator();