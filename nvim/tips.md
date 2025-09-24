# Reverse a file

```vim

" ^  ->  matches all lines
" m0 ->  moves each matched line to before line 0 (top of the file), effectively reversing order.

:g/^/m0
```


