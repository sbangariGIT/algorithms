# H-Index
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

## Solution
This one was a little tricky to understand. But the best way thing that helped me to solve was to visualize a graph with x and y axises being # of citations and # number of papers. We use that as a counting sort.

For example:
- `[3, 0, 6, 1, 5]` can be sorted using count sort to `[1, 1, 0, 1, 0, 2]`
1. This means we have 1 paper with 0 citations, 1 paper with 1 citation, 0 with 2 citations, 1 with 3 citations, 0 with 4 citations and 2 with 5 citations*. We count paper with 6 citations within 5 since h index can only be max of the number of papers.

2. Now we iterate from the back and aggregate as we are moving from behind. If index =< aggregate we return index.