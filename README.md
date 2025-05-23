Trees - the statuses we care about initially are: 
1. In a field
2. Active, but not in a field
3. Inactive, but used to be in a field
4. Inactive, dormant

For a basic tree we want to include the following information:
* Species, Genus (optional), Group, Status, Tag(s)
* A tree may have one or many tags.
* Status - can be calculated (if it has a field or not), maybe a function to make it active/inactive?

A field can have multiple trees. A tree can be in multiple fields. A tree may have current and past fields (some of which are relevant).

For a tree in a field, additional bits of information may be needed (e.g. colour of band).

We want to return:
* List of all trees by status.
* For each field, its unique list of trees and traits.
* This may include images for each tree.
