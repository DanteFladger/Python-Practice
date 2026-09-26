# Rules of Thumb:
## Default Value
- Only give a default when there's a sensible value most callers would choose, and callers who don't care shouldn't have to think about it
- No default when the value is the core of what the function does, and every caller needs to consciously choose it. 
