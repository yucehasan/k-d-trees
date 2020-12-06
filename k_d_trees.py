'''
Psuedo-code for decision tree using k-d procedure
=================================================
To find the nearest neighbour using the K-D procedure
    * Determine whether there is only one element in the set 
    under consideration
        * If there is only one, report it.
        * Otherwise, compare the unknown, in the axis of comparison,
        against the current node's threshold. The result determines
        the likely set.
        * Find the nearest neighbor in the likely set using this
        procedure.
        * Determine whether the distance to the nearest neighbor in
        the likely set is less than or equal to the distance to the 
        other set's boundary in the axis of comparison:
            * If it is, then report the nearest neighbor in the likely
            set
            * If it is not, check the unlikely set using this procedure;
            return the nearer of the nearest neighbors in the likely set
            and in the unlikely set. 
'''