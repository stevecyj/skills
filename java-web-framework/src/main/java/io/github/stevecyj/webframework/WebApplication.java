package io.github.stevecyj.webframework;

/** Entry point for registering routes and running the HTTP server. */
public final class WebApplication {
    private final Router router = new Router();
    private JdkHttpServerAdapter adapter;

    public synchronized WebApplication route(String method, String pattern, Handler handler) {
        if (adapter != null) {
            throw new IllegalStateException("Cannot register routes while the server is running");
        }
        router.register(method, pattern, handler);
        return this;
    }

    public synchronized void start(int port) {
        if (adapter != null) {
            throw new IllegalStateException("Server is already running");
        }
        JdkHttpServerAdapter created = new JdkHttpServerAdapter(router);
        created.start(port);
        adapter = created;
    }

    public synchronized void stop() {
        if (adapter != null) {
            adapter.stop();
            adapter = null;
        }
    }
}
