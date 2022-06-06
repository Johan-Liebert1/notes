w  -> Move to the next word
b  -> Move to the previous word
o  -> Insert a line below and enter insert mode
O  -> Insert a line above and enter insert mode

v  -> start selection. Then use hjkl to control the selection. Combine with number, like 3j to select next 3 lines. d to delete

(D can be comboed with anything like dw, dj, df<char>, dt<char>)
dd -> Delete a line
dw -> Delete a word
cw -> Delete a word and go into insert mode
dt<char> -> delete everything until the character "char"
D -> Delete the rest of the line
C -> Delete the rest of the line and put into insert mode
S -> Delete the entire line and put you into insert mode

p  -> Paste on the next line
P  -> Paste on the previous line
a  -> Move over one character and enter insert mode
I  -> takes you to the first character of the line and enter into insert mode
A  -> takes you the the end of the line and enter into insert mode
n  -> Goes to the next occurance of the searched character
N  -> Goes to the previous occurance of the searched character
*  -> goes to the next occurance of the character under the cursor
#  -> goes to the previous occurance of the character under the cursor
gg -> takes you the beginning of the file
G  -> takes you the end of the file

Inline (Within a line) moveements
f<char> -> Move to the next occurance of the character 'char'
F<char> -> Move to the previous occurance of the character 'char'

t<char> -> Move up to the next occurance of the character 'char'
T<char> -> Move up to the previous occurance of the character 'char'

(For T and F)
; -> keep iterating over the result of f<char>, t<char> forwards
, -> keep iterating over the result of F<char>, T<char> backwards

x -> delete a single character
s -> delete a single character and go into insert mode

Vertical movement
:<line>   -> Move to line number "line"
<number>j -> Move down by number
<number>w -> Move by the w th word
<number>k -> Move up by number
%         -> Move to the matching bracket 
