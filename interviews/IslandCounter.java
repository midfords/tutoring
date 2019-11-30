/**
 * Island Counter
 * 
 * Given a 2D array filled with 1s and 0s (1s represent land, and 
 * 0s represent water). Count how many islands there are.
 *
 * Example:
 *   0 1 1 0
 *   1 0 0 1   -> 3
 *   1 0 0 1
 *   1 0 1 1
 * Explanation: There are three distinct groups of adjacent 1s, so we
 * count as 3 islands.
 */

public class IslandCounter {
  private static final int LAND = 1;
  private static final int VISITED = -1;

  public static int count(int[][] map) {
    int c = 0;

    for (int i = 0; i < map.length, i++) {
      for (int j = 0; j < map[i].length; j++) {
        if (map[i][j] == LAND) {
          filterMap(map, i, j);
          c++; // ;)
        }
      }
    }

    return c;
  }

  public static void filterMap (int[][] map, i, j){
    map[i][j] = VISITED;

    if (i+1 < map.length && map[i+1][j] == LAND) {
      filterMap(map, i+1, j);
    }
    if (j+1 < map[i].length && map[i][j+1] == LAND) {
      filterMap(map, i, j+1);
    }
    if (i-1 >= 0 && map[i-1][j] == LAND) {
      filterMap(map, i-1, j);
    }
    if (j-1 >= 0 && map[i][j-1] == LAND) {
      filterMap(map, i, j-1);
    }
  }
}
