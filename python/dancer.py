# import modules
import sys
from dancing.dance import boogie

# set variable moves to command line arguments sent to script 
# [1:] ensures from second argument ie not name of script 
moves = sys.argv[1:]

boogie(moves)