#!/bin/bash

myVar="Hey Buddy, How are you?"
myVarLength=${#myVar}
echo "Length of the myVar is $myVarLength"

# Convert to upper case
echo "Upper case is ---- ${myVar^^}"

# Convert to lower case
echo "Lower case is ${myVar,,}"

# Replace a substring
newVar=${myVar/Buddy/Paul}
echo "New Var is $newVar"

# Extract a substring (from position 4, length 5)
substring=${myVar:4:5}
echo "Substring (from position 4, length 5) is '$substring'"

# Extract a substring from a starting position to the end
substring_from_position=${myVar:4}
echo "Substring from position 4 to the end is '$substring_from_position'"

# Extract a substring from the end (negative index)
substring_from_end=${myVar: -4}
echo "Last 4 characters are '$substring_from_end'"

# Find position of a substring
subStr="Buddy"
position=$(expr index "$myVar" "$subStr")
if [[ $position -ne 0 ]]; then
  echo "Position of '$subStr' is $position"
else
  echo "'$subStr' not found"
fi

# Remove substring from start
remove_start=${myVar#Hey }
echo "String after removing 'Hey ' from start is '$remove_start'"

# Remove substring from end
remove_end=${myVar%you?}
echo "String after removing 'you?' from end is '$remove_end'"

# Remove shortest match of substring from start
shortest_match_start=${myVar#* }
echo "Shortest match removed from start is '$shortest_match_start'"

# Remove shortest match of substring from end
shortest_match_end=${myVar% *}
echo "Shortest match removed from end is '$shortest_match_end'"

# Remove longest match of substring from start
longest_match_start=${myVar##* }
echo "Longest match removed from start is '$longest_match_start'"

# Remove longest match of substring from end
longest_match_end=${myVar%% *}
echo "Longest match removed from end is '$longest_match_end'"

