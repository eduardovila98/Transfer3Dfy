# Transfer3Dfy
Two functions that rotate the coordinate system, such as to put the central body (origin) and the two positions (for departure and arrival points) in the same plane, where a 2D solver can be used.

### `three2two(r1, r2)`
receives tuples for the 3D position of departure and arrival of the transfer. Returns the 2D positions and the angles, for the transformation.
#### Example:
`r1_2D, r2_2D, angles = three2two(r1, r2)`

### `two2three(angles, r1, r2, v1, v2, x, y, vx, vy)`
given the 3 angles, the function transforms the 2D trajectory into the original 3D coordinate system
