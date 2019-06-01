Engineer-and-bulbs
==================

## Problem definition

There are `1 000` light bulbs numerated from `1` to `1 000`. 
An engineer created a switching mechanism, which switches a state of a single 
light bulb (from *turned off* to *turned on* and vice versa) in a peculiar way. 
If the switch was pressed **K** times, the state of all light bulbs which index is 
divided by **K** changes. 

At the beginning, all light bulbs are turned off. 

Experiment starts:

After first switch (which is `K = 1`) all light bulbs are turned on.
After second switch (which is `K = 2`) even light bulbs are turned off, and odd light bulbs stay turned on.
After third switch (`K = 3`) all bulbs, which numbers are odd and divisible by `3` and all 
bulbs, which numbers are even and divisible by `3`, are turned on. Rest of the light bulbs are turned off.

Find which bulbs are switched on at the end of experiment.

## Computational solution

```
python bulbs_game.py
```
