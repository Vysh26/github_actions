
def can_pick_up(scan, package_id):
    rows, cols = len(scan), len(scan[0])
    print(rows)
    print(cols)

    # Initialize boundaries for the package
    min_row = rows
    max_row = -1
    max_col = -1

    # Find the vertical span and rightmost column of the package
    for r in range(rows):
        for c in range(cols):
            if scan[r][c] == package_id:
                min_row = min(min_row, r)
                max_row = max(max_row, r)
                max_col = max(max_col, c)

    # Check if any row has a clear horizontal path to the right
    for r in range(min_row, max_row + 1):
        if all(scan[r][c] == 0 for c in range(max_col + 1, cols)):
            return True

    return False


def main():
    # Example scan of the storage unit
    scan = [
        [0, 0, 0, 1, 2],
        [0, 0, 0, 1, 2],
        [0, 3, 3, 5, 2],
        [0, 0, 0, 5, 4],
    ]

    # Test different packages
    packages = [1, 2, 3, 4, 5]

    for pkg in packages:
        print(f"Package {pkg}: {can_pick_up(scan, pkg)}")


if __name__ == "__main__":
    main()
