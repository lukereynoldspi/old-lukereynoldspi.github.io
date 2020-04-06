
/**
 * A pallet is a stack of bricks on a wooden base.
 *
 * @author: Michael Kölling and David J. Barnes
 * @version 2016.02.29
 */
public class Pallet
{
    private static final double BASE_WEIGHT = 6.5;  // in kg
    private static final double BASE_HEIGHT = 15;  // in cm

    private Brick aBrick;
    private int bricksInPlane;
    private int layers;

    /**
     * Create a pallet with a given number of bricks.
     * @param bricksInPlane The number of bricks in each level on the base.
     * @param height The number of bricks stacked on top of each other.
     */
    public Pallet(int bricksInPlane, int layers)
    {
        this.bricksInPlane = bricksInPlane;
        this.layers = layers;
        aBrick = new Brick(8, 20, 12);
    }

    /**
     * @return The weight of the pallet (in kg)
     */
    public double getWeight()
    {
        int numberOfBricks = bricksInPlane * layers;
        return aBrick.getWeight() * numberOfBricks;
    }

    /**
     * @return The layers of this stack (in cm)
     */
    public double getHeight()
    {
        return (aBrick.getHeight() *  layers) + BASE_HEIGHT;
    }
}
