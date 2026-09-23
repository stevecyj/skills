package io.github.stevecyj.webframework;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.io.IOException;
import java.net.InetSocketAddress;
import java.net.ServerSocket;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.time.Duration;
import org.junit.jupiter.api.Test;

class WebApplicationTest {
    private static final HttpClient CLIENT = HttpClient.newHttpClient();

    @Test
    void servesRoutesAndReleasesPortOnStop() throws Exception {
        int port = availablePort();
        WebApplication app = new WebApplication()
                .route("GET", "/users/{id}", request -> Response.text(200,
                        request.pathParameter("id").orElseThrow() + "|"
                                + request.queryParameter("tag").orElseThrow() + "|"
                                + request.header("X-Test").orElseThrow()))
                .route("GET", "/users/new", request -> Response.text(200, "literal"))
                .route("POST", "/users/{id}", request -> new Response(201,
                        java.util.Map.of("Content-Type", "text/plain"), request.body()))
                .route("GET", "/explode", request -> {
                    throw new IllegalStateException("test failure");
                });

        app.start(port);
        try {
            assertThrows(IllegalStateException.class,
                    () -> app.route("GET", "/late", request -> Response.text(200, "late")));
            assertEquals("literal", send(port, "GET", "/users/new", null, false).body());
            assertEquals("42|first|yes", send(port, "GET", "/users/42?tag=first&tag=second",
                    null, true).body());

            HttpResponse<String> posted = send(port, "POST", "/users/42", "payload", false);
            assertEquals(201, posted.statusCode());
            assertEquals("payload", posted.body());

            HttpResponse<String> wrongMethod = send(port, "PUT", "/users/42", "", false);
            assertEquals(405, wrongMethod.statusCode());
            assertEquals("GET, POST", wrongMethod.headers().firstValue("Allow").orElseThrow());
            assertEquals(404, send(port, "GET", "/missing", null, false).statusCode());
            assertEquals(500, send(port, "GET", "/explode", null, false).statusCode());
        } finally {
            app.stop();
        }

        try (ServerSocket socket = new ServerSocket()) {
            socket.setReuseAddress(true);
            socket.bind(new InetSocketAddress("127.0.0.1", port));
            assertTrue(socket.isBound());
        }
    }

    @Test
    void rejectsDuplicateAndInvalidRoutePatterns() {
        WebApplication app = new WebApplication()
                .route("get", "/items/{id}", request -> Response.text(200, "ok"));

        assertThrows(IllegalArgumentException.class,
                () -> app.route("GET", "/items/{id}", request -> Response.text(200, "duplicate")));
        assertThrows(IllegalArgumentException.class,
                () -> app.route("GET", "items", request -> Response.text(200, "invalid")));
        assertThrows(IllegalArgumentException.class,
                () -> app.route("GET", "/items/{id}/{id}", request -> Response.text(200, "invalid")));
    }

    private static int availablePort() throws IOException {
        try (ServerSocket socket = new ServerSocket(0)) {
            return socket.getLocalPort();
        }
    }

    private static HttpResponse<String> send(
            int port, String method, String path, String body, boolean withHeader) throws Exception {
        HttpRequest.Builder builder = HttpRequest.newBuilder(URI.create("http://127.0.0.1:" + port + path))
                .timeout(Duration.ofSeconds(3));
        if (withHeader) {
            builder.header("X-Test", "yes");
        }
        builder.method(method, body == null
                ? HttpRequest.BodyPublishers.noBody()
                : HttpRequest.BodyPublishers.ofString(body, StandardCharsets.UTF_8));
        return CLIENT.send(builder.build(), HttpResponse.BodyHandlers.ofString(StandardCharsets.UTF_8));
    }
}
