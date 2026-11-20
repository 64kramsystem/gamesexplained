# First descent facts

- The raster instructions at `$290F–$2916` decrement the obstacle divider at `$2AF8` and reload seven at expiry. The four copies at `$25C2–$25E1` put the characters from `$2CB3/$2CB2/$2CB1/$2CB0` at `$47DE/$47DD/$47B6/$47AD` respectively.
- The collision probe reaches `$2AF2` for sprite 0 low X at least `$EE` with high X clear. Either matrix comparison can reach the same branch. Stepping the first comparison with equal cells continued to the second. A mismatch reached `$2AF2` and wrote `$32` to `$2D37`.
