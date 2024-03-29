General Notes
	Large inputs such as 1000x1000 will TLE for brute force DFS solutions.
	Extra-small and rectangular inputs test off-by-one grid or directional errors.
	Zig-Zag and Snail terrains are worse-case degenerate scenarios for DFS and other
	non-optimal solutions as each vertex has multiple possible directions to branch off.
	Flat terrain test for "no descent" case.
	Flat sloped terrain tests for lexicographical order.
	Procedural terrains tests based on simulated natural data.
	Custom test cases and random cases test for correct 
	starting point (highest altitude -- or if same, lower Y -- or if same, lower X)
	and lexicographical order.

Sample Case ID

0 - 2: Generate small procedural terrain with small max altitude -- 30x30
3 - 5: Generate small procedural terrain with large max altitude -- 30x30
6 - 8: Generate medium procedural terrain with small max altitude -- 100x100
9 - 11: Generate medium procedural terrain with large max altitude -- 100x100
12 - 14: Generate large procedural terrain with small max altitude -- 1000x1000
15 - 17: Generate large procedural terrain with large max altitude -- 1000x1000
18 - 26: Generate random extra-small square and rectangle terrains -- various small sizes ranging 1x1 to 10x2
27: Generate small square terrain with random values -- 30x30
28: Generate medium square terrain with random values -- 100x100
29: Generate large square terrain with random values -- 1000x1000
30: Generate small zig-zag (spiral) terrain (increasing top to bottom, left to right) -- 30x30
31: Generate large zig-zag (spiral) terrain (increasing top to bottom, left to right) -- 1000x1000
32: Generate small flat terrain -- 30x30
33: Generate large flat terrain -- 1000x1000
34: Generate large flat sloped terrain (same length longest paths) -- 1000x1000
35: Generate small snail terrain (increases outward from center spirally) -- 30x30
36: Generate large snail terrain (increases outward from center spirally) -- 30x30
37 - 46: Generate custom inputs -- various small testable sizes