Source of information: Wikipedia

The Stable Matching Problem:

A matching is a bijection from the elements of one set to the elements of the other set. A matching is not stable if:

There is an element of A the first matched set preferes some given element B of the second matched set over the element to which A is already matched
B also prefers A over the element to which B is already matched

In other words, a matching is stable when there does not exist any pair (A, B) which both prefer each other to their current partner under the matching

Example:

A: YXZ B: ZYX  C: XZY and X: BAC Y: CBA Z: ACB
A,B,C Men and XYZ are women

There are three stable solutions to this matching arrangement:

Men get their first choice and women their third.
Women get their first choice and men get their third.
All participants get their second choice.

Solutions:

Gale-Shapley Algorithm
In 1962, David Gale and Lloyd Shapley proved that, for any equal number of men and women it is always possible to solve the SMP and male all marriages stable.They presented an algorithm to do so.

Steps:
Initialize the first round such that all the people have no preference.
In the first round each unengaged man proposes to the women he prefers most
The women reply maybe to her suitor that she prefers and no to all the other suitors. She is then provisionally “engaged” to the suitor she most prefers so far, and that suitor is likewise provisionally “engaged” - lets call this pseudo engagement.
In each subsequent round we follow the following:
Each unengaged man proposes to the most-preferred women to whom he has not yet proposed. Regardless of whether she is already engaged (besharam)
Each woman replies “maybe” if she is currently not engaged or if she prefers this man over her current partner in which case the current partner becomes engaged. Essentially women can trade up.
Repeat until everyone is engaged.
This algorithm is guaranteed to produce a stable marriage for all participants in time O(n^2) where n is the number of men or women.


Among all possible options it always yields the one that is best for all men among all stable matchings.


## Implementation