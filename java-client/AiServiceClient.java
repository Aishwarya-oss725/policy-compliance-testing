import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.client.RestClientException;
import org.springframework.http.client.SimpleClientHttpRequestFactory;

public class AiServiceClient {

    private final RestTemplate restTemplate;
    private final String BASE_URL = "http://127.0.0.1:5000";

    public AiServiceClient() {
        SimpleClientHttpRequestFactory factory = new SimpleClientHttpRequestFactory();
        factory.setConnectTimeout(10000);
        factory.setReadTimeout(10000);

        this.restTemplate = new RestTemplate(factory);
    }

    public String describe(String input) {
        try {
            String url = BASE_URL + "/describe";
            ResponseEntity<String> response =
                    restTemplate.postForEntity(url, input, String.class);

            return response.getBody();

        } catch (RestClientException e) {
            System.out.println("Error calling AI service: " + e.getMessage());
            return null;
        }
    }
}