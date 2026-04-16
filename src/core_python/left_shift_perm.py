from enum import IntFlag, auto

class Permission(IntFlag):
    NONE            = 0
    READ            = auto() # 1  (2^0)
    WRITE           = auto() # 2  (2^1)
    DELETE          = auto() # 4  (2^2)
    MANAGE_USERS    = auto() # 8  (2^3)
    MANAGE_BILLING  = auto() # 16 (2^4)
    
    # Pre-defined Roles (Combinations)
    GUEST = READ
    EDITOR = READ | WRITE
    ADMIN = READ | WRITE | DELETE | MANAGE_USERS | MANAGE_BILLING

class User:
    def __init__(self, name, permissions=Permission.NONE):
        self.name = name
        # We store permissions as a single integer
        self.permissions = permissions

    def add_permission(self, perm: Permission):
        """Logic: Current bits OR New bits"""
        self.permissions |= perm

    def remove_permission(self, perm: Permission):
        """Logic: Current bits AND (NOT New bits)"""
        self.permissions &= ~perm

    def has_permission(self, perm: Permission):
        """Logic: Does (Current AND Target) equal Target?"""
        return (self.permissions & perm) == perm

    def __repr__(self):
        return f"User({self.name}, Perms: {self.permissions.name} [{int(self.permissions)}])"

# --- Testing the Logic ---
sathish = User("Sathish", Permission.GUEST)
print(f"Initial: {sathish}")

# Grant Editor status
sathish.add_permission(Permission.EDITOR)
print(f"Upgraded: {sathish}")

# Check if he can Delete (He shouldn't be able to)
print(f"Can delete? {sathish.has_permission(Permission.DELETE)}") # False

# Grant Delete specifically
sathish.add_permission(Permission.DELETE)
print(f"Can delete now? {sathish.has_permission(Permission.DELETE)}") # True

# """
# How to Implement This: Step-by-Step

# 1.  The "Power of 2" Rule:** Always ensure your permission values are $1, 2, 4, 8, 16, 32, 64, \dots$. If you use a number like $3$, you accidentally grant both $1$ and $2$ (because $1+2=3$). Using `auto()` in `IntFlag` prevents this mistake.
# 2.  The Storage:** In your SQL database, set the column type to `Integer` or `BigInteger`. One 32-bit integer can hold 32 different permissions. A 64-bit integer can hold 64.
# 3.  The API/Frontend:** When sending data to the frontend, you can either send the integer (e.g., `13`) or a list of names. The integer is more efficient for high-traffic apps.
# 4.  Security:** Always perform the bitwise check on the **Server Side** (Python). Never trust a "permission" check done only in JavaScript.

# Summary of Bitwise Operators used:
# `|` (OR):** Sets a bit to 1. Used to **Grant** permission.
# `&` (AND):** Extracts a bit. Used to **Check** permission.
# `~` (NOT):** Flips all bits. Used with AND to **Revoke** permission.
# `^` (XOR):** Flips a specific bit. Used to **Toggle** permission.
# """