# *****************************************************************************
# *** Gestra V2                                                             ***
# *** Ausführung DLR                                                        ***
# *** V 2.02                                                                ***
# *****************************************************************************

import time
import defaults

loop_time = 0.5


hit_array = [
            [ 0, 1],        #  0 ->  1. Track
            [ 2, 3],        #  1 ->  2. Track
            [ 4, 5],        #  2 ->  3. Track
            [ 0],           #  3 ->  4. Track
            [ 1],           #  4 ->  5. Track
            [ 0],           #  5 ->  6. Track
            [ 0],           #  6 ->  7. Track
            [ 0],           #  7 ->  8. Track
            [ 0],           #  8 ->  9. Track
            [ 0],           #  9 -> 10. Track
            [ 0],           # 10 -> 11. Track
            [ 0],           # 11 -> 12. Track
            [ 0],           # 12 -> 13. Track
            [ 0],           # 13 -> 14. Track
            [ 0],           # 14 -> 15. Track
            [ 0]            # 15 -> 16. Track
]


# -----------------------------------------------------------------------------
def main_loop():

    print("Main Loop")

    rows = len(defaults.Tracks.track_hit_t)
    print(rows)
    for elements in defaults.Tracks.track_hit_t[4]:
        print(elements)

    print("Main End")

# =============================================================================


if __name__ == '__main__':

    main_loop()
    print("=== End of Program ===")

# =============================================================================
