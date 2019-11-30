/**
 * Motion Sensors
 * 
 * Suppose you have a hallway filled with circular motion sensors, each
 * centered at a point with a given radius. Find if there is a safe path
 * through the hallway without being detected. Suppose the individual has
 * also has a radius of r.
 * 
 *  -----------------------------
 *    .-----.            .---.
 *   /       \          |  o  |
 *  |    o    |          '---'
 *   \       /--------.
 *    '----//          \
 *         |      o     |
 *  -----------------------------
 * 
 * The sensors are represented as objects containing a coordinate (x, y)
 * where the center is located, and a radius of the sensor's reach. The
 * height of the hallway and radius of the person is also provided.
 */
