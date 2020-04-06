import java.util.ArrayList;

/**
 * A class to hold details of audio files.
 * 
 * @author David J. Barnes and Michael Kölling
 * @version 2016.02.29
 */
public class MusicOrganizer
{
    // An ArrayList for storing the file names of music files.
    private ArrayList<String> files;
    private ArrayList<String> items;
    /**
     * Create a MusicOrganizer
     */
    public MusicOrganizer()
    {
        files = new ArrayList<>();
        items = new ArrayList<>();
    }
    
    /**
     * Add a file to the collection.
     * @param filename The file to be added.
     */
    public void addFile(String filename)
    {
        files.add(filename);
    }
    
    /**
     * Return the number of files in the collection.
     * @return The number of files in the collection.
     */
    public int getNumberOfFiles()
    {
        return files.size();
    }
    
    /**
     * List a file from the collection.
     * @param index The index of the file to be listed.
     */
    public boolean listFile(int index)
    {
        if(checkIndex(index)) {
            System.out.println(files.get(index));
        }
    }
    public void listFile2()
    {
            String filename = items.get(2);
            System.out.println(filename);
        
    }
     public void checkIndex(int check)
    {
         if(check >= 0 && check <= files.size()-1) {
            }
         else{
            System.out.println("u did this wrong");}
        
    }
     public boolean validIndex(int valid)
    {
         if(valid >= 0 && valid <= files.size()-1) {
             return true;
            }
         else{
            return false;}
        
    }
    /**
     * Remove a file from the collection.
     * @param index The index of the file to be removed.
     */
    public boolean removeFile(int index)
    {
        if(checkIndex(index)) {
            files.remove(index);
        }
    }
}
