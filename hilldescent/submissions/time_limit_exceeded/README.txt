dfsJavaSolution.java calculates a correct longest hill descent for
small or medium inputs but TLE's for larger inputs because it uses 
brute-force graph traversal DFS instead of DP. Note the Java solution
takes input through Standard Input (Scanner).

solNoDp.cpp is the same solution as the correct implementation with DP removed
which will result in DP.

tle-IO.cpp is the same solution as the correct implementation but it does not
have fast printing (using cout instead of printf, as well as other output issues)
which results in TLE.