
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class SHA1Example {
    public static void main(String[] args) throws NoSuchAlgorithmException {
        String text = "Hello, World!";

        MessageDigest md = MessageDigest.getInstance("SHA-1");
        byte[] hash = md.digest(text.getBytes());

        // Convert byte array into signum representation
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < hash.length; i++) {
            String hex = Integer.toHexString(0xff & hash[i]);
            if (hex.length() == 1)
                sb.append('0');
            sb.append(hex);
        }

        System.out.println("Hex format : " + sb.toString());
    }
}