# Version numbers are strings that are used to identify unique states of software products.
# A version number is in the format a.b.c.d. and so on where a, b, etc. are numeric strings
# separated by dots. These generally represent a hierarchy from major to minor changes.
# Given two version numbers version1 and version2, conclude which is the latest version number.
# Your code should do the following:
# If version1 > version2 return 1.
# If version1 < version2 return -1.
# Otherwise return 0.
#
# Note that the numeric strings such as a, b, c, d, etc. may have leading zeroes, and
# that the version strings do not start or end with dots. Unspecified level revision numbers default to 0.


def compareVersion(version1, version2):
    # Fill this in.
    nums1 = version1.strip().split(".")
    nums2 = version2.strip().split(".")

    i = 0
    while i < len(nums1) or i < len(nums2):
        a = 0
        b = 0
        if i < len(nums1):
            a = int(nums1[i])
        if i < len(nums2):
            b = int(nums2[i])
        if a > b:
            return 1
        elif a < b:
            return -1
        i += 1
    return 0

version1 = "1.0.1"
version2 = "1"
print(compareVersion(version1, version2))


version1 = "1.0.0"
version2 = "1.0"
print(compareVersion(version1, version2))
