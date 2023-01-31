public final class SumTooLargeException extends Exception { 
  public SumTooLargeException(int firstInteger, int secondInteger) { 
    super(String.format("Integers %d and %d sum up to %d, which is larger than 100, the maximum size allowed.",  
          firstInteger, secondInteger, (long)firstInteger + (long)secondInteger); 
 
  public static void assertSumNotTooLarge(int first, int second) throws SumTooLargeException { 
    if((long) first + (long) second) > 100) { // avoiding overflow errors 
      throw new SumTooLargeException(first, second); 
    } 
} 